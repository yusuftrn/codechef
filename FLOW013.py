for _ in range(int(input())):
    angles = []
    angles =list(map(int, input().split()))
    sum = angles[0] + angles[1] + angles[2]
    if sum == 180:
        print ("YES")
    else:
        print ("NO")
