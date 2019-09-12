for _ in range(int(input())):
    N, K = [int(x) for x in input().split()]
    l=list()
    for i in range(1,K+1):
	       l.append(N%i)
    print(max(l))
