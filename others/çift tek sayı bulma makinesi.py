liste = int(input("Lütefen sayınızı giriniz:"))

if liste % 2 == 0:
    print("sayınız : {} , çift sayı".format(liste))
else:
    print("sayınız : {} , tek sayı".format(liste))



def tek_çift():
    sayı = int(input("sayı:"))
    if sayı % 2 == 0:
        return sayı
    elif sayı % 2 != 0:
        raise ValueError("hata fırlatıldı")

liste = list(range(0,44))

for sayı in liste:
    if sayı % 2 == 0:
        print("sayı:{}".format(sayı))
