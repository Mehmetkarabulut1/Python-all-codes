sayılar = []

c =  input("adet giriniz: ")
try:
    n1 = int(c)
except:
    print("geçersiz değer...")
    while c!= int():
        c = input("adet giriniz: ")
        try:
            n1 = int(c)
        except:
            print("geçersiz değer...")
            continue
        break


c = int(c)
while  c != 0 and c > 0 :
    sayılar.append(input("numara giriniz:"))
    c = c-1
    if c == 0:
        break


b = int(input("girilen sayıları büyükten küçüğe sıralanacaktır eğer küçükten büyüğe istiyorsanız 0'a basın..."))
if b == 0:
    sayılar.sort(reverse=False)
    print("girilen sayılar küçükten büyüğüe:", sayılar)

elif b > 0:
        sayılar.sort(reverse=True)
        print("girilen sayılar büyükten küçüğe:" , sayılar)