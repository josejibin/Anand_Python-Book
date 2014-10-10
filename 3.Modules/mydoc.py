import re
from inspect import isfunction
def mydoc():
  a=dir(re)
  for each in a:
  
    print each,each.__doc__
mydoc()
