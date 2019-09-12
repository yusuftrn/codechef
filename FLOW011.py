for _ in range(int(input())):
    sal = int(input())
    if sal < 1500:
        gross = sal + sal*(1/10) + sal*(9/10)
    else:
        gross = sal + 500 + sal*(98/100)
    print(gross)
