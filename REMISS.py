for __ in range(int(input())):
    remiss = input()
    A = int(remiss.split(' ')[0])
    B = int(remiss.split(' ')[1])
    if A >= B:
        print(str(A) + " " + str(int(A+B)))
    else:
        print(str(B) + " " + str(int(A+B)))
