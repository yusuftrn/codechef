T = int(input())
list =[]
for i in range(T):
  list.append(input())

def firstDigit(n):
    while n >= 10:
        n = n / 10;
    return int(n)

def lastDigit(n) :
    return (n % 10)

for i in range(len(list)):
  x = int(list[i])
  total = firstDigit(x) + lastDigit(x)
  print (total)
