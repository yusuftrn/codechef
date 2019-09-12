def sum(m):
    return (m*(m+1)/2)
for _ in range(int(input())):
    N = int(input())
    m=0
    while sum(m)<=N:
        m=m+1
    print (m-1)
