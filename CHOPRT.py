for _ in range(int(input())):
    numb = input()
    A = int(numb.split(' ')[0])
    B = float(numb.split(' ')[1])
    if A > B:
        print (">")
    elif A < B:
        print ("<")
    else:
        print ("=")
