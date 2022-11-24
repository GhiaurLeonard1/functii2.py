#### ZeroDivisionError: division by zero
# print ("Inainte de diviziune")
#
#
# x= 10
# rez = x/0
# print(rez)(Nu are sens impartirea la 0
#
# print("Dupa diviziune")

# ####IndexError: list index out of range    Bloc try-except ne ajuta sa trecem peste o eroare si codul sa ruleze pana la capat.
# print ("Inainte de diviziune")
#
# try:
#     list= [1,2,3]
#     list[6]
# except IndexError as e:
#     print(e)
# print("Dupa diviziune")


# ####NameError: name 'lista' is not defined. Did you mean: 'list'?
# print ("Inainte de diviziune")
#
#
# list= [1,2,3]
# lista[6]  #list
#
# print("Dupa diviziune")

# #####TypeError: len() takes exactly one argument (4 given)
# print(len("test"))
#
# print(len(1,2,3,10))#trebuie adaugate paranteze patrate la numere len([1,2,3,10])



# #####NameError: name 'a' is not defined
# print("Inainte de diviziune")
#
#
# list= [a,2,dbr]     # contine numai cifre
# list[6]
#
# print("Dupa diviziune")
#


######SyntaxError: default 'except:' must be last
# try:
#     print(x)
# except:     #acest except se pune ultimul
#     print("Ceva nu e bine")
# except TypeError:   #in schimb putem scrie nenumarate comenzi de "except Type..."
#     print("Eroare tip")



#### Folosim aceasta verificare sa demonstram ca ceva nu este in pagina
# x="Hello"
#
# if not type(x) is int:        #daca tipul lui x nu este int
#     raise TypeError("Folositi doar tipul int")        #ne va aparea descrierea din paranteze pentru eroare


# ######Aici afisam folosind blocul try-except diferite mesaje
# try:
#     print(x)# nu am definit x-ul
# except TypeError:   #intra aici daca Este Type Error
#     print("Nu e bine")
# except :            #altfel celelalte erori afiseaza printul de aici
#     print("Eroare tip")


# #Try-except-Finally afiseaza printul de la try si printul de la finally
# try:# incearca sa rulezi
#     x ="salut"# daca comentam aceasta linie afiseaza mesajul de la except si cel de la finally
#     print(x)
# except :
#     print("Gresit")
# finally:
#     print("Am ajuns la final")




#INHERITANCE= MOSTENIRE

# class Chef:# toti studentii
#
#     def name_salad(self):
#         print("Pot sa gatesc salata")
#
#     def make_soup(self):
#         print("Pot sa gatesc supa")
#
# class ChefJaponez(Chef):    #mostenim din clasa Chef
#
#     def make_sushi(self):
#         print("Pot sa gatesc sushi")
#
# class ChefItalian(Chef):    #clasele copil nu pot mosteni de la celelalte clase copil
#
#     def make_pizza(self):
#         print("Pot sa fac pizza")
#
# std_jap = ChefJaponez()
# std_jap.name_salad()
# std_jap.make_soup()
# std_jap.make_sushi()
#
# std_ita = ChefItalian()
# std_ita.name_salad()
# std_ita.make_soup()
# std_ita.make_pizza()


#POLIMORPHISMUL -cand 2 sau mai multe functii au acelasi nume dar comportament diferit

#
# print(len("teajast"))#lungimea unui sir
#
#
# print(len([1, 2, 3, 10, 20, 30]))# Lungimea unei liste

#
# def adunare(x=1, y=0, z=0):# atribui valori aparente pentru x,y,z
#
#     print(x)
#     print(y)
#     print(z)
#
#     return x+y+z
#
#
# print("Prima adunare", adunare(2, 3))# preia numai valoarea x si y
#
# print("A doua adunare", adunare(2, 3, 4))#preia toate valorile
#
# print("A treia adunare", adunare(5))# preia numai valoarea lui x


