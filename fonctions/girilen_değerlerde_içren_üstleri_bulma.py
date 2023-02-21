#Girilen değer aralıklarında istenilen tabanın üstlerini yazdırır.
def üst_bulma():
    son_sayı = int(input("son sayı:"))
    basalangıc_sayı = int(input("başlangıç sayı:"))
    if basalangıc_sayı == 0:
        print("""
        !!! uyarı başlangıç sayısı sıfır giremezsiniz !!!
        """)
        basalangıc_sayı = int(input("başlangıç sayı:"))
    taban = int(input("taban sayı:"))
    üst = 0

    while son_sayı > basalangıc_sayı:

        if son_sayı / taban > 0:
            son_sayı /= taban
            üst += 1
            print(taban ** üst)