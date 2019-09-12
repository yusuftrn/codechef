for _ in range(int(input())):
    x = int(input())
    y = 0
    for i in range(2,x//2):
        if x%i == 0:
            y=1
            break
    if y == 0:
        print ("yes")
    else:
        print ("no")
