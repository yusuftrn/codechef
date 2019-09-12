def top_sum(N):
    n = list(range(1,N+1))
    n = sum(n)
    return n

for _ in range(int(input())):
    D, N = [int(x) for x in input().split()]
    m = N
    while D:
        m = top_sum(m)
        D = D - 1
    print(m)
