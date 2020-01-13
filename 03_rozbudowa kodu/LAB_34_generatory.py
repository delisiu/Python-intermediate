'''W tym zadaniu należy przerobić listy z poprzedniego LAB do postaci generatora.  
Nieco problematyczne będzie ustalenie ile wartości jest generowanych przez generator, 
bo w tym celu... trzeba go przejść!
Jeżeli taki opis Ci wystarcza to GO! GO! GO!'''

ports = ['WAW', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
             'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

ports_list1 = ((a,b) for a in ports for b in ports)

ile1=0
for (i, j) in ports_list1:
    print("{} - {}".format(i, j))
    ile1+=1
print("-"*30)          



ports_list2 = ((a,b) for a in ports for b in ports if a != b)

ile2=0
for (i, j) in ports_list2:
    print("{} - {}".format(i, j))
    ile2+=1
print("-"*30)

ports_list3 = [(a,b) for a in ports for b in ports if a < b]

ile3=0
for (i, j) in ports_list3:
    print("{} - {}".format(i, j))
    ile3+=1

print("-"*30)
print(ile1)
print(ile2)
print(ile3)

'''A tu dokładniejsza instrukcja:
Na przekręcie z wpłatomatem z poprzedniego zadania postanawiasz wraz ze swoim szefem 
otworzyć linie lotnicze "Flying Python". Linie będą krajowe. Oto wykaz portów lotniczych:
    ports = ['WAW'P, 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
             'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']
1. Zbuduj generator tupletów symbolizujących port początkowy i końcowy. Wykonaj połączenie każdy-z-każdym
2. Wyeliminuj z powyższego generatora połączenie z portu do tego samego portu
3. Ponieważ połączenie z A do B dubluje się z połączeniem z B do A - wygeneruj możliwe połączenia krajowe pomijając takie zdublowane trasy.
4. Policz ilość generowanych połączeń w krokach 1,2,3. W tym celu napisz pętlę for, która: wyświetli wygenerowane wartości i policzy je'''