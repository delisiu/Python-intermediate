'''Na przekręcie z wpłatomatem z poprzedniego zadania postanawiasz wraz ze swoim szefem 
otworzyć linie lotnicze "Flying Python". Linie będą krajowe. Oto wykaz portów lotniczych:
    ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
             'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']
1. Zbuduj listę tupletów symbolizujących port początkowy i końcowy. Wykonaj połączenie każdy-z-każdym'''

ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
             'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']
ports_list1 = [(a,b) for a in ports for b in ports]
print(ports_list1)

'''2. Wyeliminuj z powyższej listy połączenie z portu do tego samego portu'''

ports_list2 = [(a,b) for a in ports for b in ports if a != b]
print(ports_list2)
print("-"*30)

'''3. Ponieważ połączenie z A do B dubluje się z połączeniem z B do A 
- wygeneruj możliwe połączenia krajowe pomijając takie zdublowane trasy.'''

ports_list3 = [(a,b) for a in ports for b in ports if a < b]
print(ports_list3)
print("-"*30)

'''4. Policz ilość generowanych połączeń w krokach 1,2,3'''

print("Ilość połączeń w kroku 1:",len(ports_list1))
print("Ilość połączeń w kroku 1:",len(ports_list2))
print("Ilość połączeń w kroku 1:",len(ports_list3))