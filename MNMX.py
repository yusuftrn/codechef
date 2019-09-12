for _ in range(int(input())):
    N = int(input())
    array = list(map(int,input().split()))
    count = array[0]
    for i in range(1,N):
        if (array[i]<count):
            count = array[i]
    totalis = count*(N-1)
    print(totalis)
