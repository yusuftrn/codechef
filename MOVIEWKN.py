for _ in range(int(input())):
    n = int(input())
    L = []; R = []; a=1; b = 0;
    L = list(map(int, input().split(" ")))
    R = list(map(int, input().split(" ")))
    for i in range(n):
        if L[i]*R[i]>a:
            a = L[i]*R[i]
    for i in range(n):
        if L[i]*R[i] == a:
            if R[i] > b:
                b = R[i]
    print(R.index(b)+1)
