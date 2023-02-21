while True:
    b = int(input("sayının kaç basamaklı olduğunu girinz"))
    a = input("lütfen sayı giriniz")
    if a == "q":
        print("çıkış")
    if b == 3:
        if int(a[0]) ** b + int(a[1]) ** b + int(a[2]) ** b == int(a):
            print("bu sayı armstrong sayıdır")
            continue
    elif b == 4:
        if int(a[0]) ** b + int(a[1]) ** b + int(a[2]) ** b + int(a[3])**b == int(a):
            print("bu sayı armstrong sayıdır")
            continue