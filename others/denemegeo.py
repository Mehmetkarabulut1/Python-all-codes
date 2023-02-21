""" while ya da for dögüsü ile
[1, 2, 3, 4]
[2, 3, 4, 5]
[3, 4, 5, 6]
[4, 5, 6, 7]
çıktısını almaya çalışmak"""

i = 3
z = 0
l = list(range(0,4))
while True:
    i += 1
    l.append(i)
    l.pop(z)
    print(l)
    if i == 8:
        break

"------------------------------------------------"

x = 3
l2 = [0,1,2,3,]
for i in range(4,8):
    l2.append(i)
    l2.pop(0)
    print(l2)