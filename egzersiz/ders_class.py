class dersler():
    def __init__(self, vize_sayısı = 0 , ödev_sayısı = 0, final_sayısı = 0 , vize_oran = 0 , ödev_oran = 0 ,
                 final_oran = 0 , başarı ="hesaplanmadı",vize_ortalama = 0 ,final_ortalama = 0 , ödev_ortalama = 0, ders_adı = "NoData"):
        self.vize_sayısı = vize_sayısı
        self.ödev_sayısı = ödev_sayısı
        self.final_sayısı = final_sayısı
        self.vize_oran = vize_oran
        self.ödev_oran = ödev_oran
        self.final_oran = final_oran
        self.başarı = başarı
        self.vize_ortalama = vize_ortalama
        self.final_ortalama  = final_ortalama
        self.ödev_ortalama = ödev_ortalama
        self.seçim = ders_adı

    def ders_girme(self):
        ders_adı = input("ders giriniz: ")
        self.seçim = ders_adı

    def vize_sgirme(self):
        while True:
            vize_sayısıs = int(input("vize sayısını giriniz: "))
            if vize_sayısıs == 0:
                break
            self.vize_sayısı = vize_sayısıs
            break

    def ödev_sgirme(self):
        ödev_sayısıs = int(input("ödev sayısını giriniz: "))
        self.ödev_sayısı = ödev_sayısıs

    def final_sgirme(self):
        final_sayısıs = int(input("final sayısını giriniz: "))
        self.final_sayısı = final_sayısıs

    def vize_ogirme(self):
        vize_orans = float(input("vize oranını giriniz: "))
        self.vize_oran = vize_orans

    def ödev_ogirme(self):
        ödev_orans = float(input("ödev oranını giriniz: "))
        self.ödev_oran = ödev_orans

    def final_ogirme(self):
        final_orans = float(input("final oranını giriniz: "))
        self.final_oran = final_orans

    def başar(self):
        vize_toplam = 0
        for i in range(1,self.vize_sayısı+1):
            vize_notu = float(input("{}. vize notu: " .format(i)))
            vize_toplam += vize_notu
        self.vize_ortalama = vize_toplam / self.vize_sayısı

        final_toplam = 0
        for i in range(1, self.final_sayısı+1):
            final_notu = float(input("{}. final notu: ".format(i)))
            final_toplam += final_notu
        self.final_ortalama = final_toplam / self.final_sayısı

        ödev_toplam = 0
        for i in range(1, self.ödev_sayısı+1):
            ödev_notu = float(input("{}. ödev notu: ".format(i)))
            ödev_toplam += ödev_notu
        self.ödev_ortalama = ödev_toplam / self.ödev_sayısı

        average = self.vize_ortalama * self.vize_oran + self.ödev_ortalama * self.ödev_oran + self.final_ortalama * self.final_oran

        print("not ortalamanız: {} ".format(average))

        ortalama = average
        ort = "boş"
        if average < 60:
            ort = "FF"
            print("Başarı harf notunuz: {}".format(ort))
            print(ort)
            self.başarı = ort
        elif ortalama >= 90 and ortalama <= 100:
            ort = "AA"
            print("Başarı harf notunuz: {}".format(ort))
            self.başarı = ort
        elif ortalama >= 85 and ortalama <= 100:
            ort = "BA"
            print("Başarı harf notunuz: {}".format(ort))
            self.başarı = ort
        elif ortalama >= 80 and ortalama <= 100:
            ort = "BB"
            print("Başarı harf notunuz: {}".format(ort))
            self.başarı = ort
        elif ortalama >= 75 and ortalama <= 100:
            ort = "CB"
            print("Başarı harf notunuz: {}".format(ort))
            self.başarı = ort
        elif ortalama >= 70 and ortalama <= 100:
            ort = "CC"
            print("Başarı harf notunuz: {}".format(ort))
            self.başarı = ort
        elif ortalama >= 65 and ortalama <= 100:
            ort = "DC"
            print("Başarı harf notunuz: {}".format(ort))
            self.başarı = ort
        elif ortalama >= 60 and ortalama <= 100:
            ort = "DD"
            print("Başarı harf notunuz: {}".format(ort))
            self.başarı = ort
        else:
            print(
                """
                Hay Aksi! Bir sorunla karşılaştık.
                Lütfen ders sorumlusu ile görüşünüz
                """
            )

    def bilgiler(self):
        return "ders_Adı: {} \nvize sayısı: {}\nödev sayısı: {}\nfinal sayısı: {} \nvize oran: {} \nfinal oran: {} \nödev oran: {}\nharf notu : {}\n"\
            .format(self.seçim, self.vize_sayısı,self.ödev_sayısı,self.final_sayısı,self.vize_oran,self.final_oran,self.ödev_oran , self.başarı)


list_ders_bilgi = list()
while True:
    seçim =dersler()
    seçim.ders_girme()
    seçim.vize_sgirme()
    seçim.final_sgirme()
    seçim.ödev_sgirme()
    seçim.vize_ogirme()
    seçim.final_ogirme()
    seçim.ödev_ogirme()
    seçim.başar()
    list_ders_bilgi.append(seçim.bilgiler())
    list_ders_bilgi.append("-------------\n")


    with open("dönem.txt" ,"a" , encoding="utf-8") as file:
        for i in list_ders_bilgi:
            file.write(i)


