for _ in range(int(input())):
    N, K = [int(x) for x in input().split()];
    l = list(map(int,input().split()));
    res = "";
    for i in l:
        if K >= i:
            res += "1";
            K = K - i;
        else:
            res += "0";
    print (res)