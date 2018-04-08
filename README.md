# Ближайшие бары

Скрипт позволяет найти самый большой и самый маленький бары а так же по введенным в консоль координатам покажет ближайший бар.

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5
Так же необходимо установить модуль geopy для нахождения расстояния между барами по координатам
Запуск на Linux:

```bash
$ pip install geopy 
$ python bars.py # possibly requires call of python3 executive instead of just python

The biggest bar is: Спорт бар «Красная машина»
The smallest bar is: БАР. СОКИ
The closest bar is: Таверна

```
Вывод:
```bash
The biggest bar is: Спорт бар «Красная машина»
The smallest bar is: БАР. СОКИ
The closest bar is: Таверна

```
Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
