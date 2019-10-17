for _ in range(int(input())):
    l=list(map(str,input().split()))
    m=list(map(str,input().split()))
    count = 0;
    for i in m:
        if i in l:
            count+=1
    if count >= 2:
        print ("similar")
    else:
        print ("dissimilar")