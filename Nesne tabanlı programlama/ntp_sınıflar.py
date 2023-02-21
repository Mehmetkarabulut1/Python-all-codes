class araba():
    model = "honda"
    renk = "kırmızı"
    yıl = 2022
    beygir = 100
    silindir = 4


araba1 = araba()
print(araba1.silindir,"araba 1")

araba2 = araba()
print(araba2.silindir,"araba 2")

class araba():

    def __init__(self,model = "bilgim yok",yıl = "bilgim yok",renk = "bilgim yok",beygir = "bilgim yok",silindir = "bilgim yok"):
        self.model = model
        self.renk = renk
        self.yıl = yıl
        self.beygir = beygir
        self.silindir = silindir

arabax = araba(beygir = 200,silindir = 5)
print(arabax.beygir)
print(arabax.model)
print(arabax.silindir)
print(arabax)


class çalışan():

    def __init__(self, isim, maaş, depertman):
        self.isim = isim
        self.maaş = maaş
        self.depertman = depertman

    def bilgilerigöster(self):
        print("""
        çalışan sınıfının bilgileri...

        isim = {}
        maaş = {}
        depertman = {} 
        """.format(self.isim, self.maaş, self.depertman))

    def zam_yap(self, zam_miktarı):
        self.maaş += zam_miktarı

    def depertman_değiştir(self, yeni_depertman):
        self.depertman = yeni_depertman

    def isim_değiştir(self, yeni_isim):
        self.isim = yeni_isim

mehmet = çalışan("mehmet",5500,"petrol")
mehmet.zam_yap(10000)
mehmet.depertman_değiştir("doğalgaz")
mehmet.bilgilerigöster()

class yönetici(çalışan):

    def zam_yap(self, zam_miktarı):
        self.maaş *= zam_miktarı

mehmet1 = yönetici("mehmet1",10,"123456")
mehmet1.zam_yap(15222)
mehmet1.depertman_değiştir("müdür")
mehmet1.bilgilerigöster()

k1 = set("pijamalıyağızhastaşoföreçabucakgüvendi")
k2 = set("istanbulteknik")
print(k1|k2) #  "|" kavramı iki kümeyi birleştirmeye yarar
print(k1-k2) # k1de olup k2de olamayan elemanları alacak
print(k1&k2) #kesişimleri alır