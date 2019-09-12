t = int(input())
b = 0; c = 0;
for i in range(t):
    bir, iki = [int(x) for x in input().split()]
    if bir > 1000:
        b = bir*iki
        c = b / 10
        b = b - c
        b = str(b)
        print(b + "00000")
    else:
        c = iki*bir
        c = str(c)
        print(c + ".000000")
