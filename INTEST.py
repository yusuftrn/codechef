a, b = [int(x) for x in input().split()]
k=0
for i in range(a):
    c = int(input())
    if c%b==0:
        k = k+1
    else:
        pass
print (k)
