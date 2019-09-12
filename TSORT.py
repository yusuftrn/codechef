t=int(input())
pow = 10**6
n=[0]*pow
for i in range(t):
	x=int(input())
	n[x]+=1
for q in range(pow):
	for j in range(n[q]):
		print(q)
