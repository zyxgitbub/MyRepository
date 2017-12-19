#-*- coding: UTF-8 -*- 

import random
import time
import os
import string
 
base = string.digits+string.punctuation
total = 10
lst=[] 
def loop(ss):
  """循环"""
  rt = ''
  for c in ss:
    print c
    if c in '0123456789':
      rt = rt + c
  return rt
 
def regular(ss):
  """正则表达式"""
  import re
  rt = re.sub(r'\D', '', ss)
  return rt
 
def filter_mt(ss):
  """函数式"""
  return filter(lambda c:c.isdigit(), ss)
 
def list_com(ss):
  """列表生成式"""
  isdigit = {'0': 1, '1': 1, '2': 1, '3': 1, '4': 1,
            '5':1, '6':1, '7':1, '8':1, '9':1}.has_key
  return ''.join([x for x in ss if isdigit(x)])



 
def str_tran(ss):
  """string.translate()"""
  table = string.maketrans('', '')
  ss = ss.translate(table,string.punctuation)
  return ss
 
def main():
  for i in xrange(total):
    num = random.randrange(10, 50)
    ss = ''
    for j in xrange(num):
      ss = ss + random.choice(base)
    lst.append(ss)
  '''print lst 
  s1 = time.time()
  map(loop,lst)
  print "loop: ",time.time() - s1
  print '*'*20
  s1 = time.time()
  map(regular, lst)
  print "regular: ", time.time() - s1
  print '*' * 20
  s1 = time.time()
  map(str_tran, lst)
  print "str_tran: ", time.time() - s1
  print '*' * 20
  s1 = time.time()
  map(filter_mt, lst)
  print "filter_mt: ", time.time() - s1
  print '*' * 20
  s1 = time.time()
  map(list_com, lst)
  print "list_com: ", time.time() - s1
'''
