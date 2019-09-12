for _ in range(int(input())):
    M, x, y = [int(x) for x in input().split()]
    cops = (input().split())
    houselist=[]
    safe = 0
    safety_score = x*y
    for q in range(1,101):
        houselist.append(q)
    for i in cops:
        cops_plus = int(i) + safety_score
        cops_minus = int(i) - safety_score
        if cops_minus < 1:
            cops_minus = 1
        if cops_plus > 100:
            cops_plus = 100
        for j in range(cops_minus-1,cops_plus):
            houselist[j]=0
    for k in houselist:
        if k!= 0:
            safe +=1

    print(safe)
