def reverse(f):
  r=open(f).readlines()
  for each in r:
    print each[::-1]
reverse('she.txt')
