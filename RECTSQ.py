def lcm(a,b):
  m = a*b
  while a!=0 and b!=0:
    if a>b:
      a %=b
    else:
      b %=a
  return m//(a+b)
for i in range(int(input())):
    a, b = [int(x) for x in input().split()]
    line = int((a*b)/(lcm(a,b))) # means gcd(a,b)
    sq = (a*b)/(line*line)
    sq = int(sq)
    print(sq)
