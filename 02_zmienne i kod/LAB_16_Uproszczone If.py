'''Zapisz poniższe polecenie if w postaci uproszczonej:'''
price = 123
bonus = 23
bonus_granted = True
     
'''   if bonus_granted:
        price -= bonus
     
    print(price)
'''
price -= bonus if bonus_granted else price

print(price)

'''Zapisz poniższe polecenie if w postaci uproszczonej:
    rating = 5
     
    if rating == 5:
        print('very good')
    elif rating == 4:
        print('good')
    else:
        print('weak')
'''
rating = 5

print('very good') if rating == 5 else print('good') if rating == 4 else print('weak')
# albo w sposób poniżej
print('very good' if rating == 5 else 'good' if rating == 4 else 'weak')

'''Ktoś był kiedyś niezadowolony, bo w kursie jest za mało polskich akcentów, więc... 
posłuchaj piosenki De Mono - Niedziela będzie dla nas - 
https://www.youtube.com/watch?v=lmn0Qf1_eI4 (możesz też skorzystać z oryginalnej wersji: 
Niebiesko Czarnych: https://www.youtube.com/watch?v=Fxkhe8GqYkc)

Napisz program, który:
    zapisze w zmiennej today_weekday nazwę dzisiejszego dnia tygodnia
    bazując na pierwszej zwrotce piosenki serią poleceń if/elif/.../else ustali co dzisiaj powinieneś robić
Przepisz powyższy program stosując składnie uproszczona polecenia if'''



