mesai_ücret_isim_listesi = []

def liste_ekleme():
    #global mesai_ücret_isim_listesi
    mesai_ücret_isim_listesi.append((calısan_ismi + " = " +str(mesai_kazancı)))
    print(mesai_ücret_isim_listesi)
    return mesai_ücret_isim_listesi


while True:

    mesai_saati = int(input("yapılan mesai:"))
    mesai_ücreti = 1

    if mesai_saati > 0 and mesai_saati <= 10:
        calısan_ismi = input("çalışan ismi:")
        mesai_ücreti = 1
        mesai_kazancı = mesai_saati * mesai_ücreti
        liste_ekleme()
        continue
    elif mesai_saati > 10 and mesai_saati <= 20:
        calısan_ismi = input("çalışan ismi:")
        mesai_ücreti = 2
        mesai_kazancı = mesai_saati * mesai_ücreti
        print(mesai_kazancı)
        liste_ekleme()
        continue
    elif mesai_saati > 20 and mesai_saati <= 40:
        calısan_ismi = input("çalışan ismi:")
        mesai_ücreti = 3
        mesai_kazancı = mesai_saati * mesai_ücreti
        print(mesai_kazancı)
        liste_ekleme()
        continue
    elif mesai_saati > 40 and mesai_saati <=100:
        calısan_ismi = input("çalışan ismi:")
        mesai_ücreti = 4
        mesai_kazancı = mesai_saati * mesai_ücreti
        print(mesai_kazancı)
        liste_ekleme()
        continue
    else:
        print("çıkış yapılıyor")
        break

print(mesai_ücret_isim_listesi)
def çalışan_mesai_ücreti_çağırma(isim,mesai_saat):
    print("listedeki sırası: ",mesai_ücret_isim_listesi.index(isim + " = " + str(mesai_saat))+1)

çalışan_mesai_ücreti_çağırma("m",30)
