def reverse(f):
  r= open(f)
  r=r.readlines()
  e=r[::-1]
  for each in e:
    print each
reverse('she.txt')
