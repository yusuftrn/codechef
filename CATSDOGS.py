for _ in range(int(input())):
    C, D, L = [int(x) for x in input().split()]
    if L%4==0 and L//4<=C+D and L//4>=D+max(C-2*D,0):
        print("yes")
    else:
        print("no")
