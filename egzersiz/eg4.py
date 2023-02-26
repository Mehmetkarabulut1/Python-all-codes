print("""
ikinci dereceden kök bulma programına hoşgeldiniz
ax^2 + bx + c formatında istenen a, b ve c değerleri giriniz !
""")

a = input("a değerini girniz: ")
while True:
    try:
        n0 = int(a)
    except:
        print("geçersiz değer...")
        a = input("lütfen a değerinin sayı olduğunu kontrol edip tekrar giriniz! : ")
        continue
    break

b = input("b değerini girniz: ")
while True:
    try:
        n1 = int(b)
    except:
        print("geçersiz değer...")
        b = input("lütfen b değerinin sayı olduğunu kontrol edip tekrar giriniz! : ")
        continue
    break

c = input("c değerini girniz: ")
while True:
    try:
        n2 = int(c)
    except:
        print("geçersiz değer...")
        c = input("lütfen c değerinin sayı olduğunu kontrol edip tekrar giriniz! : ")
        continue
    break


"""
while True:
    a = input("a değerini girniz: ")
    b = input("b değerini girniz: ")
    c = input("c değerini girniz: ")
    try:
        n0 = int(a)
        n1 = int(b)
        n2 = int(c)
    except ValueError:
        print("geçersiz değer ya da değerler girdiniz... lütfen sayı girdiğinize emin olun")
        continue
    break
"""

di = n1**2 - 4*n0*n2
print("diskriminant değeri {}" .format(di))
x1 = (-n1 + (di ** (1 / 2))) / (2 * n0)
x2 = (-n1 - (di ** (1 / 2))) / (2 * n0)
if di > 0:
    print("denklemin reel kökü vardır!")
    print("kök 1: {} , kök 2: {}" .format(x1 , x2))
elif di == 0:
    print("denklemin çakışık bir reel kökü vardır! ")
    print("kök: {} " .format(x1))
else:
    print("denklemin reel kökü yoktur!")
    #print("kök 1: {} , kök 2: {}" .format(x1 , x2))