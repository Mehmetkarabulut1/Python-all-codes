b = 0
a = list()
c = int()

while (b < 10):
    print("listeniz boş ", a)
    c = (input("lütfen sayı giriniz = "))
    print("eklediğiniz sayı : {}".format(c))
    a.append(c)
    a.sort(reverse=True)
    print(a)
    b += 1