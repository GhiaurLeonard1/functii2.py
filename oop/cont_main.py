from oop.cont_bancar import ContBancar

cont1 = ContBancar("Leo G.", "RO0001")
cont2 = ContBancar("Teo V.", "RO0002")

cont1.activareCont(7777)
cont2.activareCont(3333)
cont2.activareCont(7777)

cont1.alimentareCont(300)
cont2.alimentareCont(700)
cont2.alimentareCont(300)

cont1.plataCard(500)
cont1.plataCard(300)
cont2.plataCard(100)
cont2.plataCard(200)

cont1.interogareSold()
cont2.interogareSold()



#tema clasa Angajat
#nume, prenume, salariu,vechime, functie
#constructor:nume, prenume, salariu,vechime, functie
# metode
# descriere
# marire salariu in functie de vechime
# actualizare vechime(parametrul noua vechime)...(self.vechime= noua vechime)
# daca are vechime sub 5 ani marim 300 lei, peste 5 ani 500 lei
