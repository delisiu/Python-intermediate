'''W tym zadaniu należy zapisać na dysku zawartość kilku stron www. 
Po zakończeniu pobierania należy wyświetlić komunikat o powodzeniu. 
Jednak w przypadku błędu należy wyświetlić informację o błędzie i przerwać pętlę. 
Jeśli taki opis Ci wystarcza - do działa!

A oto opis "krok po kroku"
    zaimportuj moduły os i urllib.request
    w zmiennej data_dir zapisz ścieżkę do katalogu, w którym mają być zapisywane strony
    w zmiennej pages zapisz informacje o stronach do pobrania. Może to być np. lista słowników:
pages = [
    { 'name': 'mobilo',      'url': 'http://www.mobilo24.eu/'},
    { 'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/' },
    { 'name': 'kursy',       'url': 'http://www.kursyonline24.eu/'} ]
    dla każdej stony z pages:
        zapisz w zmiennej path ścieżkę to pliku powstałą z połączenia data_dir, 
        nazwy strony pobranej z  pages i ".html"
        korzystając z  funkcji urllib.request.urlretrieve(<adres strony>, <sciezka do pliku>) 
        zapisz stronę na dysku
        (na tym etapie przetestuj sobie działanie programu)
        wewnątrz pętli while dodaj blok try/except, który w przypadku błędu zakończy wykonywanie pętli, 
        wyświetlając komunikat o błędzie
        zakończ pętlę while poleceniem, które wykona się tylko wtedy gdy pętla nie została 
        w żaden sposób przerwana. Wyświetl tu komunikat o powodzeniu'''

import os
import urllib.request

data_dir = r'C:\Users\USER\Dysk Google\Coursera\Udemy\05_Python dla srednio zaawansowanych\02_zmienne i kod\Lab_19'

pages = [
    { 'name': 'mobilo',      'url': 'http://www.mobilo24.eu/'},
    { 'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/' },
    { 'name': 'kursy',       'url': 'http://www.kursyonline24.eu/'} ]

for x in pages:
  try:
    file_name = "{}.html".format(x["name"])
    path = os.path.join(data_dir,file_name)
    urllib.request.urlretrieve (x["url"], path)
    print('OK')
    
  except:
    print('failure page: {}'.format(x["name"]))
    break
 
else:
    print('download done')
  


    # urllib.request.urlretrieve(<adres strony>, <sciezka do pliku>)
    # path[i] = os.path.join(data_dir,x["name"],".html")
    