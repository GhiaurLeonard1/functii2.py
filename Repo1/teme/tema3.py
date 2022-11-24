#Ex.1)
# note_muzicale = ["do","re","mi","fa","sol","la","si","do"]# am declarat lista
# print(note_muzicale)
# note_muzicale = note_muzicale[::-1]#am inversat ordinea elementelor din lista si am suprascris lista
# print(note_muzicale)
# note_muzicale.reverse()# am folosit metoda reverse pentru a ajunge la varianta initiala
# print(note_muzicale)

#Ex.2)
# print(len("do"))

#Ex.3)
# lista1 = [3,1,0,2]
# lista2 = [6,5,4]
# x = lista1 +lista2
# print(x)
# lista2.extend(lista1)
# print(lista2)

#Ex.4)
# lista2.sort()
# print(lista2)
# del lista2[0]
# print(lista2)

#Ex.5)
# if len(lista2) <= 0:
#     print("Lista este goala!")
# else:
#     print("Lista nu este goala!")

#Ex.6)
# del x
# print(x)

#Ex.7)
# lista2 = []
# if len(lista2) <= 0:
#     print("Lista este goala!")
# else:
#     print("Lista nu este goala!")

#Ex.8)
# dict1 = {"Ana":"8","Gigel":"10","Dorel":"5"}
# a =dict1.keys()
# print(a)

#Ex.9)
# ana = dict1.get("Ana")
# gigel = dict1.get("Gigel")
# dorel = dict1.get("Dorel")
# print(f"Ana a luat nota {ana} ")
# print(f"Gigel a luat nota {gigel} ")
# print(f"Dorel a luat nota {dorel} ")

# #Ex.10)
# dict1.update({"Dorel":"6"})
# print(dict1["Dorel"])

# Ex.11)
# del dict1["Dorel"]
# # print(dict1)
# dict1.update({"Ionica":"9"})
# print(dict1)

# # Ex.12)
# zile_sapt = {"luni","marti","miercuri","joi","vineri","sambata","duminica"}
# weekend = {"sambata","duminica"}
# zile_sapt.add("luni")
# print(zile_sapt)#nu permite duplicate iar elementele le afiseaza random

# Ex.13)
# zile_sapt = {"luni","marti","miercuri","joi","vineri","sambata","duminica"}
# weekend = {"sambata","duminica"}
# if weekend.issubset(zile_sapt):
#     print("Weekend este un subset al lielelor din sapt")
# else:
#     print("Weekend  nu este un subset al lielelor din sapt")

#Ex.14)
# zile_sapt = {"luni","marti","miercuri","joi","vineri","sambata","duminica"}
# weekend = {"sambata","duminica"}
# a = zile_sapt.difference(weekend)
# print(a) #{'joi', 'miercuri', 'marti', 'luni', 'vineri'}

#Ex.15)
# zile_sapt = {"luni","marti","miercuri","joi","vineri","sambata","duminica"}
# weekend = {"sambata","duminica"}
# b = weekend.issubset(zile_sapt)
# print(weekend)

#Ex.16)Exerciții Opționale - grad de dificultate: Mediu spre greu(may need google) .
"""1. Ne imaginăm o echipă de fotbal pt teren sintetic.
3 Schimbări maxime admise:
● Declară o Listă cu 5 jucători
● Schimbari_efectuate = te joci tu cu valori diferite
● Schimbari_max = 3
Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
- Efectuează schimbarea
- Șterge jucătorul scos din listă
- Adaugă jucătorul intrat
- Afișaza a intra x, a ieșit y, mai ai z schimbări
Dacă jucătorul nu e în teren:
- Afișează ‘ nu se poate efectua schimbarea deoarece jucătorul x nu e în
teren’
- Afișează ‘mai ai z schimbări’

Testează codul cu diferite valori
Google search hint
“how to check if item îs în list python”
"""
#Ne imaginam o echipa de fotbal pt teren sintetic.
# 3 Schimbari maxime admise
#
# Declara o Lista cu 5 jucatori
# Schimbari_efectuate = va jucati voi cu valori diferite
# Schimbari_max = 3
#
# Daca Jucatorul x e in teren si mai avem schimbari la dispozitie
# -	Efectuam schimbarea
# -	Stergem jucatorul scos din lista
# -	Adaugam jucatorul intrat
# -	Afisam a intra x, a iesit y, mai aveti z schimbari
# Daca jucatorul nu e in teren:
# -	Afisati ‘ nu se poate efectua schimbarea deoarece jucatorul x nu e in teren’
# -	Afisati ‘mai aveti z schimbari’
#
# SCHIMBARI_MAX = 3
# schimbari_ramase = SCHIMBARI_MAX  #j6, j7, j8
# echipa = {'j1', 'j2', 'j3', 'j5', 'j4'}
# jucator_out = input('introduceti un jucator care sa iasa')
# jucator_in = input('introduceti un jucator sa intre ')
#
#
# if jucator_out in echipa and schimbari_ramase > 0:
#     if jucator_in in echipa:
#         print('Nu putem face schimbarea')
#     else:
#         echipa.remove(jucator_out)
#         echipa.add(jucator_in)
#         schimbari_ramase = schimbari_ramase - 1
#         print(f'Am introdus {jucator_in}')
#         print(f'Am scos {jucator_out}')
#         print(f'echipa actuala este {echipa}')
#         print(f'Mai avem {schimbari_ramase} schimbari')
# else:
#     if schimbari_ramase <= 0:
#         print(f'Nu mai avem schimbari')
#     else:
#         print(f'Nu putem face schimbarea pentru ca jucatorul {jucator_out} este deja in teren')
#
