#Ex.1)
""""
Functia if else o folosim atunci cand dorim sa verificam daca o
variabila este sau nu adevarata, daca contine sau nu numere, etc.
"""
# #Ex.2)
# x = int(input("Introdu valoarea lui x:"))
# if (x >= 0):
#     print(f"X este numar natural!")
# else:
#     print(f"X nu este numar natural!")

# #Ex.3)
# x = int(input("Introdu valoarea lui x:"))
# if x > 0:
#     print(f"X este numar pozitiv!")
# elif x < 0:
#     print(f"X este numar negativ!")
# else:
#     print(f"X este numar neutru!")

# #Ex.4)
# x = int(input("Introdu valoarea lui x:"))
# if x >= -2 and x <= 13: # Am folosit operatorul de comparare pentru a cauta o valoare intre 2 valori date.
#     print("X este intre -2 si 13!")
# else:
#     print("X nu este intre -2 si 13!")

# #Ex.5)
# x = int(input("Introdu valoarea lui x:"))
# y = int(input("Introdu valoarea lui y:"))
# if (x > y) and (x-y) < 5 and x >0:
#     print("Diferenta este mai mica de 5!")
# elif (y > x ) and (y-x) < 5 and y >0:
#     print("Diferenta este mai mica de 5!")
# else:
#     print(False)

# #Ex.6)
# x = int(input("Introdu valoarea lui x:"))
# if not ( x > 5 and x < 27 ): # Am folosit operatorul de comparare si not pentru a cauta o valoare intre 2 valori ("X  nu este intre 5 si 27!")
#     print("Este adevarat ca x nu se gaseste intre aceste 5 si 27")
# else:
#     print("X se gaseste intre 5 si 27")

# #Ex.7)
# x = int(input("Introdu valoarea lui x:"))
# y = int(input("Introdu valoarea lui y:"))
# if x == y:
#     print("x = y")
# elif x > y:
#     print(f"x={x}")
# elif y > x:
#     print(f"y={y}")
# else:
#     print("Eroare")

# #Ex.8)
# x = int(input("Introdu valoarea lui x:"))# latura x
# y = int(input("Introdu valoarea lui y:"))# latura y
# z = int(input("Introdu valoarea lui z:"))# latura z
# if x==y==z:
#     print("Triunghi echilateral")
# elif (x == y != z) or (y == z != x) or (z == x != y):
#     print("Triunghi isoscel")
# else:
#     print("Triunghi oarecare")

# #Ex.9)
# w = input("Tasteaza litera:") #citesc de la tastatura litera
# # a,e,i,o,u = ("a","e","i","o","u") # am atribuit vocalele unor varibile
# vocale = ("a","e","i","o","u")
# # if (w == a) or (w == e) or (w == i) or (w == o) or (w == u): # verific daca litera introduca este este vocala sau consoana
# if w in vocale:
#     print(f"{w} este vocala!")
# else:
#     print(f"{w}  este o consoana!")

#Ex.10)
# x = int(input("Introdu valoarea lui x:"))
# if (x >= 9) and (x <= 10): # am stabilit nota maxima de 10
#         print("A")
# elif x == 8:
#         print("B")
# elif x == 7:
#         print("C")
# elif x == 6:
#         print("D")
# elif x == 5:
#         print("E")
# elif x<=4 and x>=1:
# # elif (x == 4) or (x == 3)or (x == 2)or (x == 1):# am stabilit nota minima de 1
#         print("F")
# else:
#         print("Nu ati tastat nota corecta!")

# #Ex.11)
# x = int(input("Introdu minim 4 cifre:"))
# # print(type(x))
# y = len(str(x)) # !!!!!!!!!!!!!!!!!!!!!!!!!!!Ca sa numaram cifrele unui int. trebuie sa il transformam in string
# # print(y)
# if y <= 4: # Am pus conditia ca x sa aiba minim 4 cifre
#         print(f"{x} are {y} cifre")
# else:
#         print(f"{x} nu are minim 4 cifre!")

# #Ex.12)
# x = int(input("Introdu valoarea lui x:"))
# y = len(str(x)) # !!!!!!!!!!!!!!!!!!!!!!!!!!!Ca sa numaram cifrele unui int. trebuie sa il transformam in string
# if y == 6:
#      print(True)
# else:
#      print(False)

# #Ex.13)
# x = int(input("Introdu valoarea lui x:"))
# print(type(x))
# if x % 2 == 0:         # orice numar impartit la 2 cu rest 0 este par!
#     print("Numarul este par!")
# else:
#     print("Numarul este impar!")

# #Ex.14)
# x = int(input("Introdu valoarea lui x:"))
# y = int(input("Introdu valoarea lui y:"))
# z = int(input("Introdu valoarea lui z:"))
# print(type(x))
# print(type(y))
# print(type(z))
# if (x > y) and (x > z):
#     print((f" = {x}"))
# elif (y > x) and (y > z):
#     print(f"Y = {y}")
# elif (z > x) and (z > y):
#     print(f"Z = {z}")
# else:
#     print("Cel putin doua numerele sunt egale")

#Ex.15)
# x = int(input("Introdu valoarea lui x:"))
# y = int(input("Introdu valoarea lui y:"))
# z = int(input("Introdu valoarea lui z:"))
# if (x >= 10) and (y >= 10) and (z >= 10) and (x <= 150) and (y <= 150) and (z <= 150) and x+y+z == 180:
#     #daca suma unghiurilor este egala cu 180, rezulta ca triunghiul este valid
#     print("Triughiul este valid")
# else:
#     print("Triunghiul nu este valid!")

