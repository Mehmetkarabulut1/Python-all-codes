while True:
    a =  float(input("lütfen dik kenarlardan birini giriniz "))
    b = float(input("lütfen dik kenarlardan diğerini giriniz "))
    hipatenüs = (a**2 + b**2 )  ** (1/2)
    if (a + b) > hipatenüs > abs(a - b) and (a + hipatenüs) > b > abs(a - hipatenüs) and (b + hipatenüs) > a > abs(b - hipatenüs):
        print("üçgen belirtiyor")
        print("hipatenüs =  {}".format(hipatenüs))
        continue
    else:
        print("üçgen belirtmiyor")