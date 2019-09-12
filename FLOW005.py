for _ in range(int(input())):
    money = int(input())
    count = 0
    while money != 0:
        if money >= 100:
            money = money - 100
            count += 1
        elif money >= 50 and money < 100:
            money = money - 50
            count += 1
        elif money >= 10 and money < 50:
            money = money - 10
            count += 1
        elif money >= 5 and money < 10:
            money = money - 5
            count += 1
        elif money >= 2 and money < 5:
            money = money - 2
            count += 1
        elif money >= 1 and money < 2:
            money = money - 1
            count += 1
    print (count)
