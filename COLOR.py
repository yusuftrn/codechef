def my_min(list):
    if not list:
        raise ValueError('empty sequence')
    min = list[0]
    for item in list:
        if item < min:
            min = item
    return min
for _ in range(int(input())):
    rooms = int(input())
    colors = str(input())
    colors = [str(i) for i in colors]
    red = colors.count("R"); green = colors.count("G"); blue = colors.count("B");
    list = [len(colors)-red,len(colors)-green,len(colors)-blue]
    print(my_min(list))
