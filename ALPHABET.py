word=input()
n=int(input())
for _ in range(n):
    s=input()
    count=0
    for a in s:
        if a in word:
            count+=1
    if count==len(s):
        print('Yes')
    else:
        print('No')
