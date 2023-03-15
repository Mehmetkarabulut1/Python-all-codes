
a = input("""write the decimal part of the number in the next input...
                        please enter your binary number:  """)
decimal = input("""if you don't have decimal number, write pass...
                        please enter your decimal part of number: """)

b = len(a)
c = len(decimal)
toplam = 0

for i in a:
    if i == "1":
        b = b - 1
        i = int(i)
        sonuc = i * (2 ** b)
        toplam += sonuc
    else:
        b = b-1

y = -1
for x in decimal:
    if x == "1":
        x = int(x)
        sonu = x * (2**y)
        y = y-1
        toplam += sonu
    elif decimal == "pass":
        pass
    else:
        y = y-1

print("your number converted to decimal format =" , toplam)
