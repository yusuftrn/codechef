def integerdiv(a,b):
    if a>b:
        return int(a/b);
    else:
        return int(b/a);
for _ in range(int(input())):
    a, b, n = [int(x) for x in input().split()];
    if (n%2 !=0):
        a = a * 2
    print (integerdiv(a,b))