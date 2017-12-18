 # -*- coding: utf-8 -*-
"""命令行火车票查看器

Usage:
    tickets [-dgktz] <from> <to> <date>

Options:
    -h, --help 查看帮助
    -d         动车
    -g         高铁
    -k         快速
    -t         特快
    -z         直达

Examples:
    tickets 上海 北京 2016-10-10
    tickets -dg 成都 南京 2016-10-10
"""

import requests
from docopt import docopt
from prettytable import PrettyTable
from colorama import init, Fore

from stations import stations


init()

class TrainsCollection:

    header = '车次 车站 时间 历时 商务 一等 二等 高级软卧 软卧 硬卧 硬座 无座'.split()

    def __init__(self, available_trains, options,smapdic):
        """查询到的火车班次集合

        :param available_trains: 一个列表, 包含可获得的火车班次, 每个
                                 火车班次是一个字典
        :param options: 查询的选项, 如高铁, 动车, etc...

        :param smapdic  站名字典 
        """
        self.available_trains = available_trains
        self.options = options
        self.stationmap = smapdic

    ''' 
	 def _get_duration(self, raw_train):
        duration = raw_train.get('lishi').replace(':', '小时') + '分'
        if duration.startswith('00'):
            return duration[4:]
        if duration.startswith('0'):
            return duration[1:]
        return duration
    '''
    @property
    def trains(self):
        for rst in self.available_trains:
            raw_train = rst.split('|')	
            train_no = raw_train[3]
            initial =  train_no[0:1].lower()
            #print(self.stationmap[raw_train[6]])
            #print(self.stationmap[raw_train[7]])
            if not self.options or initial in self.options:
                train = [
                    train_no,
                    '\n'.join([Fore.BLUE + self.stationmap[raw_train[6]] + Fore.RESET,
                               Fore.RED + self.stationmap[raw_train[7]] + Fore.RESET]),
                    '\n'.join([Fore.BLUE + raw_train[8] + Fore.RESET,
                               Fore.RED + raw_train[9] + Fore.RESET]),
                    raw_train[10],
                    raw_train[32],
                    raw_train[31],
                    raw_train[30],
                    raw_train[21],
                    raw_train[23],
                    raw_train[28],
                    raw_train[29],
                    raw_train[26],
                ]
	        yield train

    def pretty_print(self):
        pt = PrettyTable()
        pt._set_field_names(self.header)
        for train in self.trains:
            pt.add_row(train)
        print(pt)


def cli():
    """Command-line interface"""
    arguments = docopt(__doc__)
    #print type(arguments['<from>'])
    from_station = stations.get(arguments['<from>'])
    to_station = stations.get(arguments['<to>'])
    #print type(from_station)
    #print arguments['<from>']
    print from_station
    print from_station
    date = arguments['<date>']
#    url = ('https://kyfw.12306.cn/otn/leftTicket/query?'
#           'purpose_codes=ADULT&leftTicketDTO.train_date={}&'
#           'leftTicketDTO.from_station={}&leftTicketDTO.to_station={}').format(
#                date, from_station, to_station
#           )
    url = ('https://kyfw.12306.cn/otn/leftTicket/query?'
           'leftTicketDTO.train_date={}&'
           'leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT').format(
                date, from_station, to_station
           )

    print(url)
    options = ''.join([key for key, value in arguments.items() if value is True])
    r = requests.get(url, verify=False)
    dmp = r.json()['data']['map']
    available_trains = r.json()['data']['result']
    TrainsCollection(available_trains, options,dmp).pretty_print()


if __name__ == '__main__':
    cli()

