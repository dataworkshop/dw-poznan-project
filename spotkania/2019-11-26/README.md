## Opis

Spotkaliśmys się 26-go listopadą w strefie nauki i pracy galerii Malta: http://galeriamalta.pl/strefa-nauki-i-pracy-2420/, o godzinie: 18:30 - 20:30. Agenda:

* **Chrome Extension** - Czyli jak rozszerzyć stronę filmweb o nowe możliwości 
* **Flask Server** - Jak przekazywać dane chrome extension do serwera 
* **IMDB** - Jak z naszych wcześniejszych spotkań stworzyć narzędzie do łączenia dwóch różnych baz danych. 
* **Wykresy** - Jak pokazać użytkownikowi przy pomocy `chart.js` pokazaż interesujące wykresy 

Prezentacja ze spotkania jest dostępna w pliku: **DW Poznań - projekt filmweb-rekomendacje #3**

### Video 

Przetwarzanie danych z filmweb cz. IV | Jak zbudować Chrome Extension i serwer Flask | DW Community
[![Przetwarzanie danych z filmweb cz. I | DW Community](http://img.youtube.com/vi/0zfvVfynYUA/0.jpg)](http://www.youtube.com/watch?v=0zfvVfynYUA)


## Notatka

Dziękuje wszystkim za udział w spotkaniu, Mateuszowi za pokazanie i pracę przy projekcie oraz Krzystofowi za pomoc przy analizie danych. 

Repozytorium jest dostępne na GitHub: https://github.com/alexiej/filmweb-rekomendacje

Filmik ze spotkanie razem z poprzednim zostanie udostępniony niedługo. Aktualnie projekt przeszedł już drugi Milestone w którym zbudowaliśmy już działające rozszerzenie chrome, trochę wykresów i pozostała ostatnia część naszego projektu czyli system rekomendacji. Spotkamy się ponownie za dwa tygodnie ale w tym czasie mamy wiele do zrobienia. 

Zadania dostępne są w https://github.com/dataworkshop/dw-poznan-project/projects/3s

* **TRAVIS** - Była już mowa o testowaniu aplikacji. Przydałoby się dodać testy do naszej biblioteki, chodzi o testy do bibliotek `filmweb_integrator` oraz `movies_analyzer` 
* **Wykresy** - Poprawa UX wykresów i dodanie nowych. Możliwe wykresy
  * Dashborad - czyli zestawienie kilku wykresów na jednym ekranie z najważniejszymi informacji, ulubione filmy, najbardziej lubiane gatunki, najbardziej lubiani aktorzy, najmniej lubiani aktorzy, ilość ocen, średnie oceny na najważniejsze gatunki i porównanie z imdb, itp... Tego typu małych wykresów może sporo
  * Zestawienie czasowe jak bardzo lubimy dane gatunki, jak zmieniał nam się gust
  * Zestawienia ze zdjęciami aktorów jak bardzo popularni byli w danym czasie, na Isi x czas na y, nasza średnia ocena, i weilkość zdjęcia aktora to ilość ocen jaką daliśmy.
  * inne pomysły :) Nie wszystkie znajdą się w końcowym produkcie ale część z nich może być naprawdę ciekawa
* **Surprise** - Rekomendacje na podstawie danych IMDB. Tutaj częścią zajmuje się Krzystof, ale można mu pomóc i podzielić się i spróbować różnych metod i wskażników do rekomendacji. Niech za źródło będzie zestaw ocen przygotowany przez IMDB 
  https://www.imdb.com/interfaces/ oraz https://grouplens.org/datasets/movielens/100k/
* **Poprawki do Integracja Danych** - Nasze łączenie przez IMDB nie jest doskonałe i wiele filmów nie zostaje powiązanych. Można byłoby poprawić ładowanie danych
