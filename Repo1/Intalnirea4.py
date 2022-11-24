# while / while else

# i = 0
# while i <= 1100:
#     print(i)
#     if i < 1000:
#         print('Bravo')
#     else:
#         print('Nu e bine')
#     i = i + 1
#     i = i + 10
#     i = i + 99
# else:
#     print('Am ajuns la limita')

# for /for else

# for i in range(4, 0,-2):
#     print(i)
# else:
#     print('Am ajuns la limita')

# mancare = ['hamburger', 'senvis', 'lapte', 'oua', 'dulceata', 'hamburger', 'hamburger', 'hamburger']
# for tip_mancare in mancare:
#     if tip_mancare == 'hamburger':
#         nr_ham = mancare.count('hamburger')
#         print(f'Clientii au cumparat un numar de {nr_ham} hamburgeri')
#     elif tip_mancare == 'oua':
#         nr_oua = mancare.count('oua')
#         print(f'Numarul de oua vandut este {nr_oua}')

# break
# for i in range(999):
#     if i == 4:
#         break
#     print(f'{i} dupa break')


#continue
# for i in range(5):
#     if i == 2:
#         print(f"Am ajuns la doi, sarim peste el")
#         continue
#     print(f'{i}')

#exit
for i in range(88):
    if i == 4:
        print("Am ajuns la 4 si putem iesi din loop")
        exit()
    print(f"{i}")