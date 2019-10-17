def gcd(a, b): 
    if (a == 0): 
        return b 
    return gcd(b % a, a) 

for _ in range(int(input())):
    l = [int(x) for x in input().split()]
    l = l[1:]
    le = len(l)
    gc = gcd(l[0], l[1])
    if le>=3:
        for i in range(2,le):
            gc = gcd(gc,l[i]);
    else:
        gc = gcd(l[0], l[1])
    for i in l:
        if i/gc == int(i/gc):
            print (int(i/gc), end = " ")
        else:
            print (int(i), end = " ")
    print (" ")