""""
Colectiile de date sunt de 4 tipuri(List,Tuplu,Set,Dictionary)

List- se foloseste cel mai des
    -pastreaza toate tipurile de date
    - se pastreaza intre paranteze patrate("[]")
    - se poate ordona
    - un element nou se afiseaza la final
    - este mutabila(se poate adauga,sterge sau modifica)
    - accepta valori duplicat
    - lungimea (len) reprezinta nr de elemente

"""

# list1 = ["abc", "b23", "crue", "dalse", "eanana", "fortocala", "gortocala", "h.0"]
#
# print(len(list1))# listam numarul elementelor
# print(list1[:-1])# stergem ultimul element
#
# print(list1[::-1])# afiseaza alfabetic de la dreapta la stanga
# list1[0]="DEF" #schimbam primul element din lista cu ""DEF"
# print(list1)

# list1[0:3] = ["ADI", 499, False]
# print(list1)

# list1.insert(0, "banana")# adaugam un nou element in locul 0
# print(list1)
#
# print(len(list1))# printam numarul de elemente a listei
#
# list1.append("camion")# adaugam elementul la finalul listei
# print(list1)
#
# list1.remove("dalse")# sterge un element sin lista
# print(list1)
#
# list1.pop(7) # sterge elementul 7 din lista
# print(list1)
#
# list1.pop()  # sterge ultimul element din lista
# print(list1)

# del list1[0] # sterge elementul 0
# print(list1)

# del list1 # sterge list1
# print(list1)

# list1.clear()# sterge elementele din lista
# print(list1)

# for x in range(len(list1)): # afiseaza elementele pe verticala
#     print((list1[x]))

# print(len(list1))# listam numarul elementelor
# for x in list1:# printeaza lista de n"9" elemente pe orizontala
#     print(list1)

# x = 0
# while x < len(list1): # printeaza la infinit elementul x daca x <(nr elementelor din lista)
#     print(list1[x])
#     x+= 1# opreste comanda de print la infinit

# [print(str(x)) for x in list]
#               #<generator object <genexpr> at 0x000001ADE85261F0>

# list1 = ["ala", "ala", "ala", "bala", "portocala", "fortocala", "gortocala", "h.0"]
# print(list1)

# list1.sort(reverse=False)# ordoneaza alfabetic
# print(list1)

# list1.sort(reverse=True)# ordoneaza alfabetic de la dreapta la stanga
# print(list1)

# list2 =list1.copy() # copiem lista completa in
# print(list2)
#
# list3 = list(list1[:3])# copiem o insiruire de elemente
# print(list3)

# list2 = ["ala", "bala", "portocala"]
# print(list2)

# list3 = list2 + list1# lipeste elementele din lista 2 la cele din lista 1 intr-0 singuta lista
# print(list3)

# x = list3.count("ala")# calculeaza de cate ori se gaseste elementul in lista
# print(x)

# list4 = ["1", "2", "3"]
# list3.extend(list4)# extinde(adauga) elem din list4 in list3
# print(list3)

# list5 = ["a", "b", "c"]
# list6 = ["a", "b", "c"]
# assert list6 == list5 # verificam daca listele sunt identice(nu afiseaza nici o eroare)
# daca nu sunt identice, vom primi ca rezultat un AssertionError!

# if os.path.exists("C:\Program Files (x86)\Autodesk\Autodesk Desktop App\CER\img"):
#     print(True)
# programul valideaza ca path-ul este adevarat


""""
Tuples
    -pastreaza mai multe valori
    - nu se poat schimba valorile
    - accepta valori duplicat
"""
# fruits = (True, "portocale", 3.0, "cirese") # fruits=tupla
# print(fruits)
# print(fruits[1])# afiseaza  elementul 1=portocale

# x = list(fruits)# transformam tupla in lista pentru a schimba valorile
# print(x)
# x[0] = "kiwi" # adaugam elementul nou in locul elementului 0
# fruits = tuple(x) #transformam lista in tupla
# print(fruits)

# fruits2 = (" cirese")
# fruits3 = fruits2 + fruits2# afiseaza = cirese cirese
# print(fruits3)

# fruits = (True, "portocale", 3.0, "cirese")# fruits=tupla
# fruits2 = (False, "cirese") # o tupla trebuie sa contina doua sau mai multe tipuri de valori
# fruits3 = fruits + fruits2
# print(fruits3)
# #
# x = fruits3.count(True)# afiseaza de cate ori apare elementul in tupla
# print(x)

# y = fruits3.index("portocale")# ne afiseaza numarul elementuluidin paranteza
# print(y)
# print(f"Am un cos plin cu {fruits[3]}")# preia elementulnr 3 si o afiseaza

