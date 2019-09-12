def lcm(a,b):
  m = a*b
  while a!=0 and b!=0:
    if a>b:
      a %=b
    else:
      b %=a
  return m//(a+b)

t = int(input())
for i in range(t):
    a, b = [int(x) for x in input().split()]
    gcd = int((a*b)/(lcm(a,b)))
    print(str(gcd) + " " + str(lcm(a,b)))
