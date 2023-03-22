with open("score.txt" , "a" , encoding = "utf-8") as ScoreFile:
    pass
def succses():
    student_name = str(lines[::])
    midterm_1 = str(lines[1::])
    midterm_2 = str(lines[2::])
    final = str(lines[3::])
    while True:
        midterm_ratio = float(input("please enter your ratio of midterm"))
        final_ratio = float(input("please enter your final ratio"))
        if midterm_ratio + final_ratio == 1:
            break
        else:
            print("please check again your raitos")
            continue

        average = ((midterm_1 + midtrem_2)/2) * midterm_ratio + final * final_ratio

        average = ortalama
        ort = "boş"
        if average < 60:
            ort = "FF"
            print("Başarı harf notunuz: {}".format(ort))
            print(ort)
        elif ortalama >= 90 and ortalama <= 100:
            ort = "AA"
            print("Başarı harf notunuz: {}".format(ort))
        elif ortalama >= 85 and ortalama <= 100:
            ort = "BA"
            print("Başarı harf notunuz: {}".format(ort))
        elif ortalama >= 80 and ortalama <= 100:
            ort = "BB"
            print("Başarı harf notunuz: {}".format(ort))
        elif ortalama >= 75 and ortalama <= 100:
            ort = "CB"
            print("Başarı harf notunuz: {}".format(ort))
        elif ortalama >= 70 and ortalama <= 100:
            ort = "CC"
            print("Başarı harf notunuz: {}".format(ort))
        elif ortalama >= 65 and ortalama <= 100:
            ort = "DC"
            print("Başarı harf notunuz: {}".format(ort))
        elif ortalama >= 60 and ortalama <= 100:
            ort = "DD"
            print("Başarı harf notunuz: {}".format(ort))
        else:
            print(
                """
                Hay Aksi! Bir sorunla karşılaştık.
                Lütfen ders sorumlusu ile görüşünüz
                """
            )
    with open("last_success_file.txt" , "a" , encoding = "utf-8") as last:
        last.write(student_name + midterm_1 + midterm_2 + final )





with open("score.txt" , "r+" , encoding = "utf-8") as ScoreFile:
    lines = ScoreFile.readlines()
    succses()


