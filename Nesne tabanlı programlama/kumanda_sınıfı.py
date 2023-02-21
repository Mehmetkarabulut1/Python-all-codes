import random
import time
class kumanda():
    def __init__(self,tv_durum = "kapalı",ses_durum = 0, kanal_durum = ["trt"], kanal = "trt" ):
        self.tv_durum = tv_durum
        self.ses_durum = ses_durum
        self.kanal_durum = kanal_durum
        self.kanal = kanal

    def tv_aç(self):
        self.tv_durum == "açık"
        """
        if self.tv_durum == "açık":
            print("televizyon zanten açık")

        else:
            print("televizyon açılıyor")
            time.sleep(1)
            print("televizyon açık")
            self.tv_durum == "açık"
        """

    def tv_kapat(self):
        self.tv_durum == "kapalı"
        """if self.tv_durum == "kapalı":
            print("televizyon zaten kapalı")
        else:
            print("televizyon kapatılıyor")
            time.sleep(1)
            print("televizyon kapalı")
            self.tv_durum == "kapalı"
        """

    def tv_ses(self):
        while True:
            ses = input("ses arttırmak için '>' \nses azaltmak için '<' \nçıkış için : çıkış\n")
            if (ses == "<"):
                if (self.ses_durum != 0):
                    self.ses_durum -= 1
                    print("ses = {}".format(self.ses_durum) )
            elif (ses == ">"):
                if(self.ses_durum < 32):
                    self.ses_durum += 1
                    print("ses = {}".format(self.ses_durum) )
            else:
                print("çıkış yapılıyor")
                time.sleep(1)
                print("ses güncellendi = {}".format(self.ses_durum))
                break

    def kanal_ekle(self,kanal_ismi):
        self.kanal_durum.append(kanal_ismi)
        time.sleep(1)
        print("güncel kanal listesi", self.kanal_durum)

    def kanal_çıkar(self):
        print(self.kanal_durum)
        sıra = int(input("kanalının listedeki numarasını giriniz"))
        self.kanal_durum.pop(sıra-1)
        print("kanal listeden çıkartılıyor...")
        time.sleep(1)
        print("kanal listeden çıkartıldı!" + " mevcut kanal listeniz:", self.kanal_durum)

    def kanal_seçme(self):
        rastgele = random.randint(0,len(self.kanal_durum)-1)
        self.kanal = self.kanal_durum[rastgele]
        time.sleep(1)
        print("şu anki kanal", self.kanal)

    def __len__(self):
        return len(self.kanal_durum)

    def __str__(self):
        return "tv_durum: {}\nses_durum: {}\nkanal_durum: {}\nkanal: {}".format(self.tv_durum,self.ses_durum,self.kanal_durum,self.kanal)

kumanda = kumanda()
print("""

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
    işlem = input("işlem seçiniz:")
    if işlem == "1":
        kumanda.tv_aç()
        #time.sleep(1)
        print("televizyon açılıyor...")
        time.sleep(1)
        print("televizton açık")

        while True:
            işlem1 = input("işlem seçiniz:")
            if (işlem1 == "2"):
                time.sleep(1)
                print("Televizyon kapatılıyor...")
                kumanda.tv_kapat()
                break
            elif (işlem1 == "3"):
                kumanda.tv_ses()
            elif (işlem1 == "4"):
                 kanal_ismi = input("kanal isimlerini ',' ile ayırarak girin:")
                 kanal_listesi = kanal_ismi.split(",")
                 for eklenecekler in kanal_listesi:
                    kumanda.kanal_ekle(eklenecekler)
            elif (işlem1 == "41"):
                kumanda.kanal_çıkar()
            elif (işlem1 == "5"):
                print("kanal sayısı:",len(kumanda))
            elif (işlem1 == "6"):
                kumanda.kanal_seçme()
            elif (işlem1 == "7"):
                print(kumanda)
            else:
                print("geçersiz işlem")
                continue

    elif kumanda.tv_durum == "kapalı":
        print("önce televizyonu açmalısın")
        continue