import random
bilgisayark = 0
oyuncuk = 0

def durum():
    print("oyuncu puanı:", oyuncuk, "\nbilgisayar puanı:", bilgisayark)

def bilgisayar_ne_yaptı():
    if bilgisayar == 0:
        print("bilgisayar: taş")
    elif bilgisayar == 1:
        print("bilgisayar: makas")
    else:
        print("bilgisayar: kağıt")
    print("Aynı hamle")


while True:
    bilgisayar = random.randint(0, 2)
    print ("*" * 30 )
    seçenek = input("seçenek giriniz:")
    if oyuncuk == -2 or bilgisayark == -2 or seçenek == "q":
        break
    elif bilgisayar == 0 and seçenek == "makas":
        bilgisayark += 1
        print("bilgisayar: taş")
        print("oyuncu:", seçenek)
        print("-" * 10)
        durum()
        if oyuncuk == 3:
            print("siz kazandınız")
            break
        elif bilgisayark == 3:
            print("bilgisayar kazandı")
            break
    elif seçenek == "kağıt" and bilgisayar == 0:
        oyuncuk += 1
        print("oyuncu:", seçenek)
        print("bilgisayar: taş")
        print("-" * 10)
        durum()
        if oyuncuk == 3:
            print("siz kazandınız")
            break
        elif bilgisayark == 3:
            print("bilgisayar kazandı")
            break

    elif bilgisayar == 1 and seçenek == "kağıt":
        bilgisayark += 1
        print("bilgisayar: makas")
        print("oyuncu:", seçenek)
        print("-" * 10)
        durum()
        if oyuncuk == 3:
            print("siz kazandınız")
            break
        elif bilgisayark == 3:
            print("bilgisayar kazandı")
            break

    elif bilgisayar == 1 and seçenek == "taş":
        oyuncuk += 1
        print("oyuncu:",seçenek)
        print("bilgisayar: makas")
        print("-" * 10)
        durum()
        if oyuncuk == 3:
            print("siz kazandınız")
            break
        elif bilgisayark == 3:
            print("bilgisayar kazandı")
            break

    elif bilgisayar == 2 and seçenek == "taş":
        bilgisayark += 1
        print("bilgisayar: kağıt")
        print("oyuncu:", seçenek)
        print("-" * 10)
        durum()
        if oyuncuk == 3:
            print("siz kazandınız")
            break
        elif bilgisayark == 3:
            print("bilgisayar kazandı")
            break

    elif bilgisayar == 2 and seçenek == "makas":
        oyuncuk += 1
        print("oyuncu:", seçenek)
        print("bilgisayar: kağıt")
        print("-" * 10)
        durum()
        if oyuncuk == 3:
            print("siz kazandınız")
            break
        elif bilgisayark == 3:
            print("bilgisayar kazandı")
            break

    elif (bilgisayar == 0 and seçenek == "taş") or (bilgisayar == 1 and seçenek == "makas") or (bilgisayar == 2 and seçenek == "kağıt"):
        bilgisayar_ne_yaptı()
        continue
    else:
        print("geçersiz hamle")
