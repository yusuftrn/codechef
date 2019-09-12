def gcd (a,b):
    if (b == 0):
        return a
    else:
         return gcd (b, a % b)
for _ in range(int(input())):
    N,K = [int(x) for x in input().split()]
    grapes = list(map(int, input().split(" ")))
    totalis = 0
    res = grapes[0]
    for c in grapes[1::]:
        res = gcd(res , c)
    print (res)
