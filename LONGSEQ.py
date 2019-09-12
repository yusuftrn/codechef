for _ in range(int(input())):
    n = str(input())
    n = [int(i) for i in n]
    d = dict((x,n.count(x)) for x in set(n))
    if len(n) == 1:
        print("Yes")
    else:
        if 0 in d.keys() and 1 in d.keys():
            if (d[0] == 1):
                print("Yes")
            elif (d[1] == 1):
                print("Yes")
            else:
                print("No")
        else:
            print("No")
