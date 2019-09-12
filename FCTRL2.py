def fact(x):
	if x <= 1:
		return x
	else:
		return (x*fact(x-1))
		
def Main(T):
    for j in range(T):
        n = int(input())
        print(fact(n))


if __name__ == '__main__':
    T = int(input())
    Main(T)
