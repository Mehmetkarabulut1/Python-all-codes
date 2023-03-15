
import random
import time
class kumanda():

    def __init__(self, tv_durum = "kapalı", tv_ses = 12 , kanal_listesi = ["trt"] , kanal ="trt" ):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal

    def tv_aç(self):
         if self.tv_durum ==  "açık":
             print("televizyon zaten açık")

         else:
             self.tv_durum = "açık"
             print("televizyon açılıyor... " , self.tv_durum)

    def tv_kapat(self):
        if self.tv_durum == "kapalı":
            print("televizyon zaten kapalı")

        else:
            self.tv_durum = "kapalı"
            print("televizyon kapanıyor... ", self.tv_durum)

    def ses(self):
        while True:
            ses = input("ses açmak için + azaltmak için - tuşuna basınız")


            if ses == "+":
                self.tv_ses += 1
                print("televizyonun güncel ses seviyesi  " , self.tv_ses)
                continue

            elif ses == "-":
                self.tv_ses -= 1
                print("televizyonun güncel ses seviyesi  ", self.tv_ses)
                continue

            else:
                print("ses açma işleminden çıkış yapılıyor")
                break

    def kanal_ekle(self,kanal_ismi):
        self.kanal_listesi.append(kanal_ismi)
        print("Güncel kanal listesi ektedir " , self.kanal_listesi)


    def kanal_çıkarma(self):
        a = 1
        for tarama in self.kanal_listesi:
            print( a , tarama)
            a+=1
        sıra = int(input("kanal sırasını giriniz"))
        if sıra <0 :
            raise ValueError("geçerli değer giriniz")
        self.kanal_listesi.pop(sıra-1)
        print("kanal listeden kaldırıldı" )

    def rastgele(self):
        rastgele = random.randint(0 , len(self.kanal_listesi)-1)
        self.kanal = self.kanal_listesi[rastgele]
        print("şu an kanal" ,self.kanal )

    def __len__(self):
        return len(self.kanal_listesi)

    def __str__(self):
        return "tv_durum: {}\nses_durum: {}\nkanal_durum: {}\nkanal: {}".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)

kuman = kumanda()

print("""
televizyon uygulamasına hoş geldiniz 

TELEVİZYON UYGULAMASI

1. TV AÇ
2. TV KAPAT
3. SES AYARLARI
4. KANAL EKLE
41 KANAL ÇIKAR 
5. KANAL SAYISI ÖĞREN
6. RASTGELE KANAL SEÇME
7. TELEVİZYON BİLGİLERİ

""")

while True:
    while True:
        seçenek = input("lütfen işlem seçiniz: ")
        try:
            n = int(seçenek)
        except:
            print("doğru değer giriniz")
            continue
        break


    if n == 1:
        kuman.tv_aç()
    elif n == 2:
        kuman.tv_kapat()
    elif n == 3:
        kuman.ses()
    elif n == 4:
        kanal_ismi = input("kanal adı giriniz")
        kuman.kanal_ekle(kanal_ismi)
    elif n == 41:
        kuman.kanal_çıkarma()

    elif n == 5:
        len(kuman)
    elif n == 6:
        kuman.rastgele()
    elif n == 7:
        print(kuman)
    else:
        print("önce televizyonu açmalısınız")
        continue