for _ in range(int(input())):
    s = list(input())
    count = 0
    for i in s:
        m = s.count(i)
        if m>count:
            count = m
    if count == len(s) - count:
        print('YES')
    else:
        print('NO')
