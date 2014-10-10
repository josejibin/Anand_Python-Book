import os
import re
import sys
import urllib
def wget(url):
   match=re.search('\w+.html',url)
   if match:
     m=match.group()
     t=open(match.group(),'a')
     print t
   else:
     t=open('index.html','w')
     m='index.html'
   urllib.urlretrieve(url,m)
wget(sys.argv[1])
