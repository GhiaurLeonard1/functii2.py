class ContBancar:
    #constructor
    def __init__(self, titularCont, iban):

        #atribute
        self.titularCont = titularCont
        self.iban = iban
        self.sold = 0
        self.activ = False
        self.pin = 7777
        self.incercari_activare = 0

        #metode
    def interogareSold(self):
        print(f"Titular {self.titularCont}")
        print(f"IBAN {self.iban}")
        print(f"Sold {self.sold}")
        print(f"Activ {self.activ}")
        print(f"Nr. de incercari {self.incercari_activare}")
        print("-------------------------------------------")

    def activareCont(self, pin_utilizator):
        self.salut()
        if pin_utilizator == self.pin:
            print("Card activat")
            self.activ = True
        else:
            print("Pin gresit!")
            self.incercari_activare = self.incercari_activare + 1
           # self.incercari_activare+=1

    def alimentareCont(self, suma_depusa):
        self.salut()
        self.sold += suma_depusa # se ia suma si se adauga la sold
        print(f"Ati alimentat {suma_depusa}")
        print(f"Aveti in cont{self.sold}")

    def plataCard(self, suma_cheltuita):
        self.salut()
        if suma_cheltuita <= self.sold:
            self.sold -= suma_cheltuita
            print(f"Ati cheltuit{suma_cheltuita}")
            print(f"Aveti in cont {self.sold}")
        else:
            print("Fonduri insuficiente!")




    def salut(self):
        print(f"Buna {self.titularCont}")