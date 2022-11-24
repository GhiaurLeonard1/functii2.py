""""
Pentru toate exercitiile Apelati functia de cel putin 2 ori cu valori diferite pentru a testa
Daca functia este return,printati raspunsul
"""
import datetime

#Ex.1)Functie care sa calculeze si sa returneze suma a doua numere
# def suma(a,b):
#     return a+b
#
# print(suma(2,3)) #5
# print(suma(5,6)) #11
# print(suma(7,10)) #17

# #Ex.2)Functie care sa returneze True daca  un numar este par si False daca este impar.
# def nr_nat(numar):
#     if numar % 2 == 0:
#         return False
#     else:
#         return True
# #
# #
# rasp= nr_nat(-4)# False
# print(rasp)
# rasp= nr_nat(5)# True
# print(rasp)
# rasp= nr_nat(9)# Truee
# print(rasp)

# # Ex.3)Functie care returneaaza numarul total de caractere din numele tau complet(nume,prenume,nume_mijlociu)
# def number_of_characters(first_name, last_name, middle_name):
#     sum = len(first_name)+ len(last_name)+ len(middle_name)
#     return sum
#
#
# print(number_of_characters("Ghiaur", "Leonard","Valentin"))
# print(number_of_characters("Zaharia", "Tiberiu","Ion"))

# Ex.4)Functie care returneaza aria dreptunghiului
# def aria_dreptunghiului(l,L):
#     return l*L
#
# print(f"Aria dreptunghiului este de {aria_dreptunghiului(5,9)}")
# # print(f"Aria dreptunghiului este de {aria_dreptunghiului(20,78)}")
# # print(f"Aria dreptunghiului este de {aria_dreptunghiului(2,6)}")

# #Ex.5)Functie care returneaza aria cercului
# def aria_cercului(R):
#     Aria = 3.14 *R ** 2
#     return Aria
# print(aria_cercului(4))
# # print(f"Aria cercului este de {aria_cercului(4)}")

# #Ex.6) Functie care returneaza True daca un caracter introdus x se gaseste intr-un string dat. False daca nu.
#
# character = input(f'Please insert a character to verification appear in string :\n')
#
#
# def return_character(string):
#     if character in string:
#         return True
#     else:
#         return False
#
# # print(return_character("simfonie"))
# print(return_character("xerox"))
#
# def check(s):
#     str="simfonie"
#     if s in str:
#         return True
#     else:
#         return False
#
# print(check("a"))

# #Ex.7)Functia fara return primeste un string si printeaza pe ecran:
# #   -Nr de caractere lower este x
# #   -Nr de caractere upper este y
#
# def nr_caractere(s):
#     d = {"upper_case": 0,"lower_case":0}
#     for c in s:
#         if c.isupper():
#             d["upper_case"] +=1
#         elif c.islower():
#             d["lower_case"]+=1
#
#     print(f"Numarul de upper case este:",d["upper_case"])
#     print(f"Numarul de lower case este:",d["lower_case"])
#
# print(nr_caractere(f"Numarul Total De CaracterE mici este"))


# def count_letters(string):
#     count1 = 0
#     count2 = 0
#     for x in string:
#         if x.isupper():
#             count1 += 1
#         if x.lower():
#             count2 += 1
#     print(f'Numbers of upper characters is {count1}')
#     print(f'Numbers of lower characters is {count2}')
#
#
# count_letters('THIS is a Sample Text')


# #Ex.8) Functie care primeste o lista cu numere si returneaza o lista doar cu numere pozitive
#
# def numbers_positive(list1):
#     return [abs(n) for n in list1]# functia abs sterge minusul sau plusul din fata int-urilor
#
#
# print(numbers_positive(list1=[2, -3, 0, -1, 53, 90, 4, 10, -45, -8, ]))

# Ex.9) Functia care nu returneaza nimic.Primeste 2 numere si printeaza:
#-Primul nuar este mai mare decat al doilea numar
#-Al doilea numar este mai mare decat primul numar
#- numerele sunt egale

# def numbers(x,y):
#     if x>y:
#         print(f"Primul numar {x} este mai mare decat al doilea numar {y}")
#     elif x<y:
#         print(f"Al doilea numar {y} este mai mic decat primul numar {x}")
#     else:
#         print(f"Numerele sunt egale")
#
# print(numbers(15,6))
# print(numbers(5,16))
# print(numbers(6,6))

#Ex.10) Functie care primeste un numar si un set de numere.
#Printeaza "am adaugat numarul nou in set" + returneaza True
#sau Printeaza"nu am adaugat numarul in set.Acesta exista deja"+ returneaza False

# def functie(x,set={}):# am definit o functie care primeste un numar si un set
#     if x in set :# am pus conditia daca numarul se regaseste in set
#         print(f"nu am adaugat numarul {x} in set.Acesta exista deja.")
#         return False
#     else:
#         set.add(x)#adaugam numarul in set
#         print(f"am adaugat numarul {x} in set.")
#         return True
#
# print(functie(5,set={7,6,2,12}))
# print(functie(5,set={7,5,2,12}))

#Ex.11)Functie care primeste o luna din an si returneaza cate zile are acea luna:
# from calendar import monthrange # am importat din calendar zilele lunii
# num_days = monthrange(2022,10)[1]# am introdus anul, luna si separat []
# print(num_days)
# #
# from calendar import monthrange
# def numar_zile_ale_lunii(an=2022,luna=2):
#     return monthrange(2022,2)[1]
# print(numar_zile_ale_lunii(2022,2))

