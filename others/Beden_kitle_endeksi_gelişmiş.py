boy = float(input("Lütfen boyunuzu giriiz"))
kilo = float(input("Lütfen kilonuzu giriiz"))

bke = kilo / (boy * boy)
print(bke)

if bke < 18.5:
    print("zayıfsınız")
elif bke <= 25 and bke > 18.5:
    print("Normal endeks")
elif bke > 25 and bke < 30:
    print("fazla kilolu")
else:
    print("obez")