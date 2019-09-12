for _ in range(int(input())):
    l = []
    win = 0; lose = 0;
    l=list(map(int,input().split()))
    for i in range(len(l)):
        if l[i]%2 == 0:
            win = win + 1
        else:
            lose = lose +1
    if win > lose:
        print ("READY FOR BATTLE")
    else:
        print ("NOT READY")
