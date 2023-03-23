class files():
    def __init__(self):
        with open("text.txt","r",encoding="utf-8") as file:
            content_of_file = file.read()
            words = content_of_file.split()
            self.list_of_words = list()
            for i in words:
                i.strip("\n")
                i.rstrip(".")
                i.rstrip(",")
                self.list_of_words.append(i)

    def all_words(self):
        self.set_of_words = set()
        for i in self.list_of_words:
            self.set_of_words.add(i)
            print(i)
            print("---------------")

    def frequency_of_word(self):
        self.dictionary = {}
        for i in self.list_of_words:
            if i in self.dictionary:
                self.dictionary[i] += 1
            else:
                self.dictionary[i] = 1
        for i,j in self.dictionary.items():
            print(i,"kelimesi",j ,"defa geçiyor")
            print("------------------")
        return self.dictionary

    def finder(self):
        self.dictionary = {}
        for i in self.list_of_words:
            if i in self.dictionary:
                self.dictionary[i] += 1
            else:
                self.dictionary[i] = 1
        the_word = input("please enter your word")
        for  i,j in self.dictionary.items():
            if i == the_word:
                print(i ,"kelimesi",j,"defa metinde geçiyor")

exp = files()
exp.finder()