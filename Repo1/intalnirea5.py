# O functie(def) -este un grup de declaratii care exista intr-un program pentru a realiza o anumita sarcina.
#definirea unei functii se face cu "def"
import math

# def mesaj():#functia mesaj contine in bloc doua declaratii
#     print("Sunt Leo")
#     print("si incerc sa invat Python")
#
# print(mesaj())

#demonstram ca doua functii au variabile locale cu acelasi nume
# def main():
#     dolj()#daca numele este subliniat cu rosu inseamna ca nu a fost apelat
#     gorj()
# def dolj():
#     pasari = 5000
#     print("Doljul are", pasari, "de pasari")
# def gorj():
#     pasari = 8000
#     print("Gorjul are", pasari, "de pasari")
#
# print(main())#apelam functia principala

#Un argument este o portiune de date care este trecuta intr-o functie atunci cand functia este invocata

#Un parametru este o variabila care primeste un argument ce este trecut intr-o functie

# def dublul(numar): #numar este parametru
#     numar = 6
#     rezultat = numar*2
#     print(rezultat)
#
# dublul(6)

# def main():
#     valoare =5#argument
#     arata_dublul(valoare)
#
# def arata_dublul(numar):#functia accepta argumentul si afiseaza valoarea lui dubla
#     rezultat= numar*2
#     print(rezultat)
#
# main()

# #trecerea intr-o functie a mai multor argumente
# def main():
#     print("Suma lui 12 cu 45 este:")
#     arata_suma(12, 45)
#     print("Suma lui 4 cu 6 este:")
#     arata_suma(4, 6)
#
# def arata_suma(num1,num2):
#     rezultat = num1+num2
#     print(rezultat)
#
# main()#

# #schimbarea parametrilor
# def main():
#     valoare = 99
#     print("Valoarea este:", valoare)
#
# def schimba_valoarea(arg):
#     print("Voi schimba valoarea.")
#     arg = 0
#     print("Acuma valoarea este", arg)
#
# main()
# schimba_valoarea(1)

# #constanta globala
# PI = 3.14
# def aria_cercului(raza):
#     return PI*raza*raza
#
# def circumf_cerc(raza):
#     return 2*PI*raza
# print("Cercul cu raza 5 are suprafata:", aria_cercului(5))#Cercul cu raza 5 are suprafata: 78.5
# # print("Circumferinta aceluiasi cerc este:", circumf_cerc(5))#Circumferinta aceluiasi cerc este: 31.400000000000002
# print("Circumferinta este:", format(31.400000000000002, ".2f"))

# #Program ce transforma gradele Celsius in Farenhait
# temp = 0
# while temp != -50:
#     temp = eval(input("Introdu temperatura in F(-50 ca sa iesiti):"))
#     print("Temperatura in C este:", format(5/9*(temp-32), ",.2f"))


# x= 0
# numar= 3
# # while numar < 10:
# #     print(numar)#afiseaza la infinit numar
# #     break #opreste dupa prima verificare
# while x<10 and numar>0:# 0-iesi din while
#     numar = int(input("Introdu un numar:"))

# #Bucla for itereaza de un numar specific de ori
# def main():
#     print("Voi afisa numerele de la 1 la 5")
#     for num in [1, 2, 3, 4, 5]:#pentru fiecare numar din [1,2,3,4,5]
#         print(num)# afisez numar
#
# main()

# #acest program demonstreaza cum functia range poate fi folosita cu bucla for
# def main():
#     for x in range(5):#afiseaza un mesaj de 5 ori
#         print("Ce\n \tfaci \n \t \t Leo?")
# main()
#

#def print_hi( nume,prenume ):
#     if nume == "Test" and prenume == "None":
#         return "Bravo"
#
#
# #     print(f"Salut  {prenume} {nume.upper()}")
# print(print_hi("Test", "None"))


# def nr_nat(numar):
#     if numar>=0:
#         return "numar natural"
#     else:
#         return "Numar nenatural"
#
#
# rasp= nr_nat(-4)
# print(rasp)

# # calculam impozitul pe masina
# cc = int(input("Introduceti capacitatea cilindrica"))
# impozit = None


# def calcul_impozit(hibrid_input, cc_input):
#     if hibrid_input:
#         return 10
#     if cc_input < 1200:
#         return 75
#     if cc_input > 1200 and cc_input<1600:
#         return 125
#     if cc_input>1600 and cc_input<2000:
#         return 200
#     else:
#         return 500
#
#
# impozit = calcul_impozit(False,cc)
# print(impozit)
# impozit = calcul_impozit(True,500)
# print(impozit)
# impozit = calcul_impozit(False,1599)
# print(impozit)
# impozit = calcul_impozit(False,1601)
# print(impozit)

# #cand am mai putin de 15% benzina in rezervor sa imi afiseze Warning!
# REZERVOR= 50
# benz = float(input("Introduceti benzina ramasa"))
# benz_ramasa = None
#
#
# def benzina_ramasa(benzina_input):
#     procentaj_benzina = benzina_input/REZERVOR*100
#     if procentaj_benzina<=15:
#         print("Warning!!!")
#     elif procentaj_benzina >100:
#         print(f"Nu poti avea mai multi litri de {REZERVOR}")
#     else:
#         print("Mai aveti destula benzina!")
#         return procentaj_benzina
#
#
# benz_ramasa = benzina_ramasa(benz)
# print(f"Mai ai {benz_ramasa}% benzina ramasa")

#                                                               cum folosesc functii din alte fisiere

# from helper import suma
# from helper import produs
#
#
# print(suma(4,7))
# print(produs(3,5,10))
#
#Acest program calculeaza  suma unei serii de numere introduse de user la constanta pentru numarul maxim
# MAX = 5# numarul maxim de numere care sa le calculeze
# def main():
#     #instaleaza varibila acumulator
#     total = 0.0# acumulatorul se initiaza intotdeauna cu 0.0(counter)
#     print("Acest program calculeaza suma a ")
#     print(MAX, "numere introduse.")
#     #ia numerele si calculeaza-le
#     for counter in range(MAX):
#         number =int(input("Introdu un input:"))
#         total= total+number
#     #afiseaza calculul numerelor
#     print("Totalul este:", total)
# main()

# def sum(num1, num2):
#     result = num1 + num2
#     return result
#
# print(sum(2,5))

suprafata = math.pi*radius**2
