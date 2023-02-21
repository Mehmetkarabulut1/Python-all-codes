print("belirtilen değerleri giriniz : ")
a = int(input("denklemin xkareli değerini giriniz"))
b = int(input("denklemin xli katsayısını giriniz"))
c = int(input("denklemin sabit sayısınını giriniz"))

D = b ** 2 - 4 * a * c
print("Delta değeri = {}" .format(D))
x1 = (-b-D ** 0.5) / (2*a)
x2 = (-b+D ** 0.5) / (2*a)
print("Denklemin birinci kökü = : {}\nDenklemin ikinci kökü = :{}\n".format(x1,x2))
