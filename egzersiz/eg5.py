def hesaplama(kimya ,math):
    while True:
        vize1 = (input("vize1 sonucunu girniz: "))
        vize2 = (input("vize2 sonucunu girniz: "))
        final = (input("final notunu girniz: "))
        vizeratio = (input("vize etkileme oranını girniz: "))
        finalratio = (input("final etkileme oranını girniz: "))
        try:
            v1 = float(vize1)
            v2 = float(vize2)
            f = float(final)
            vr = float(vizeratio)
            fr = float(finalratio)
        except ValueError:
            print("lütfen girdiğiniz sonuç ve ya sonuçları kontrol edip tekrar giriniz")
            continue
        break


    average = v1 * (vr) + v2 * (vr) + f * (fr)
    print("not ortalamanız: {} ".format(average))

    ortalama = average
    ort = "boş"
    if average < 60:
        ort = "FF"
        print("Başarı harf notunuz: {}".format(ort))
        print(ort)
    elif ortalama >= 90 and ortalama <= 100:
        ort = "AA"
        print("Başarı harf notunuz: {}".format(ort))
    elif ortalama >= 85 and ortalama <= 100:
        ort = "BA"
        print("Başarı harf notunuz: {}".format(ort))
    elif ortalama >= 80 and ortalama <= 100:
        ort = "BB"
        print("Başarı harf notunuz: {}".format(ort))
    elif ortalama >= 75 and ortalama <= 100:
        ort = "CB"
        print("Başarı harf notunuz: {}".format(ort))
    elif ortalama >= 70 and ortalama <= 100:
        ort = "CC"
        print("Başarı harf notunuz: {}".format(ort))
    elif ortalama >= 65 and ortalama <= 100:
        ort = "DC"
        print("Başarı harf notunuz: {}".format(ort))
    elif ortalama >= 60 and ortalama <= 100:
        ort = "DD"
        print("Başarı harf notunuz: {}".format(ort))
    else:
        print("Dersin sorumlusu olduğu hocanız ile görüşün")

while True:
    ders = input("""
    1. math
    2. kimya
    ! çıkış için q ya basınız
    
    print dersi yazınız:
    """)

    if ders == "math":
        hesaplama()

    elif ders == "kimya":
        hesaplama()

    elif ders == "q":
        break

    else:
        print("istenilen derse ait girdi bulunamadı!")

hesaplama()

def ort_hesaplama_math(vize1 : "girilimedi", vize2 : "girilmedi" , final : "girilmedi"):
    while True:
        vizeratio = (input("vize etkileme oranını girniz: "))
        finalratio = (input("final etkileme oranını girniz: "))
        try:
            v1 = float(vize1)
            v2 = float(vize2)
            f = float(final)
            vr = float(vizeratio)
            fr = float(finalratio)
        except ValueError:
            print("lütfen girdiğiniz sonuç ve ya sonuçları kontrol edip tekrar giriniz")
            continue
        break

    average = v1 * (vr) + v2 * (vr) + f * (fr)
    print("not ortalamanız: {} ".format(average))

    ortalama = average
    ort = "boş"
    if average < 60:
        ort = "FF"
        print("Başarı harf notunuz: {}".format(ort))
        print(ort)
    elif ortalama >= 90 and ortalama <= 100:
        ort = "AA"
        print("Başarı harf notunuz: {}".format(ort))
    elif ortalama >= 85 and ortalama <= 100:
        ort = "BA"
        print("Başarı harf notunuz: {}".format(ort))
    elif ortalama >= 80 and ortalama <= 100:
        ort = "BB"
        print("Başarı harf notunuz: {}".format(ort))
    elif ortalama >= 75 and ortalama <= 100:
        ort = "CB"
        print("Başarı harf notunuz: {}".format(ort))
    elif ortalama >= 70 and ortalama <= 100:
        ort = "CC"
        print("Başarı harf notunuz: {}".format(ort))
    elif ortalama >= 65 and ortalama <= 100:
        ort = "DC"
        print("Başarı harf notunuz: {}".format(ort))
    elif ortalama >= 60 and ortalama <= 100:
        ort = "DD"
        print("Başarı harf notunuz: {}".format(ort))
    else:
        print("Dersin sorumlusu olduğu hocanız ile görüşün")
