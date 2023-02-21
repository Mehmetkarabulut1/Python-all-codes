def fib():
    a = 0
    b = 1
    list_fib = []
    buraya_kadar = int(input("sayı giriniz:"))
    for i in range(0,buraya_kadar):
        a , b = b ,a+b
        list_fib.append(a)
    print(list_fib)
