'''

Flow control(controlam curgerea codurilor)-if else
 evalueaza conditii si bifurca codul in functie de rezultat
'''
# piesa_faina = True
# print('Pornim radio')
# if piesa_faina == False:
#     print('Dam mai tare')
#     print('fredonam')
# print('Oprim radio')

# if else
# daca numarul este par printam acest lucru
# altfel printam impar

# nr = 3
# # ce inseamna par? se imparte exact la 2
# #ce inseamna ca se imparte la 2?ne da rest 0
# if nr % 2 ==0:
#     print('nr par')
# else:
#     print('impar')
#
# if (nr > 0):
#     print("pozitiv")
# else:
#     print(" nu este pozitiv")
#
# # exercitiu acces interzis minorilor
# ani = int(input())
# if (ani >= 18):
#     print("Utilizatorul are acces")
# else:
#     print("Utilizatorul este minor si nu are acces")

# if, elif ,else
# ora = int(input("Introdu ora!"))
# # print (ora ==17)
# if ora <00:
#     print("Ora invalida!")
# elif ora <= 10:
#     print("Buna Dimineata")
# elif ora <= 14:
#     print("Buna Ziua")
# elif ora <= 20:
#     print("Buna Seara")
# elif ora <= 24:
#     print("Noapte buna!")
# else:
#     print("Reintroduceti ora exacta")


# roboélul telefonic
optiunea = int(input("Alege o optiune"))
if optiunea == 1:
    print("Ati ales Limba Romana!")
elif optiunea == 2:
    print ("Ati ales Limba Engleza!")
elif optiunea == 3:
    print ("Ati ales Limba Franceza!")
elif optiunea == 4:
    print("Ati ales Limba Italiana!")
elif optiunea == 5:
    print("Ati ales Limba Chineza!")
elif optiunea == 6:
    print("Ati ales Limba Japoneza!")
elif optiunea == 7:
    print("Ati ales Limba Coreeana!")
elif optiunea == 8:
    print("Ati ales Limba Greaca!")
elif optiunea == 9:
    print("Reveniti la meniul anterior")
elif optiunea == 0:
    print("Veti fi transferat catre un consultant!")
else:
    print("Alegerea dumneavoastra este incorecta!")

