## Opis

Spotkaliśmys się 17-go grudnia 2019 w strefie nauki i pracy galerii Malta: http://galeriamalta.pl/strefa-nauki-i-pracy-2420/, o godzinie: 18:30 - 19:30. Agenda:

* **Algorytmy Ewaluacji**
* **Cosine Similarity i Mise en Scene**
* **Collaborative Filtering**
* **Algorytmy SVD**

Prezentacja ze spotkania jest dostępna w pliku: **DW Poznań - projekt filmweb-rekomendacje #4**

## Notatka

Dziękuje jeszcze raz za udział w spotkaniu, oraz przygotowanie przentacji przez Pawła oraz Krzysztofa. Cały kod dostępny jest w Google Colab pod adresem:

**https://colab.research.google.com/drive/16Jfvhe_viHdFVq9QAlbO29LCVNNpyvxz**

a także w repozytorium GitHub:

https://github.com/dataworkshop/dw-poznan-project/tree/master/spotkania/2019-12-17

Cała prezentacja notomiast można znaleść pod adresem: http://bit.ly/2LWGi6X albo w postaci pdf w wyżej wymienionym repozytorium. 

Tym razem opowiadaliśmy o algorytmach rekomendacji i opisaliśmy kilka najważniejszych które są używane. Mam nadzieje że się podobało :) , i że niedługo będziemy mogli udostępnić filmik z niego jak i poprzednich.

Kolejne spotkanie odbędzie się już w nowym roku, drugi tydzień stycznia, najprawdopodobnie 14-go stycznia. Poniżej kolejne zadania w naszym projekcie

* **Przetestowanie algorytmów rekomendacji** - potrzebujemy przetestować i sprawdzić omawiane podczas prezentacji algorytmy, oraz wybrać najlepszy albo może połączyć kilka algorytmów w jeden wspólny algorytm. W plku `data_static/filmweb_exmaple_final.csv` znajduje się przykładowy użytkownik.

  * Przetestowanie **Cosine Similarity i Mise En Scene** - utworzenie metody która dla naszego użytkownika z pliku wytorzy rekomendacje, a także przetestowanie za pomocą ewaluacji z prezentacji
  * Przetestowanie **Collaborative Filtering** - j/w
  * Przetestowanie **SVD** i **SVDpp** - j/w
  * Zebranie i zestawienie algorytmów i wybranie najlepszego
  * Utworzenie Flaska do najlepszej metody
  * Utworenie widoku dla Rekomendacji dla użytkownika

* **Wykresy** - Poprawa UX wykresów i dodanie nowych. Możliwe wykresy
  * Dashborad - czyli zestawienie kilku wykresów na jednym ekranie z najważniejszymi informacji, ulubione filmy, najbardziej lubiane gatunki, najbardziej lubiani aktorzy, najmniej lubiani aktorzy, ilość ocen, średnie oceny na najważniejsze gatunki i porównanie z imdb, itp... Tego typu małych wykresów może sporo
  * Zestawienie czasowe jak bardzo lubimy dane gatunki, jak zmieniał nam się gust
  * Zestawienia ze zdjęciami aktorów jak bardzo popularni byli w danym czasie, na Isi x czas na y, nasza średnia ocena, i weilkość zdjęcia aktora to ilość ocen jaką daliśmy.
  * inne pomysły :) Nie wszystkie znajdą się w końcowym produkcie ale część z nich może być naprawdę ciekawa
  
  

Jeszcze raz, dzięki wszystkim za udział w spotkaniu :) i do zobaczenia już w nowym roku.