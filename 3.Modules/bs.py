import urllib
from BeautifulSoup import BeautifulSoup
urllib.urlretrieve('http://sheldonbrown.com/web_sample1.html','az.txt')
a=open('az.txt').readlines()
for each in a:
  soup=BeautifulSoup(each)
  print soup.prettify()

