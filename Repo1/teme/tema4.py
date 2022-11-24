#Ex.1)
# masini = ["Audi","Volvo","Mercedes","Aston Martin","Lastun","Fiat","Trabant","Opel"]
# for x in range(0,len(masini)):
#a)
#     print(f"Masina mea preferata este {masini[x]}")#am iterat toata lista
# #b)
# for x in masini:
#     print((f"Masina mea preferata este {x}"))
# #c)
# x = 0
# while (x < len(masini)):
#     print(f"Masina mea preferata este {masini[x]}")
#     x += 1

#Ex.2)
# for x in range(1,len(masini)-1):#am scris cu majuscule toate elementele cu exceptia primului si ultimului.
#     masini[x] = masini[x].upper()
# else:
#     print(masini)

# #Ex.3)
# for x in masini:
#     if x == "Mercedes":
#         print(f"Am gasit masina {x} dorita de dumneavoastra!")
#         break
#     else:
#         print(f"Am gasit masina {x}.Mai cautam.")

# Ex.4)
# for x in masini:
#     if x=="Trabant":
#         continue
#     if x=="Lastun":
#         continue
#     else:
#         print(f"S-ar putea sa va placa masina {x}")

# Ex.5)
# masini_vechi=[]
# for x in range(len(masini)):
#     if masini[x]=="Lastun":
#         masini_vechi.append("Lastun") #adaugam un element in lista in masini vechi
#         masini[x]="Tesla"
#     if masini[x]=="Trabant":
#         masini_vechi.append("Trabant")
#         masini[x]="Tesla"
# print(f"Modelele noi sunt {masini}")
# print((f"Modelele vechi sunt {masini_vechi}"))

# Ex.6)
# pret_masini={
#     "Dacia":6800,
#     "Lastun":500,
#     "Opel":1100,
#     "Audi":19000,
#     "BMW":23000
#     }
# buget=15000
# for key,value in pret_masini.items():#tinem cont de itemii key si value
#     if value<= buget:
#         print(f"Pentru un buget de {buget} euro puteti alege masina {key}!")
# #(dict.items()) se pot compara si dupa len(buget)

# Ex.7)
# numere=numere=[5,7,3,9,3,3,1,0,-4,3]
# apare3 = []#am construit o variabila unde sa salvam numarul 3
# for x in numere:
#     if x==3:#daca gaseste 3
#          apare3.append(x)#sa il copie in variabila apare3
# print(f"Numarul 3 apare de {len(apare3)}")

# y=0# counter sau cel care calculeaza si pleaca de la 0
# numere=[5,7,3,9,3,3,1,0,-4,3]
# for i in numere:#daca i in numere
#     if i==3:# si i este 3
#         y=y+1 #calculeaza y +de cate ori apare in lista
#         print(f"Numarul {i} apare de  {y}  ori")

# Ex.8)
# numere=[5,7,3,9,3,3,1,0,-4,3]
# a=0
# for numar in numere:
#    #calculam elementele pas cu pas
#     a=a+numar
# print(f"Suma este {a}")#Am afisat suma numerelor fara sum

# Ex.9)
# numere=[5,7,3,9,3,3,1,0,-4,3]
# for x in numere:
#     x= sorted(numere)[5]#sorteaza numerele de la mic la mare si afiseaza (ultimul)cel mai mare numar
# print(x)
#
# numere=[5,7,3,9,31,3,1,0,-4,3]
# maxim=0
# for i in numere:
#     if i > maxim:
#         maxim=i
# print(f"Maxime este {maxim}")

#Ex.10)
# numere=[5,7,3,9,3,3,1,0,-4,3]
# for x in range(0,len(numere)):
#     if x>=0:
#         numere[x]=-numere[x]#afiseaza numerele pozitive in negative si invers
# print(numere)

# for x in numere:
#     print(-x)

# #Ex.11)
# alte_numere = [-5,7,2,9,12,3,1,-6,-4,3]
# numere_pare = []#am initializat 4 liste goale
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# #
# for x in alte_numere:
#     if x >= 0 :#daca x>=0 inseamna ca sunt pozitive
#         numere_pozitive.append(x) #atribuim numerele pozitive in lista numere_pozitive
#     if x < 0:
#         numere_negative.append(x)
#     if x % 2 == 0 and x>0:
#         numere_pare.append(x)
#     else:
#         numere_impare.append(x)
# print(numere_pozitive)
# print(numere_pare)
# print(numere_impare)
# print(numere_negative)

# #Ex.12))# Ordonati crescator fara sa folositi sort! De vizualizat linkul din tema!!!
# alte_numere = [-5,7,2,9,12,3,1,-6,-4,3]
# lista_ordonata = []
# while alte_numere:
#     min = alte_numere[0]
#     for x in alte_numere:
#         if x < min:
#             min = x
#     lista_ordonata.append(min)
#     alte_numere.remove(min)
# print(lista_ordonata)

# Ex.13) Ghicitoare de numar
# import random
# numar_ghicit =[]#initiem o lista noua
# numar = int(input("Alege un numar: "))
# numar_secret=random.randint(1,10)#conditionam ca numarul sa fie intre 1 si 10
# print(numar_secret)#printeaza numarul secret
# while numar<numar_secret:
#     print("Numarul secret e mai mare")
#     break
# if numar > numar_secret:
#     print("Nmarul secret este mai mic")
# elif numar ==numar_secret:
#     print("Felicitari! Ai ghicit!")

# #Ex.7)Scrieti un program care sa genereze o piramida de numere!!!!!!!!!!!!!!!!
# randuri = int(input("Introduceti un numar:"))
# for i in range(randuri +1):
#     for i in range(1):
#         print(1,and+"")
# print("")

#Ex telefon
# tastatura_telefon =(
# [1, 2, 3],
# [4, 5, 6],
# [7, 8, 9],
# [0],
# )
# for row in tastatura_telefon:
#     for col in row:
#          print(f"Cifra curenta este",row)



