for _ in range(int(input())):
    bob, lim = [int(x) for x in input().split()];
    candycount = 1
    while(True):
        if (bob - candycount < 0):
            bob -= candycount
            break  
        else:
            bob-= candycount
            candycount+=1
            
        if (lim - candycount<0):
            lim -= candycount
            break
        else:
            lim -= candycount
            candycount += 1
    if(bob<lim):
        print("Bob")
    else:
        print("Limak")
