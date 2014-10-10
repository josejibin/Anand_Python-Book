import urllib
import sys
import re
def antihtml(url):
  
  urllib.urlretrieve(url,'az.txt')
  f=open('az.txt').readlines()
 
  for each in f:
    match=re.search('(<)(\w+)(>)' , each)
    if match:
      print match.group(2)
antihtml(sys.argv[1])
