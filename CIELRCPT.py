def cielrcpt(n):
    prices = 11
    total = 0
    while n != 0:
        if n/2**prices >= 1:
            n = n - 2**prices
            total += 1
        else:
            prices -= 1
    return total
T = int(input())
for i in range(T):
    n = int(input())
    answ = cielrcpt(n)
    print (answ)
