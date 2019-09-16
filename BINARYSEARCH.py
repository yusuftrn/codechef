##Liste yarat
se = [""]*100
for i in range(100):
    se[i] = i
aranacak = int(input())

#Sınırlarımız
i = 1;
j = 100;

#Binary Algoritması
while (i<j):
    m = int((i+j)/2)
    if aranacak > se[m]:
        i = m + 1;
    else:
        j = m;
#Çözüm Kümesi
if aranacak == se[i]:
    print("Konum: %s", i)
else:
    print ("Bulumadı")