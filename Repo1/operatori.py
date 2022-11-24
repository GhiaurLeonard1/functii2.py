""""
Recap:
Variavile
tipuri de date: string,int,float,boot

 operatori aritmetici:**(ridicarea la putere)ex.10**3=10 la a 3-a *,/,+,-, % (restul impartirii).
 operatori de comparare: <>, ==,!=(diferit), >=,<=
 logici: and(si) ,or(sau), !(not)
operatori de atribuire: x=x+1(x+=1);y=y-2(y-=2);z=z*5(z*=5);total=total+number(total+=number)

 Flow control(controlam curgerea codurilor)-if else
"""
# a = 3
# b = 5
# print(a + b )# 3+5=8
#
# print(a==b)# a este egal cu b?= False

# print(a<b and a<4)# True si True=True
#
# print(a<b or a<4)# True sau True=True

#cu mama sau cu tata sau (cu bunicu si bunica)
# mama = True
# tata = False
# bunicu = False
# bunica = False
# print(mama or tata or(bunicu and bunica))# true

# mama = False
# tata = True
# bunicu = True
# bunica = True
# print(mama or tata or(bunicu and bunica)) # True

# mama = False
# tata = False
# bunicu = True
# bunica = True
# print(mama or tata or(bunicu and bunica)) # True

# mama = False
# tata = False
# bunicu = False
# bunica = True
# print(mama or tata or(bunicu and bunica)) # False


# mama = False
# tata = True
# bunicu = False
# bunica = True
# print(mama or tata or(bunicu and bunica)) # True

#afiseaza salariul unui angajat(rezultat eronat)
# def main():
#     #ia numarul orelorlucrate intr-o saptamana
#     ore = int(input("Introdu numarul orelor lucrate intr-o saptamana:"))
#     #punem conditia ca orele sa fie raliste
#     while ore > 40:
#         print("Eroare!Nu poti lucra mai mult de 40 ore!")
#         ore = int(input("Introdu orele corecte:"))
#     #ia salariulorar
#     sal_orar = float(input("Introdu salariul orar(lei/ora):"))
#     #calculeaza salariul
#     salariu = ore * sal_orar
#     #afiseaza salariul
#     print("Salariul este:lei", format(salariu, ",.2f"))
#
# #Chemam functia principala
# main()


