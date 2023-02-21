def ekok(sayı,sayı2):
    ekok = 0
    for i in range(1,sayı):
        for j in range(1,sayı2):
            if sayı*i == sayı2*j:
                ekok =sayı*i
                return ekok
while True:
    sayı = input("sayı:")
    sayı2 = input("sayı2:")

    if sayı == "q":
        print("çıkış yapılıyor")
        break
    else:
        sayı = int(sayı)
        sayı2 = int(sayı2)
        print("ekok",ekok(sayı,sayı2))