sayı = (input("sayı giriniz: "))
basamaksayısı = len(sayı)
sayı = int(sayı)
toplam = 0
gecicisayı = sayı
sonbasamak = 0

while gecicisayı > 0:
    sonbasamak = gecicisayı % 10
    toplam += sonbasamak ** basamaksayısı
    gecicisayı //= 10
    print(toplam)
    if toplam == sayı:
        print("armstrong")
        break



