for _ in range(int(input())):
    users = int(input())
    a1 = list(input().split(" "))
    a2 = list(input().split(" "))
    totalis = 0
    if int(a2[0])<=int(a1[0]):
        totalis += 1
    for i in range(1,users):
        x = int(a1[i])-int(a1[i-1])
        if int(a2[i])<=x:
            totalis += 1
    print (totalis)
