for i in range(int(input())):
    s=input()
    list=[]
    rnp_is =''
    for j in s:
        if j=='(' or j=='+' or j=='-' or j=='*' or j=='/' or j=='^' :
            list.append(j)
        elif j==')':
            rnp_is = rnp_is + list.pop()
            list.pop()
        else:
            rnp_is = rnp_is + j
    print (rnp_is)
