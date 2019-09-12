t=int(input())
while t:
    n=int(input())
    list=[int(x) for x in input().split()]
    list.sort()
    print(list[0]+list[1])
    t=t-1
