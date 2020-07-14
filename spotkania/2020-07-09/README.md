

## Podsumowanie spotkania - DW POZNAN #12 Projekt #2

## VIDEO

[![Autonomiczny pojazd - Projekt #2 | DW Poznań](http://img.youtube.com/vi/KEqKid9rXoM/0.jpg)](https://youtu.be/KEqKid9rXoM?list=PLa8KbhSQZVUhFsfa2Por7p10Oo8LKoBmD)

### Prezentacja

[DWPOZNAN12_PROJEKT2.pdf](https://github.com/dataworkshop/dw-poznan-project/blob/master/spotkania/2020-07-09/DWPOZNAN12_PROJEKT2.pdf)

![./assets/elegoo.png](./assets/model.png)

### Podsumowanie:

Dzięki wszystkim za spotkanie.  Tym razem mieliśmy wstęp do nowego projektu który dotyczył autonomicznego pojazdu. Nauczyliśmy się na nim

* Czym jest autonomiczny pojazd
* Poznaliśmy ARDUINO UNO na przykładowym zestawie ELEGOO Robot Kit 3.0
* Zaprogramowaliśmy jeżdzenie samochodem, odczytywanie sensorów oraz komunikację przez IRDA oraz przez symulator.
* Zaprogramowaliśmy prosty model SVM i wyeksportowaliśmy go przy pomocy biblioteki **micromlgen** https://github.com/eloquentarduino/micromlgen/tree/master/micromlgen do C++ by móc go użyć przez nasz model
* Utworzyliśmy prosty dwuwarstwowy model Tensorflow którego nauczyliśmy i przekonwertowaliśmy używając wag perceptronu, funkcji aktywacji relu oraz softmax w C++ do naszego modelu.

#### Co następnym razem?

Osoby chętne do udziału w projekcie mogą zgłaszać się na slacku naszego poznańskiego zespołu (jeśli nie masz poproś mnie na maila). Aktualne zadania na projektu to:

* Przyjrzymy się symulatorowi CARLA oraz AirSIM
  * Symulator AirSim Microsoftu; [https://github.com/Microsoft/AirSim](https://github.com/Microsoft/AirSim)
  * Symulator CARLA : [https://carla.org/](https://carla.org/) (https://www.youtube.com/playlist?list=PLQVvvaa0QuDeI12McNQdnTlWz9XlCa0uo)
* Przyjrzymy się kilku datasetom które zostały udostępnione do uczenia maszynowego

  * UDACITY :[https://github.com/udacity/self-driving-car](https://github.com/udacity/self-driving-car)
  * AUDI Autonomous dataset: [https://www.infoq.com/news/2020/04/audi-autonomous-driving/](https://www.infoq.com/news/2020/04/audi-autonomous-driving/)



#### Uruchomienie

* Musimy mieć tensorflow w wersji co najmniej 2.0

```python
pip install tensorflow
pip install jupyterlab

jupter lab
```

* `train_model.ipynb` - Uczenie modelu SVM oraz tensorflow
* `car_obstacle_train` - Główny katalog projektu ARDUINO
  * `car_obstacle_train.ino` - Główny plik ARDUINO do modelu samochodu
  * `engine.h` - Sterowanie silnikiem
  * `model.h` - Model Tensorflow w postaci pliku
  * `obstacle_model_classes.h` - pomocna liczba klas poleceń
  * `obstacle_model_svm.h` - model SVM dla naszego modelu
  * `remote.h` - obsługa pilota IRDA oraz wejścia z klawiatury dla naszego modelu
  * `sensors.h` - odczyt sensorów takich jak odległości, lewy, środkowy i prawy czujnik czarnej linii, dioda.

