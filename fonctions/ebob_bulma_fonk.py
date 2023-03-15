def ebob(sayı, sayı1):
    liste = []
    ebobu = 1
    for i in range(1,sayı+1):
        if sayı % i == 0 and sayı2 % i == 0:
            liste.append(i)
            liste.sort(reverse=True)
            ebobu = liste[0]
    return ebobu


while True:
    sayı = input("sayı:")
    sayı2 = input("sayı2:")

    if sayı == "q":
        print("çıkış yapılıyor")
        break
    else:
        sayı = int(sayı)
        sayı2 = int(sayı2)
        print("ebobu",ebob(sayı,sayı2))