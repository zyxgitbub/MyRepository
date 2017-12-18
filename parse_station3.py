# coding:utf-8
import os
import re
import chardet
import requests
import json
from pprint import pprint

url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9035'
response = requests.get(url, verify=False)
stations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', response.text)

'''for index,value in enumerate(stations):
	stations[index]=(stations[index][0].encode('utf8'),stations[index][1].encode('utf8'))

file = open(os.path.abspath('.')+'/stations.py','w')
file.write('stations={\n')

for item in stations:
	if item  == stations[-1]:
		print >> file,"'%s':'%s'" %(item[0],item[1])
	else:
		print >> file,"'%s':'%s'," %(item[0], item[1])
file.write('}\n')
file.close()'''

pprint(dict(stations), indent=4)

