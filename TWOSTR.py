for _ in range(int(input())):
    X = list(input()); Y = list(input());
    q_ = 0; q_eq = 0; q__ = 0;
    lento = int(len(X))
    if lento == len(Y):
        for i in range(lento):
            if X[i] == Y[i] and X[i] != '?':
                q_+=1
            elif X[i] == Y[i] and X[i] == '?':
                q_eq+=1
            elif X[i] == '?' or Y[i] == '?' :
                q__+=1
    else:
        break;
    eq = lento - q_ - q_eq - q__
    if eq == 0:
        print("Yes")
    else:
        print("No")
