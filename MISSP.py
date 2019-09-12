for _ in range(int(input())):
    N = int(input())
    a = dict()
    for i in range(N):
        b = int(input())
        a[b] = a.get(b,0)+1
    for key, value in a.items():
        if value%2!=0:
           print(key)
