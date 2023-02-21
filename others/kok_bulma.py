print("lütfen verilen değerleri aşşağıya giriniz ")
a = input("lütfen xkarenin kat sayısını giriniz : ")
b = input("Lütfen xin kat sayısını giriniz : ")
c = input("lütfen sabit sayıyı giriniz : ")

"""
burada şu şekilde de bir kodalama yapılabilridi intleri sonra atamak yerine
intleri inputla birlikte alabilirdik

örneğin;
a = int(input("denklemin xkareli katsayısını giriniz : "))

"""

delta = int(b)**2 - 4*int(a)*int(c)
print("delta değeri = : {}".format(delta))

a = int()
b = int()
c= int()

x1 = (- b - delta ** 0.5) / (2*a)
x2 = (- b + delta ** 0.5) / (2*a)

print("Denklemin birinci kökü = : {}\nDenklemin ikinci kökü = : {}\n".format(x1,x2))