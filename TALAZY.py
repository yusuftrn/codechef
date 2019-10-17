for _ in range(int(input())):
    n, b, m = [int(x) for x in input().split()]
    t=0
    while(n):
        if(n==1):
            x=1
        elif(n%2!=0):
            x=(n+1)//2
        else:
            x=n//2
        t += x*m+b
        n=n-x
        m=m*2
    print(t-b)