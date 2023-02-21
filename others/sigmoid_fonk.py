"""
Verilen bir sayının sigmoid fonksiyonunu veren kodu yazınız. Sigmoid fonksiyonu (Sigmoid function)
 basitçe f(x) = 1 / (1+e-x ) olarak yazılabilir. Sigmoid
fonkisyonunun ismi de fonksiyonun kartezyen uzayda
çizilmiş halinin andırdığı S harfinden (sigma) gelmektedir.
"""
sonuc = 0
e =  2.71828
e = float()
def fonk():
    x = int(input("sayı:"))
    sonuc = 1 / (1+e-x)
    print(sonuc)

fonk()