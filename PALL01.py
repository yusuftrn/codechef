## isPalindrome
for _ in range(int(input())):
    y = input();
    if (y==y[::-1]):
        print ("wins")
    else:
        print ("losses")
