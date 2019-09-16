for _ in range(int(input())):
    t = int(input());
    key = input(); key = list(key);
    if (len(key)) == t:
        if "Y" in key and "I" not in key:
            print ("NOT INDIAN");
        elif "I" in key and "Y" not in key:
            print ("INDIAN");
        elif "N" in key and ("Y" or "I" not in key):
            print ("NOT SURE")
