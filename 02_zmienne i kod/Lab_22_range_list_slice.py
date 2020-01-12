'''Budujesz moduł generujący wykresy. 
Chcesz samodzielnie wpływać na to, jakie kolory będą wykorzystane na wykresie. 
Definiujesz na początku listę kolorów:
["red", "orange", "green", "violet", "blue", "yellow"]
Czasami na wykresie będą prezentowane tylko 3 kategorie i wtedy chcesz wykorzystać tylko 3 pierwsze kolory, 
innym razem wykres ma mieć 5 kategorii i potrzebujesz listę 5 kolorów.
Napisz funkcję, która przyjmuje dwa argumenty: listę kolorów i liczbę n. 
Funkcja ma zwracać nową kopię listy kolorów o długości n korzystając z przekazanej listy argumentów.'''

colors = ["red", "orange", "green", "violet", "blue", "yellow"]

def colorlist(list,n_val):
    return list[:n_val]

new_colors = colorlist(colors,2)
print(new_colors)

'''Napisz pętlę, która wygeneruje wszystkie możliwe zestawy kolorów dostępne w liście. 
Pętla powinna radzić sobie z wyświetleniem wszystkich zestawów, 
nawet jeżeli do początkowej listy zostanie kiedyś dodany następny kolor 
(nie korzystaj z wpisywania na stałe wartości liczbowej).'''

for i in range (len(colors)):
    print(colors[:i+1])

'''Napis też można "kroić". Wytnij z poniższego tekstu pochodzącego z 
https://nonsa.pl/wiki/Korporacja (dawniej nonsensopedia.pl) fragment tłumaczący pochodzenie słowa 
"Korporacja" - fragment znajduje się w nawiasach (same nawiasy pomiń):
Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) 
– organizacja, która pod przykrywką prowadzenia biznesu włada dzisiejszym światem. 
Wydawać się może utopijnym miejscem realizacji pasji zawodowych. 
W rzeczywistości jednak nie jest wcale tak kolorowo. 
Korporacja służy do wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli. '''

 
 
definition = 'Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja, która pod przykrywką prowadzenia biznesu włada dzisiejszym światem. Wydawać się może utopijnym miejscem realizacji pasji zawodowych. W rzeczywistości jednak nie jest wcale tak kolorowo. Korporacja służy do wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli. '
 
print(definition[definition.index('(')+1:definition.index(')')])