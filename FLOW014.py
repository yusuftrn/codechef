for _ in range(int(input())):
    l = list(input().split(" "))
    h = float(l[0]); c = float(l[1]); t = float(l[2]);
    if h>50.0 and c<0.7 and t>5600.0:
        print("10")
    elif h>50.0 and c<0.7:
        print("9")
    elif t>5600.0 and c<0.7:
        print("8")
    elif h>50.0 and t>5600.0:
        print("7")
    elif h>50.0 or c<0.7 or t>5600.0:
        print("6")
    else:
        print("5")