#
# class Romania():
#     def language(self):
#         print("Romaneste")
#
#
# class Italia():
#     def language(self):
#         print("Italiana")
#
#
# class Brazilia():
#     def language(self):
#         print("Portugheza")
#
#
# x_ro = Romania()
# x_it = Italia()
# x_br = Brazilia()
#
# for tara in (x_ro, x_it, x_br):
#     tara.language()#parcurge toate atributele in functie de ordinera din paranteza de mai sus


#####Exemplu de polimorphism + inheritance

#
# class Pasari:
#
#     def descriere(self):
#         print("Exista mai multe specii de pasari")
#
#
#     def zboara(self):
#         print("Majoritatea pasarilor pot sa zboare")
#
# class Vultur(Pasari):
#
#     # def descriere(self):
#     #     print("Vulturii sunt pasari rapitoare")
#
#
#     def zboara(self):
#         print("Vulturii pot Zbura")
#
# class Pinguin(Pasari):
#
#     # def descriere(self):
#     #     print("Pinguinii locuiesc la polul sud")
#     #
#
#     def zboara(self):
#         print("Pinguinii nu pot sa zboare")
#
# x_pasari = Pasari()
# x_vulturi= Vultur()
# x_pinguin = Pinguin()
#
# x_pasari.descriere()
# x_pasari.zboara()
# print(" ")
# x_vulturi.descriere()
# x_vulturi.zboara()
# print(" ")
# x_pinguin.descriere()
# x_pinguin.zboara()
# print(" ")
#

###### ABSTRACTION
from abc import ABC, abstractmethod

# class Animal(ABC):
#
#     def sound(self):
#         raise NotImplementedError
#
#     def sleep(self):
#         raise NotImplementedError
#
# class Dog(Animal):
#     def sound(self):
#         print("Ham Ham")
#
#     def sleep(self):
#         print("ZZZZZZZZ")
#
# class Cat(Animal):
#
#     def sound(self):
#         print("Miawww Miaww")
#
#     def sleep(self):
#         print("prrrr")

#
# from abc import ABC, abstractmethod
#
# class Poligon(ABC): #Interfata
#
#     @abstractmethod
#     def nr_de_laturi(self):# aceste functii pot fi folosite de celelalte clase
#         pass
#
#     @abstractmethod
#     def perimetru(self):# aceste functii pot fi folosite de celelalte clase
#         pass
#
#     # @abstractmethod
#     # def arie(self):  # aceste functii pot fi folosite de celelalte clase
#     #     pass
#
# class Triunghi(Poligon):
#     def nr_de_laturi(self):
#         print("Am 3 laturi")
#
#     def perimetru(self):
#         print("Perimetrul triunghiului este suma celor 3 laturi")
#
# class Patrat(Poligon):
#     def nr_de_laturi(self):
#         print("Am 4 laturi")
#
#     def perimetru(self):
#         print("Perimetrul triunghiului este suma celor 4 laturi")
#
#
# class Hexagon(Poligon):
#     def nr_de_laturi(self):
#         print("Am 6 laturi")
#
#     def perimetru(self):
#         print("Perimetrul triunghiului este suma celor 6 laturi")
#
# R = Triunghi()
# R.nr_de_laturi()
# R.perimetru()
#
# F = Patrat()
# F.nr_de_laturi()
# F.perimetru()
#
#
# G = Hexagon()
# G.nr_de_laturi()
# G.perimetru()


####ENCAPSULATION -FOLOSIM "_" LA METODELE CE NU VREM SA SE VADA
# class Counter:
#
#     def __init__(self):
#         self.__current = 0
#
#     def creste(self):
#         self.__current += 1
#
#     def valoare(self):
#        return  self.__current
#
#     def reset(self):
#         self.__current = 0
#
# counter = Counter()
# counter.creste()
# counter.creste()
# counter.current = 999
# counter.creste()
#
# print(counter.valoare())
#



# class Nume:
#     nume = None
#     prenume = None
#
#     def nume_complet(self,nume,prenume):
#         self.nume = nume
#         self.premnume = prenume
#         print(f"Nume complet {self.nume}{self.premnume}")
#
#     def descriere(self):
#         return self .nume_complet()
#
# n=Nume(Leonard, Tudor)

def __init__(self,name):
    self.name =name