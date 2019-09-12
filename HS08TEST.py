money = input()
p = int(money.split(' ')[0])
t = float(money.split(' ')[1])

if t >= p + 0.5 and p % 5 == 0:
    print("{:0.2f}".format(t - (p + 0.5)))
else:
    print("{:0.2f}".format(t))
