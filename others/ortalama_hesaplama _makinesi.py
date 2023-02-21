sınav_notu1 = float(input("vize sonucunuzu giriniz"))
sınav_notu2 = float(input("final sonucunuzu giriniz"))
ödev_notu1 = float(input("1.ödev sonucunuzu giriniz"))
ödev_notu2 = float(input("2.ödev sonucunuzu giriniz"))
#ödevlerin %20 vizenin %30 finalin %50 olduğu etkili olduğunu göze alarak kodlayınız
ortalama = (ödev_notu1+ödev_notu2)*(2/20) + sınav_notu1*(3/10) + sınav_notu2*(5/10)
print(ortalama)
if ortalama < 60:
    print("FF")
elif ortalama >= 90 and ortalama <= 100:
    print("AA")
elif ortalama >= 85 and ortalama <= 100:
    print("BA")
elif ortalama >= 80 and ortalama <= 100:
    print("BB")
elif ortalama >= 75 and ortalama <= 100:
    print("CB")
elif ortalama >= 70 and ortalama <= 100:
    print("CC")
elif ortalama >= 65 and ortalama <= 100:
    print("CB")
elif ortalama >= 60 and ortalama <= 100:
    print("DD")
else:
    print("öğrenci işlerine gidiniz")
