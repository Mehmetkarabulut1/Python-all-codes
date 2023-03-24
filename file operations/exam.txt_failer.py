kalanlar_liste = []
geçenler_liste = []

def kalanlar(kalan):
    kalan = kalan[:-1]
    liste = kalan.split(",")
    if liste[2] == "FF":
        kalanlar_liste.append(kalan + "\n")
    elif liste[2] =="":
        kalanlar_liste.append(kalan + "\n")

    return kalanlar_liste

def geçenler(geçen):
    geçen = geçen[:-1]
    liste = geçen.split(",")
    if liste[2] != "FF":
        geçenler_liste.append(geçen + "\n")
    return geçenler_liste

def succsess(element):
    element = element.strip()
    liste = element.split(",")
    student_name = str(liste[0])
    midterm_1 = int(liste[1])
    midterm_2 = int(liste[2])
    final = int(liste[3])


    midterm_ratio = 0.4
    final_ratio = 0.6


    average = ((((midterm_1 + midterm_2)/2) * midterm_ratio) + (final * final_ratio))
    ort = ""
    if average < 60:
        ort = "FF"
    elif average > 90 and average <= 100:
        ort = "AA"
    elif average > 85 and average <= 90:
        ort = "BA"
    elif average > 80 and average <= 85:
        ort = "BB"
    elif average > 75 and average <= 80:
        ort = "CB"
    elif average > 70 and average <= 75:
        ort = "CC"
    elif average > 65 and average <= 70:
        ort = "DC"
    elif average >= 60 and average <= 65:
        ort = "DD"
    else:
        print(element,
                    """
                    Hay Aksi! Bir sorunla karşılaştık.
                    Lütfen ders sorumlusu ile görüşünüz
                    """)

    return student_name +  ",------------------->," + ort + "\n"




with open("score.txt" , "r+" , encoding="utf-8") as scores:
    append_list = list()
    for i in scores:
        succsess(i)
        append_list.append((succsess(i)))


with open("last_success_file.txt" , "r+" ,encoding= "utf-8") as last:
    for i in append_list:
        last.write(i)

with open( "last_success_file.txt", encoding = "utf-") as kal:
    for i in kal:
        kalanlar(i)
        geçenler(i)

with open("geçenler.txt", "r+", encoding="utf_8") as file:
    for i in geçenler_liste:
        file.write(i)

with open("failer.txt" , "r+" , encoding = "utf-8") as fail:
    for i in kalanlar_liste:
        fail.write(i)