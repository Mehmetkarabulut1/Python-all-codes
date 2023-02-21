"""liste1 = list(range(0,20))
liste = [i%2  for i in liste1]
print(liste)
a = 0
for i in liste:
    if  i == 1:
        print(liste1[a],"tek sayı")
        a += 1
    else:
        print(liste1[a],"çift sayı")
        a += 1
"""
liste2 = []
sayı =int(input("sayı girniz: "))
for i in range(2,sayı+1):
    sonuc = 0
    for x in range(2,i):
        if i % x == 0:
            sonuc += 1
            break
    if sonuc == 0:
        liste2.append(i)


    print(liste2)