"""
i = 0
while (i < 10):
    if (i == 5):
        break
    print(i)
    i += 1
"""
"""
liste = [1,2,3,4,5,6]
for a in liste:
    if (a == 5):
        break
    print(a)
"""
a = 0
isim = list()
while True:
    isim1 = input("isminizi giriniz:")
    if (isim1 == "q"):
        print("sistemden çıkılıyor")
        print("listenin son hali ", isim)
        break
    isim.append(isim1)
    isim.sort()
    print("isim : {} ".format(isim))