#Ex.12)
""""
Functie calculator care sa returneze 4 valori:Suma, Diferenta,Inmultirea,Impartirea a 2 numere
 In final vei putea face:
 a,b,c,d= calculator(10,2)
 print("Suma:", a)
 print("Diferenta:", b)
 print("Inmultirea:", c)
 print("Impartirea:", d)
"""
# def calculator(x,y): # am definit functia calculator
#     suma = x+y            #am introdus formulele
#     diferenta = x-y
#     inmultirea = x*y
#     impartirea = x/y
#     return suma,diferenta,inmultirea,impartirea # returneaza rezultatul formulelor
#
# a,b,c,d= calculator(10,2)# am salvat formulele in variabile si am folosit cele 2 valori pentru toate formulele
# # a,b,c,d= calculator(7,3)
# # a,b,c,d= calculator(16,6)
#
# print("Suma numerelor este:",a)
# print("Diferenta numerelor este:",b)
# print("Inmultirea numerelor este:",c)
# print("Impartirea numerelor este:",d)

#Ex.13)
#Functie care primeste o lista cu cifre(adica doar 0-9) Ex:[1,3,1,5,9,7,7,5,5]
#Returneaza un DICT care ne spune de cate ori apare fiecare cifra

# def frecventa_numere(list):
#     dict ={}# am declarat dictionarul
#     list = [1,1,4,1,2,2,5,5,6,8,7,9,0,0,1,0,2,3]# am primit lista
#     for i in list:# pentru orice numar in lista
#         dict[i]=dict.get(i,0)+1# dictionar x calculeaza x se gaseste de 0+1 ori de fiecare data cand il vede
#     return dict
#
# print(frecventa_numere(list))

#Ex.14)
""""
Functie care primeste 3 numere si returneaza valoarea maxima dintre ele
"""
# def val_maxima(x,y,z):
#      if x<y<z:
#          return f"Valoarea maxima dintre ele este:{z}"
#      elif x>y>z:
#          return f"Valoarea maxima dintre ele este:{x}"
#      else:
#          return f"Valoarea maxima dintre ele este:{y}"
#
# print(val_maxima(4,9,2))
# print(val_maxima(1,5,6))
# print(val_maxima(16,61,66))

#Ex.15)
""""
Functie care primeste 1 numar si returneaza suma tuturor numerelor de la 0 la acel numar
Ex.daca avem 3, Suma va fi 6(0+1+2+3)
"""
# def sum(i):# am seclarat functia
#     if i==0:# numarul pleaca de la 0
#         return 0
#     else:
#         return i+sum(i-1)#numar +suma numerelor anterioare
#
#
# print(sum(6))

#Ex.16)
""""
Functie care primeste 2 liste de  numere(numerele pot fi dublate) si returneaza numerele comune
"""
# def common_numbers(list1, list2):
#     difference = list1.intersection(list2)
#     return difference
#
# print(common_numbers(list1 = {1,1,2,3},list2 = {2,2,3,4}))
# print(common_numbers(list1 = {1,3,4,3},list2 = {4,1,3,4}))

#Ex.17)
""""
Functie care sa aplice reducere de pret 10%. Tratati cazurile in care reducerea este invalida reducere de 110 % invalida
"""
# def reducere_10(a,b):
#     if b> 110:
#         print("Reducerea este invalida, nu se poate aplica!")
#     elif b<=100:
#         print(f"Reducerea este de:",int((a/100)*b),"$")
#         print(f"Pretul redus este de:",a-(a/100)*b,"$")
#
# print(reducere_10(120,70))
# print(reducere_10(120,100))
# print(reducere_10(450,120))

#Ex.18)
""""
Functie care sa afiseze data si ora curenta din Romania;(Bonus: data si ora din China)
"""
# import datetime
# now = datetime.datetime.now()
#
# print("Data si ora curenta in Romania:",now.strftime("%Y-%m-%d %H:%M:%S")

#Ex.18)
# Functie care sa afiseze cate zile mai sunt pana la ziua ta/pana la Craciun.

#
# import datetime
#
# def ziua_mea():
#     azi = datetime.date.today()
#     print(datetime.date.day)
#     ziua_mea = datetime.date(2023,2,24)
#     zile_ramase = (azi-ziua_mea).days
#     print("Mai sunt  \n" +{diff.days} +" \n zile ramase pana la ziua mea!")
#
# print(ziua_mea(2022,10,27))

# from datetime import datetime
# import pytz
# timezone = pytz.timezone("Asia/Singapore")
# # you can generate a string using `.strftime()` method
# date_string_with_specific_timezone = datetime.utcnow().astimezone(tz=timezone).strftime('%d.%m.%Y %H:%M')
# print(date_string_with_specific_timezone)

# def discount():
#     pret_original=500
#     discount1 = pret_original*0.2
#     # discount2 = (pret_original/100)*20
#     print(pret_original)
#     # print(discount2)
#     pret_vanzare = pret_original-discount1
#     return pret_vanzare
#
# print(discount())

# plata_lunara = 725
# plata_anuala1 = plata_lunara*12
# print("Plata ta anuala este de $",format (plata_anuala1,",.2f"), sep="")#afisam suma cu , si fara spatiu intrevaluta si venit

    #afisam un numar in campul de latime 12
# print("Numarul este", format(12345.6789,"12,.2f"))

# print(format(0.5,".0%"))# 50%

print(format(123456, ",d"))#1 23,456





