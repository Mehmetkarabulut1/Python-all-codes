a = float(input("sayı1"))
b = float(input("say2"))
c = float(input("say3"))

if a>b and a>c:
    print("enbüyük sayı : {}".format(a))
elif b>a and b>c:
    print("en büyük sayı :{}".format(b))
elif c>a and c>b:
    print("en büyük sayı :{}".format(c))
