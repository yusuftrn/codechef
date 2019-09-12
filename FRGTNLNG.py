for _ in range(int(input())):
    N, K = [int(x) for x in input().split()]
    forgot = input().split()
    list = []
    for i in range(K):
        list += input().split()
        c = ""
    for i in range(N):
        if forgot[i] in list: c += "YES "
        else: c += "NO "
    print (c)
