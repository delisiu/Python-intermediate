'''
    projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
    leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']
Korzystając ze "sprytnej" metody pracy z for wyświetl komunikaty w postaci:
The leader of "...nazwa projektu..." is ...imię i nazwisko lidera...'''

projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']

for i,j in zip(projects,leaders):
    print("The leader of",i,"is", j)
    print('The leader of {} is {}'.format(i,j))
print("\n","-"*90)
'''Utwórz kolejną listę z datami rozpoczęcia projektów:
dates = ['2016-06-23', '2016-08-29', '1994-01-01']
The leader of "...nazwa projektu..."  started ...data rozpoczęcia projektu... is ...imię i nazwisko lidera...'''

dates = ['2016-06-23', '2016-08-29', '1994-01-01']

for i,j,k in zip(projects,dates,leaders):
    print("The leader of",i,"started",j,"is", k)
    print('The leader of {} started {} is {}'.format(i,j,k))
print("\n","-"*90)

'''Korzystając ze "sprytnego" złożenia enumerate i zip 
- dodaj do komunikatu dodatkowo numer kolejny projektu rozpoczynając od 1:
...numer kolejny... - The leader of "...nazwa projektu..."  started ...data rozpoczęcia projektu... is ...imię i nazwisko lidera...'''

for num,(i,j,k) in enumerate(zip(projects,dates,leaders)):
    print(num+1,"- The leader of",i,"started",j,"is", k)
    print('{} - The leader of {} started {} is {}'.format(num+1,i,j,k))