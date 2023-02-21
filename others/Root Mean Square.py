"""Bir dizi alarak bu sayıların RMS (Root Mean Square) bulan kodu yazınız.
RMS: Bilgisayar bilimlerinde çeşitli istatistik ve hesaplama alanlarında kullanılan bir formüldür.
Basitçe üç aşamadan oluşur: Değerlerin karelerini al (square) ,
kareleri alınan bu değerlerin ortalamasını al (mean) , bu ortalama değerinin karekökünü al (root)
"""
liste =list(range(0,15))
liste_karesi = []
c= 0
for i in liste:
    a = i ** 2
    c += (i ** 2)
    liste_karesi.append(a)
    print(liste_karesi)

ortalama = c / liste[-1]
print(ortalama)
ortalama_karakoku = ortalama ** 0.5
print(ortalama_karakoku)