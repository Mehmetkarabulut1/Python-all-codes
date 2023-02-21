class ayazaga():
    def __init__(self,maden_fakültesi = ["petrol"] , fen_edebiyat = []):
        self.maden_fakültesi = maden_fakültesi
        self.fen_edebiyat = fen_edebiyat

    def maden_bölümekle(self,bölüm_adı):
        self.maden_fakültesi.append(bölüm_adı)
        print(self.maden_fakültesi)

    def __str__(self):
        return (self.maden_fakültesi,self.fen_edebiyat)

class okul(ayazaga):
    def __init__(self,maden_fakültesi = [],fen_edebiyat = [],mimarlık = [],makina = []):
        super().__init__(maden_fakültesi,fen_edebiyat,)
        self.mimarlık = mimarlık
        self.makina = makina

    def okul_dışı(self):
        return "okulun dışındaki bölümler: {} {}".format(self.maden_fakültesi,self.mimarlık)

    def __str__(self):
        return (self.maden_fakültesi)

