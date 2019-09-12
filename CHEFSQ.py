for _ in range(int(input())):
    a1 = int(input())
    L1 = list(input().split(" "))
    a2 = int(input())
    L2 = list(input().split(" "))
    c = ""
    for i in range(len(L2)):
        if L2[i] in L1: c = "Yes"
        else: c = "No"
    print(c)
