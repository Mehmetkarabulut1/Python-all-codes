liste = []
def tam_bölen(sayı):
    for i in range(1,sayı+1):
        if sayı % i == 0:
            liste.append(i)
    return liste

while True:
    sayı = input("sayı:")

    if sayı == "q":
        print("çıkış yapılıyor")
    else:
        sayı = int(sayı)
        print("tam bölenler:", tam_bölen(sayı))

