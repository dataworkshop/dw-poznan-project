## Podsumowanie spotkania - DW POZNAN #11 Streamlit

Dzięki wszystkim za spotkanie.  Tym razem mamy okazję zobaczyć bibliotekę Streamlit, która pozwala nam szybko wdrożyć model uczenia maszynowego bez poświęcania czasu na tworzenie całego frontendu i backendu.  Zobaczcie, jak  w szybki i bezbolesny sposób można przejść od modelu do prezentacji. Pokazaliśmy jak tworzyć model, wyświetlać go na stronie oraz jak użyć augmentacji danych (Augmentation Data) do testowania modelu w różnych konfiguracjach.

Wszystkie przykłady oraz prezentacja  są już dostępne na naszym repozytorium GitHub:

https://github.com/dataworkshop/dw-poznan-project/tree/master/spotkania/2019-06-25

W przypadku pytania czy da się dynamicznie pokazać kod. Oczywiście jest to możliwe za pomocą metody `code` ze streramlit.

```python
st.code(open("./app.py").read(),language="python");
```

#### Uruchomienie

Aby uruchomić najpierw trenujemy nasz model, który utworzy nam model `my_model.h5` (wymagany `tensorflow`)

```
pip install -r requirements.txt
python train.py
```

Następnie możemy załadowany model

```shell
streamlit run app.py
```



#### VIDEO

[![Jak pokazać model ML, czyli użycie Streamlit do szybkiej publikacji modelu | DW POZNAN #11
](http://img.youtube.com/vi/g1AD_1rgzEA/0.jpg)](https://www.youtube.com/watch?v=g1AD_1rgzEA)

#### Kolejne spotkanie

Niedługo przedstawimy wizję projektu którą będziemy chcieli razem z wami wykonać. Każdy kto będzie miał czas może się przyłączyć :) Do zobaczenia następnym razem, a wszelkie pytania można kierować na slack.