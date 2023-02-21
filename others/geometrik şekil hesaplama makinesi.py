print("""*********************************************
Geometril şekil hesaplama makinesine hoşgeldiniz

lütfen hangi şekille işlem yapacağınız seçin;

1. üçgen
2. dörtgen 

*********************************************
""")
while True:
    sekil =int(input("şekil seçiniz:"))
    if sekil == 1:
        a = float(input("lütfen 1. kenarı giriniz"))
        b = float(input("lütfen 2. kenarı giriniz"))
        c = float(input("lütfen 3. kenarı giriniz"))
        if (a+b) >c >abs(a-b) and (a+c) > b > abs(a-c) and (b+c) > a > abs(b-c):

            if a == b and a == c:
                print("eşkenar üçgen")

            elif a == b and b!= c:
                print("ikizkenar")

            elif b == c and c!= a:
                print("ikizkenar")

            elif b == c and c!= a:
                print("ikizkenar")

            elif a == c and c!= b:
                print("ikizkenar")

            else:
                print("çeşitkenar üçgen")

        else:
            print("üçgen belirtmiyor")

    elif sekil == 2:
        a1 = float(input("lütfen 1. kenarı giriniz"))
        a2 = float(input("lütfen 1. kenarı giriniz"))
        a3 = float(input("lütfen 1. kenarı giriniz"))
        a4 = float(input("lütfen 1. kenarı giriniz"))

        if a1 == a2 == a3 == a4:
            print("kare")

        elif a1 == a2 != a3 == a4 or a1 == a3 != a2 == a4 or a1 == a4 != a2 == a3:
            print("dikdörtgen")

        elif a1 != a2 != a3 != a4:
            print("yamuk")