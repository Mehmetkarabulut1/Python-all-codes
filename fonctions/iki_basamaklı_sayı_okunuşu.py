birler = ["","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]
onlar = ["","on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]
def okuma(sayı):
    birinci = sayı % 10
    ikinci = sayı // 10
    return onlar[ikinci] +" " + birler[birinci]

while True:
    sayı = input("sayı giriniz:")
    if sayı =="q":
        break
    else:
        sayı = int(sayı)
        if (okuma(sayı)):
            print("okunuş:" , okuma(sayı))
        else:
            sayı = int(sayı)
            print("değil")