sayı = input("sayı:")
basamksayısı=len(sayı)
sayı = int(sayı)
basamak = 0
toplam = 0
gecici_sayı = sayı
while (gecici_sayı > 0):
    basamak = gecici_sayı % 10
    toplam += basamak ** basamksayısı
    gecici_sayı //= 10

if sayı == toplam:
    print("armstrong")
else:
    print("değil")
