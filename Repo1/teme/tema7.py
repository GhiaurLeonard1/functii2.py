# #Ex.2)
# from abc import ABC, abstractmethod
#
#
#
# class FormaGeometrica(ABC):      #clasa abstracta FormaGeometrica
#     PI = 3.14                    #field
#
#     @abstractmethod              #metoda abstracta aria
#     def aria(self):
#         raise NotImplementedError
#
#     def descrie(self):           #metoda clasei descrie
#         print("Cel mai probabil am colturi")
#
#     def descrie_nou(self):  # definim o noua metoda descrie
#         print("Nu am colturi")
#
# class Patrat(FormaGeometrica):   # clasa patrat mosteneste din clasa parinte FormaGeometrica
#
#     def __init__(self, latura):  #constructor pentru latura
#         self.__latura = latura   #latura este proprietate privata
#
#     @property
#     def latura(self):            #definim latura care este proprietate privata
#         return self.__latura
#
#     def aria(self, aria_patratului=None):  # metoda ceruta de interfata unde definim aria_patratului
#         aria_patratului = self.__latura ** 2  # scriem formula ari_patratului si o salvam intr-o variabila cu acelasi nume
#         print(f"Aria patratului este {aria_patratului}")
#
#     @latura.getter              #implementam metoda getter.
#     def latura(self):
#         return self.__latura
#
#     @latura.setter              #implementam metoda setter.
#     def latura(self, latura):
#         print(f"Aceasta este o noua latura de {latura} a patratului")
#         self.__latura= latura
#
#     @latura.deleter             #implementam metoda deletter.
#     def latura(self):
#         print("Am sters o latura a patratului")
#         self.__latura = None
#
#
#
#
# class cerc(FormaGeometrica):# clasa cerc mosteneste din clasa parinte FormaGeometrica
#
#     def __init__(self, raza): #constructor pentru raza
#         self.__raza = raza     #raza este proprietate privata
#
#     @property
#     def raza(self):         #definim raza
#         return self.__raza
#
#     def aria(self, aria_cercului= None):   #metoda ceruta de interfata unde definim aria_cercului
#         aria_cercului = self.PI * self.__raza ** 2 #scriem formula ariei cercului si o salvam intr-o variabila
#         print(f"Aria cercului este {aria_cercului}")
#
#     @raza.getter
#     def raza(self):         # #initializam metoda getter
#         return self.__raza
#
#     @raza.setter
#     def raza(self, raza):   #initializam metoda setter
#         print(f"Aceasta este o noua valoare a  razei cercului de {raza} ")
#         self.__raza = raza
#
#     @raza.deleter
#     def raza(self):         #initializam metoda deletter
#         print("Am sters o raza a cercului")
#         self.__raza = None
#
#
#
# def descrie():# definim o noua metoda descrie
#     print("Nu am colturi")
#
#
# p = Patrat(10)
# p.descrie()
# p.aria()
# p.descrie_nou()
# p.latura= 8
# p.latura
# del p.latura
# p.latura=20
#
# cerc = cerc(10)
# cerc.descrie()
# cerc.aria()
# descrie()
# cerc.raza = 2
# cerc.aria()
# del cerc.raza
