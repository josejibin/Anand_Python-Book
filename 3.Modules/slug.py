import re
def slug(s):
  match=re.search('(^\s*)(\w+)(\s*)(\w+)',s)
  if match:
    print match.group(2)+'-'+match.group(4)
slug("hello world")
