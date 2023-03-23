#question 1
word = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
word = word.lower()
list_of_letter = list()
for i in word:
    list_of_letter.append(i)

dictionary = {}
for  i in list_of_letter:
    if i in dictionary:
        dictionary[i] += 1
    else:
        dictionary[i] = 1
liste =[]
for i,j in dictionary.items():
    print(i,j)
    
    

#question 2
with open("poem.txt","r",encoding="utf-8") as file:
    secret = str()
    for i in file:
        word = i.strip()
        secret += word[0]
    print(secret)



#question3
with open("mails.txt","r",encoding="utf-8") as file:
    list_of_gamils = []
    for i in file:
        word = i.strip()
        x = word.endswith("gmail.com")
        if x == True:
            list_of_gamils.append(word)
    print(list_of_gamils)



#question4
list1 = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
list2 = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]
for i,j in zip(list1,list2):
    print(i,j)