# #Ex.16)
# string = "Coral is either the stupidest animal or the smartest rock"
# x = int(input("Introdu valoarea lui x:"))
# a = len(string) # aflam lungimea stringului
# # print(a)
# b = int(a-x) # aflam diferenta de lungime pe care va trebui sa o printam
# # print(b)
# if (0 < x < a) and (b <= a): #conditionam x>0, a>x pentru a nu ne returna valori negative si asociem ca difeneta sa nu depaseasca lungimea stringului.
#     print(string[:b]) # in final printam bucata din string conform diferentei dintre a si x-ul introdus:
# else:
#     print("valoarea este prea mare")

# #Ex.17)
# string = "Coral is either the stupidest animal or the smartest rock"
# a = len(string) # aflam lungimea stringului
# # print(a)
# nr_caractere = 5# introducem nr de caractere ce dorim sa le afisam
# b = (a - nr_caractere)# calculam diferenta(de unde incepem sa citim ultimele 5 caractere)
# # print(b)
# string_nou = str(string[:nr_caractere]+string[b:a]) #declaram si initializam o varianta noua de tip string in care afisam primele 5 si ultimele 5 caractere din Stringul principal.
# print(string_nou)
# print(type(string_nou))#verificamtipul variabilei

#Ex.18)
""""
salveaza intr-o variabila si afiseaza indexul de start al cuvantului rock
(hint: este o functie care te ajuta sa faci asta)
folosind aceasta variabila + slicing, afiseaza tot stringul pana la acest cuvant
output: 'Coral is either the stupidest animal or the smartest ' 
"""
# string = "Coral is either the stupidest animal or the smartest rock"
# x = string.rstrip("rock")# taie ultimul element din string
# print(x)
# y= string.lstrip("Coral is") # taie primul element din string
# print(y)
# sau
#
# a = len(string)
# nr_caractere = 4
# index_start_rock = (a - 4)
# b = str(string[:index_start_rock])
# print(b)

#Ex.19)
# var = "racecaR"
# assert var.casefold()[0] == var.casefold()[-1]# .casefold or .lower ajuta programul sa fie case insensitive
# print("Primul si ultimul caracter sunt la fel")

#Ex.20)
# var1 = "0123456789"
# # print(type(var1))
# print(len(var1))
# numere_pare = var1[::2] #slicing bucatele(sau paranteze patrate) iar pasul este din cat in cat
# print(f"{numere_pare} sunt numere pare")
# numere_impare = var1[1::2]
# print(f"{numere_impare} sunt numere impare")

# #Ex.21) Verificare imbarcare
# pasaport = input("Detineti pasaport?")# confirmam cu da sau nu daca detinem pasaport
# if pasaport == "nu":#daca nu avem pasaport nu neputem imbarca si se opreste codul
#     print("Nu aveti permisiunea de imbarcare!")
# elif pasaport =="da":# daca avem pasaport ne va cere sa introducem varsta
#     varsta = int(input("Introduceti varsta:"))
#     if varsta >= 18:# daca avem 18 sau peste 18 ani ne putem imbarca
#         print(f"Persoana are varsta de {varsta} ani si detine pasaport!\n Va puteti imbarca!")
#     else:# daca avem sub 18 ani
#         if varsta < 18:
#             cu_mama = input("Calatoriti cu mama?")
#             cu_tata = input("Calatoriti cu tata?")
#         if cu_mama == 'da' and cu_tata == 'da':# si calatorim cu ambii parinti vom primi accept pentru imbarcare
#             print(f"Persoana are varsta sub {varsta} ani,detine pasaport si este insotita de ambii parinti!\n Va puteti imbarca!")
#         else:# altfel pentru a calatori doar cu un parinte ne trebuie permisiunea scrisa de la celalalt parinte
#             act_permisiune = input("Aveti permisiunea celuilalt parinte")
#             if cu_mama == 'da' or cu_tata == 'da' and act_permisiune=="da":# daca avem permisiunea de la un parinte si calatorim cu celalalt parinte
#                 # vom primi accept pentru imbarcare
#                 print(f"Persoana are varsta sub {varsta} ani,detine pasaport, este insotita de cel putin un parinte si are permisiunea de la celalalt parinte!\n Va puteti imbarca!")
#             else:
#                 print("Nu aveti permisiunea de imbarcare! ")#altfel nu vom primi accept pentru imbarcare.

#Ex.22) Joc ghicit zarul
# import random  #importam un numar random
# dice_roll = int(input("Zarul tau arata:"))   #numarul pe care il ghicim este salvat in variabila
# zar = random.randint(1,6)  #conditionam numarul random sa nu fie mai mic de 1 si mai mare de 6
# print(f"Ai ales {zar}")# afisam numarul ce trebuie ghicit
# while dice_roll > zar:
#     print(f"Ai pierdut.Ai ales un numar mai mic.Ai ales {dice_roll}, dar a fost {zar}")
#     break
# if dice_roll < zar:
#     print(f"Ai pierdut.Ai ales un numar mai mare.Ai ales {dice_roll}, dar a fost {zar}")
# elif dice_roll == zar:
#     print(f"Ai ghicit.Felicitari!Ai ales {dice_roll} si zarul a fost  {zar}")