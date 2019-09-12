def fact(x):
    c = 1
    if x <= 1:
        return c
    else:
        return (x*fact(x-1))

def Main(T):
    for j in range(T):
        n = int(input())
        print(int(fact(n)))


if __name__ == '__main__':
    T = int(input())
    Main(T)
