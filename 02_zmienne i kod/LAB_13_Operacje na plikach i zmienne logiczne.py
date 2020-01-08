'''
Utwórz plik i wpisz do niego kilka słów, np co widzisz za oknem :)
Utwórz funkcję, która jako parametr przyjmuje ścieżkę dostępu do pliku i zwraca ilość słów w tym pliku, 
jeśli potrzebujesz kroków pomocniczych oto i one:
    Otwórz plik poleceniem open (możesz skorzystać z parametru encoding="utf-16" jeżeli trzeba)
    Wczytaj plik do zmiennej korzystając z funkcji read()
    "Rozbij" wczytaną zawartość korzystając z funkcji split()
    Policz ile elementów jest zwracanych przez funkcję split()
    Zwróć tą wartość
'''

import os
path = r'C:\Users\USER\Dysk Google\Coursera\Udemy\05_Python dla srednio zaawansowanych\02_zmienne i kod\temp.txt'

def slowa(path):
    f = open(path)
    data = f.read().split()
    count = len(data)
    return count

'''
W głównym skrypcie:
    zadeklaruj zmienną path i przypisz jej wartość wskazującą na plik utworzony na początku
    napisz polecenie warunkowe, które sprawdzi czy plik istnieje
        jeśli tak, wywoła funkcję, policzy ilość słów w pliku i wyświetli o tym informację 
    napisz wyrażenie logiczne, które wykona te same czynności, co wcześniej napisana instrukcja if
'''

if os.path.isfile(path):
    print('There are',slowa(path), 'words in the file', path)

os.path.isfile(path) and print("There are {} words in the file {}".format(slowa(path), path))