""""
Seturile -se mai folosesc pentru verificarea CNP-urilor
        -se pot adauga sau sterge valori
        -nu accepta valori duplicat
        -se folosesc acolade
"""
# setul1 = {"mar", "banana", "cireasa"}
# print(setul1)
# print(len(setul1))# afiseaza nr de elemente din set
#
# for x in setul1:# afiseaza elementele pe verticala
#     print(x)
#
# setul1.add("pineapple")# adaugam un element
# print(setul1)
#
# setul1.remove('pineapple') # sterge un element
# print(setul1)
# setul2 = {"mar", "cartof", "cireasa", "test", "alin", "verde"}
#
# setul3 = setul2.union(setul1) #Se lipesc seturile iar la fiecare comanda de run se amesteca random elementele
# print(setul3)
# #
# setul1.update(setul2) #se adauga setul1la setul 2
# print(setul1)
#
# x = setul1.difference(setul2)#ne afiseaza diferenta de elemente dintre cele 2 seturi
# print(x)

# setul2.discard('cartof')# scoate elementul din paranteze
# print(setul2)
#
# setul2.pop() #scoate random un element la fiecare comanda run
# print(setul2)

# setul3 = {'a', 'b', 'c'}
# setul4 = {'f', 'g', 'h', 'a', 'b', 'c'}
# x = setul3.issubset(setul4)#verifica daca este subset(daca setul4 contine setul3)
# print(x)
#
# setul5 = {'f', 'g', 'h', 'a', 'b', 'c'}
# setul6 = {'a', 'b', 'c'}
# y = setul5.issuperset(setul6)#verifica daca este superset(setul5 contine setul6)
# print(y)


# a=5
# b=9
# formatSir1 = "Setul este {{{},{}}}."
# setSir1 = formatSir1.format(a,b)
# print(setSir1)#Setul este {5,9}.

""""
Dictionarul -sunt ordonte
            -sunt mutabile
            -nu accepta key(ïndexi) duplicat
            -se folosesc acolade
            -dupa ultimul element din dictionar nu se pune nici un semn de punctuatie
"""
# dicti = {"nota": "10",
#          "nume": "Matei",
#          "clasa": "9"
#         }
# print(len(dicti))# afiseaza cate perechi(keie + valoare) contine
#
# print(dicti['nota'])#printeaza valoarea dupa keia atribuita
# x = dicti.get('nota')#returneaza valoarea keii
# print(x)
# y = dicti.keys()#returneaza numai cheile
# print(y)
# z = dicti.values()#returneaza numai valorile
# print(z)

# dicti['nota'] = 7 #folosim cheia Nota cu noua valoare
# print(dicti)
# dicti.update({'nota': '11'})#schimbam valoarea
# print(dicti)
# dicti['materie'] = 'matematica'# adaugam o noua keye si valoarea sa
# print(dicti)
# dicti.update({'medie': '7.85'})# adaugam o keye si valoarea sa noua
# print(dicti)
#
# dicti.pop('medie') #sterge keia medie cu valoare sa
# print(dicti)
# dicti.pop(dicti)
# print(dicti)
# del dicti['nota']#scoate keia nota cu valoarea ei
# print(dicti)
#del dicti - sterge dictionarul

# dicti.clear()# sterge continutul dictionarului
# print(dicti)

# for x in dicti:
#     print(x)       # printeaza cheile pe verticala(una sub alta)

# for y in dicti:
#     print(dicti[y])   # printeaza valorile cheilor pe verticala
#
# dict2 = dicti.copy()#copiem dictionarul
# print(dict2)
#
# dict3 = dict(dict2)#copiem cu ajutorul formulei dict
# print(dict3)
#
#
# familie = {'copil1': {'Index_zero': 'Matei', 'an': '1990'},
#            'copil2': {'123': 'Andrei', 'an': '1991'},
#            'copil3': {'456': 'Andrei', 'an': '1991'}
#            }
# print(familie)
# x = dict3.setdefault('culoare', 'rosu')#adaugam o noua valoare keii culoare
# print(x)
# print(dict3)
# dict3.popitem() #sterge ultima keie cu valoarea sa
# print(dict3)
#
# dict4 = dict.fromkeys(dict3)
# print(dict4)
# x = {'key1', 'key2', 'key3'}# atribuim alte key
# y = 1990                    #atribuim o valoare idenica celor 3 kei de mai sus
# dict5 = dict.fromkeys(x, y)#salvam modificarile de mai sus in dict5
# print(dict5)

# print(familie['copil1']['an'])# imi returneaza date despre copil 1=>anul de nastere
