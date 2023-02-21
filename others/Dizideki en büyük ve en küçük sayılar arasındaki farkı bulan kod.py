"""import random
liste = list(range(0,random.randint(1,100)))
liste.sort()
print(liste[-1])
print(liste[0])
print(liste[-1]-liste[0])
"""

sayılar = input("sayı:")
liste1 = sayılar.split(",")
x = 0
for i in liste1:
    x += int(i)
print(x/len(liste1))