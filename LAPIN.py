for _ in range(int(input())):
    lap = input();
    isdouble = len(lap)/2
    issingle = (len(lap)-1)/2
    if isdouble == int(isdouble):
        a = ""; b = "";
        for i in lap[0:int(isdouble)]:
            a = a + i
        for j in lap[int(isdouble):len(lap)]:
            b = b + j
        a = list(a); a.sort();
        b = list(b); b.sort();
        if a == b:
            print ("YES")
        else:
            print ("NO")
    else:
        a = ""; b = "";
        for i in lap[0:int(issingle)]:
            a = a + i
        for j in lap[int(issingle)+1:len(lap)]:
            b = b + j
        a = list(a); a.sort();
        b = list(b); b.sort();
        if a == b:
            print ("YES")
        else:
            print ("NO")