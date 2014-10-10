import re
import urllib
def links(url):
  uf=urllib.urlopen(url)
  text=uf.read().split()
  
  for each in text:
    match=re.search('http://\w+\S+',each)
    if match:
      print match.group()
links('http://www.cpan.org/SITES.html')
