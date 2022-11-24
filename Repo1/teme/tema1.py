# #Ex.1)
# Variabila- se poate scrie sub forma de(snake, pascal sau camel case)si este o cutiuta in care putem pune patru tipuri de valori.(int,string,float,bool).Nu poate contine spatii si nu poate incepe cu numere.
# #Ex.2)
# var1, var2, var3, var4 = ("sring"), (12), (True), (24.56) #am declarat si initializat 4 tipuri de variabile
# print(var1, var2, var3, var4)
# #Ex.3)
# print(type(var1))  #Am folosit funtia type pentru a verifica tipul de date
# print(type(var2))
# print(type(var3))
# print(type(var4))
#
# #Ex.4)
# print(round(var4))  #Am folosit functia de rotunjire pentru variabila de tip float.(var4)
# var4 = 25  #Am salvat rezultatul in aceeasi variabila(suprascriere)
#
# #Ex.5)  Afisez propozitii cu cele 4 tipuri de variabile
# Var2 = (300)
# Var3 = (754.730)
# Var4 = True
# Var1 = ("car")
# print("I bought a " + Var1 + " from 1989 for " + str(Var3) + " Euro, and it has " + str(Var2) +" "+ str(Var4)+" Km.")
#
# Var1 = ("John")
# Var2 = int(45)
# Var3 = float(1.70)
# Var4 = True
# print("John is "+ str(Var2)+" years old, him weight is " + str(Var3) + " meters, and is " + str(Var4) + " that he live in Canada.")
#
# Var1 = str("Anna")
# Var2 = int(2)
# Var3 = float(1.70)
# Var4 = True
# print(f'It is {Var4} that {Var1} has {Var2} dogs, and she bought for them {Var3} kilograms of dog food.')
#
# Var1 = str("pool")
# Var2 = int(20)
# Var3 = float(2.30)
# Var4 = False
# print(f"It is {Var4} that the maximum water deph in my {Var1} is {Var3} meters, and it is {Var2} meters long.")
#
#Ex.6)
# nume = ("Ghiaur")
# # print(nume)  #citesc nume de la tastatura
# prenume = ("Leonard")
# # print(prenume) #citesc prenume de la tastatura
# numele_complet = nume +prenume   # salvez numele complet intr-o variabila
# # print(len(numele_complet))  # calculez cate caractere are numele complet
# x = len(numele_complet)   #salvez rezultatul calculatorului in variabila x
# # print(x)
# print(f"Numele complet are {x} caractere")

# #Ex.7)
# lungimea = 4
# print(lungimea)  #citesc lungimea
# latimea = 3
# print(latimea) #citesc latimea
# aria_dreptunghiului = lungimea * latimea  # calculez aria dreptunghiului(poti calcula aria daca ai doua int-uri)
# # print(aria_dreptunghiului)
# print(f"Aria dreptunghiului este {aria_dreptunghiului}")
# # print(type(aria_dreptunghiului))

#Ex.8)
# var = "Coral is either the stupidest animal or the smartest rock"
# print(var.count("the"))   # aflam de cate ori apare "the" in variabila.

# #Ex.9)
# var = "Coral is either the stupidest animal or the smartest rock"
# varTHE = var.replace("the","THE")  # Inlocuiesc "the" cu "THE" prin apelarea variabilei var cu replace(ceea ce vreau sa inlocuiesc) si o salvez in alta variabila
# print(varTHE)

#Ex.10)
# var = "Coral is either the stupidest animal or the smartest rock"
# # Din diferenta celor doua rezultate cu aceeasi functie, rezulta ca variabila {var} nu este alcatuita din numere.
# myvar = var.isdigit()  #demonstram daca variabila este formata numai din litere (raspuns=>False)
# # daca am inlocui continutul variabilei  var ,cu un numar, (raspunsul=>True) ca este alcatuit numai din cifre.
# print(myvar)
# my_var_num = "123" # declaram si initializam o variabila ce contine numai numere
# # daca am schimba continutul variabilei my_var_num, cu litere, (raspunsul=> False) ca nu este format din cifre.
# myvar1 = my_var_num.isdigit()# demonstram ca aceasta variabila este formata numai din numere(raspuns=>True)
# print(myvar1)
#
# verify_digit = var.isdigit()
# print(f'Este {verify_digit} ca variabila var contine cifre')

#Ex.16)
# string = "GhiaurLeonard"
# print(string)
# w = len(string)# lungimea variabilei este de 13 caractere.
# a = w / 2      # am impartit lungimea la 2 sa aflam mijlocul
# b = round(a) #am rotunjit mijlocul ca sa aflam de la cecaracter trebuie sa incepem afisarea
# # print(b)
# print(string[6:7])   #Am inceput de la 6 , am adunat la caracterul 6 +1(un caracterul din mijloc) si am aflat unde ne oprim cu printarea.

# #Ex.17)
"""
“Un palindrom este un șir de caractere (de obicei cuvinte, fraze sau numere) care citit de la stânga la dreapta 
sau de la dreapta la stânga rămâne neschimbat. Termenul „palindrom” a fost introdus de scriitorul englez 
Ben Jonson (1572-1637) și provine de la cuvintele grecești palin (πάλιν; „înapoi”) și 
dromos (δρóμος; „drum, direcție”).” 
"""
# original = input("Enter the value:") # (madam, racecar, mom,) demonstram ca un string este palidrome
# reverse = original[::-1]
# assert reverse == original
# print(f'This is a palindrome string.')
#
#
# s = input("Enter the value:")  #Aceasta varianta ne demonstreaza ca un int sau un string este sau nu palidrom
# reverse = s[::-1]
# if(s == reverse):
#     print(f"This is a palindrome!")
# else:
#     print(f"This is not a palindrome!")

# # #Ex.18) Orice am introduce de la tastatura va arata acelasi mesaj
# intro = str(input('Introdu urmatoarele valori ale variabilelor : '))
# var1 = "alabala"
# var2 = "portocala"
# print(f'{var1} {var2}')

#Ex.20)
"""citeste un user de la tastatura
citeste o parola
afiseaza: 'Parola pt user x este ***** si are x caractere'
***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie sa afiseze corect
eg: parola abc => ***
parola abcd => ****
"""

# user = input("Introduceti User:")            # citeste un User de la tastatura
# parola = input("Introduceti parola:")        # citeste Parola de la tastatura
# cont = len(parola)                            #se calculeaza lungimea parolei
# par = cont * "$"                         #inlocuieste cate caractere contine parola  cu "*"
# print(f"Userul este:{user} \nParola lui {user} este {par} \nSi are {cont} caractere.")

