import sys

class Irasas():
    def __init__(self):
        self.pajamos = 0
        self.islaidos = 0
        self.islaidu_sarasas = []
        self.islaidu_pav = []
        self.pajamu_sarasas = []
        self.pajamu_pav = []
        self.greitos_pajamos()
        self.greitos_islaidos()

    def prasyti_pajamu(self):
        prideti_pajamas = input("Irasyti pajamas? [y/n]: ")
        return prideti_pajamas

    def pajamu_sum(self):
        self.pajamos = sum(self.pajamu_sarasas)

    def prasyti_islaidu(self):
        prideti_islaidas = input("Irasyti islaidas? [y/n]: ")
        return prideti_islaidas

    def islaidu_sum(self):
        self.islaidos = sum(self.islaidu_sarasas)

    def pajamu_tikrinimas(self):
        if not self.pajamu_sarasas:
            print("Iveskite pajamas [tik skaiciai].")
            self.greitos_pajamos()
        else:
            return

    def islaidu_tikrinimas(self):
        if not self.islaidu_sarasas:
            print("Iveskite islaidas [tik skaiciai].")
            self.greitos_islaidos()
        else:
            return

    def greitos_pajamos(self):
        x = False
        while not x:
            rezultatas = self.prasyti_pajamu()
            if rezultatas == 'y':
                ivesti_pajamas = int(input("Gaunamos pajamos. [tik skaiciai]: "))
                self.pajamu_sarasas.append(ivesti_pajamas)
                pajamu_vardas = input("Kokio tipo pajamos. [Tik raides]: ")
                self.pajamu_pav.append(pajamu_vardas)
            else:
                self.pajamu_tikrinimas()
                x = True
        self.pajamu_sum()
        pav = [pav for pav in self.pajamu_pav]
        pajamos = [pajamos for pajamos in self.pajamu_sarasas]
        pajamu_ataskaita = dict(zip(pav, pajamos))
        for k in pajamu_ataskaita:
            print(k + ': ', 'Eur' + str(pajamu_ataskaita[k]))
        print("Visos pajamos: ", 'Eur' + str(self.pajamos))
        self.greitos_islaidos()

    def greitos_islaidos(self):
        x = False
        while not x:
            rezultatas = self.prasyti_islaidu()
            if rezultatas == 'y':
                ivesti_islaidas = int(input("Islaidu dydis. [tik skaiciai]: "))
                self.islaidu_sarasas.append(ivesti_islaidas)
                islaidu_vardas = input("Kokio tipo islaidos. [Tik raides]: ")
                self.islaidu_pav.append(islaidu_vardas)
            else:
                self.islaidu_tikrinimas()
                x = True
        self.islaidu_sum()
        pav = [pav for pav in self.islaidu_pav]
        islaidos = [islaidos for islaidos in self.islaidu_sarasas]
        islaidu_ataskaita = dict(zip(pav, islaidos))
        for k in islaidu_ataskaita:
            print(k + ': ', 'Eur' + str(islaidu_ataskaita[k]))
        print("Visos islaidos: ", 'Eur' + str(self.islaidos))
        self.isjungti_programa()

    def isjungti_programa(self):
        print("Viso Gero!")
        sys.exit(0)

Irasas()