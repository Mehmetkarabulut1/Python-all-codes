print("""**************************************

faktöriyel hesap makinesine hoşgeldiniz

**************************************""")

while True:
    a = (input("lütfen sayı giriniz:"))
    if a == "q":
        print("çıkış yapılıyor")
        break
    else:
        a = int(a)
        faktoriyel = 1
    print("girdiğiniz sayı: " , a)

    for i in range(2 , a+1):
        faktoriyel *= i
    print("işlemin sonucu" , faktoriyel)

