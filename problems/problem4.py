toplam = 0
while True:
    a = input("lütfen sayı giriniz:")
    if a == "q":
        print("sistemden çıkılıyor")
        break
    else:
        a = int(a)
    toplam += a
    print(toplam)