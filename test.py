"""try:
    print(x)
except NameError:
    print("code is working in except block")

liste = ["mf45","mk","54km"]

try:
    x = "mehmet"
    print(x)
except:
    print("ups!! this code doesnt work")
else:
    print("we dont have any problem")"""

liste = ["345","mehmet","45as"]
for i in liste:
    if i != int(i):
        raise TypeError("int veri tipinde değil")

"""for i in liste:
    try:
        i == int(i)
        print(i)

    except:
        print(i,", sring veri tipi içeriyor")
        pass
    """


