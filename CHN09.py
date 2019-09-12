t=int(input())
while t:
    l =input()
    d = dict((x,l.count(x)) for x in set(l))
    paint = 0
    if d['a']>d['b']:
        paint = d['b']
    elif d['b']>d['a']:
        paint = d['a']
    else:
        paint = 0
    t = t - 1
    print(paint)
