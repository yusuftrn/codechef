while True:
    n = int(input())
    if n > 0:
        l = list(map(int, input().split()))
        k = [0]*n
        for i in range(0, n):
            k[l[i]-1] = i+1
        if l == k :
            print("ambiguous")
        else:
            print("not ambiguous")
    else:
        break
