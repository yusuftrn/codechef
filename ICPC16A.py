for _ in range(int(input())):
    cord = list(map(int,input().split()))
    x1=cord[0]; y1=cord[1]; x2=cord[2]; y2=cord[3];
    if x1>x2 and y1==y2:
        print("left")
    elif x1<x2 and y1==y2:
        print("right")
    elif y1>y2 and x1==x2:
        print("down")
    elif y1<y2 and x1==x2:
        print("up")
    else:
        print("sad")
