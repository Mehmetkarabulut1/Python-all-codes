print("""
MEHMET BANK 
HOŞGELDİNİZ

1. İŞLEM BAKİYE SORGULAMA
2. İŞLEM PARA YATIRMA 
3. İŞLEM PARA ÇEKME
4. ÇIKMAK İÇİN 4 e BASIN
"""
)
bakiye = 1000
a = 0
son_bakiye = bakiye
while True:
    islem = int(input("işlem seçiniz:"))

    if islem == 1:
        print(son_bakiye)

    elif islem == 2:
        a = int(input("yatrılacak tutarı giriniz:"))
        son_bakiye = son_bakiye + a
        print("son bakiyeniz: {}".format(son_bakiye))

    elif islem == 3:
        a = int(input("çekilecek tutarı giriniz:"))
        if bakiye - a < 0:
            print("lütfen geçerli bir tutar giriniz")
            continue
        elif bakiye - a > 0:
            print("paranız hazırlanıyor")
        son_bakiye  = son_bakiye - a
        print("son bakiyeniz: {}".format(son_bakiye))

    if islem == 4:
        print("programdan çıkılıyor yine bekleriz")
        break

    if islem > 4:
        print("geçersiz işlem seçtiniz")