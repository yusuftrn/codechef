for _ in range(int(input())):
    N, M, K = [int(x) for x in input().split()]
    if N>M:
        S = M; L = N;
    else:
        S = N; L = M;
    if (S+K)>L:
        print("0")
    else:
        print(L-(S+K))
