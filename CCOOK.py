for _ in range(int(input())):
    dev = str(input().split());
    count = 0;
    for i in dev:
        if i == "1":
            count += 1;
    if count == 0:
        print ("Beginner")
    elif count == 1:
        print("Junior Developer")
    elif count == 2:
        print("Middle Developer")
    elif count == 3:
        print("Senior Developer")
    elif count == 4:
        print("Hacker")
    else:
        print("Jeff Dean")