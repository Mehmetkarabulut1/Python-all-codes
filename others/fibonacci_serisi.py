a = 1
b= 1
fiban = [a,b]
for i in range(20):
     a, b = b, a + b
     fiban.append(b)
print(fiban)
