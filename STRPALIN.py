for _ in range(int(input())):
    a = str(input())
    b = str(input())
    test = False;
    for i in a:
        if i in b:
            test = True;
            break;
    if test:
        print ("Yes")
    else:
        print ("No")
