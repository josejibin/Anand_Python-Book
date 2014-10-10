import re
def validate(num):
  match=re.search('^\d\d\d\d\d\d\d\d\d\d$',num)
  if match:
    print 'matches',match.group()
validate('9633975321')
