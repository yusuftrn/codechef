T = int(input())
list = []
for i in range(T):
  list.append(input())

for j in range(len(list)):
  if '4' in str(list[j]):
    print ("1")
  else:
    print("0")
