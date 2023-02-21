i = 0
while i < 101:
    if i%3 == 0:
        print(i)
    i += 1

for i in range(0,101):
    if i%3 == 0:
        print(i)

for i in range(0,101):
    if i%3 != 0:
        continue
    print(i)