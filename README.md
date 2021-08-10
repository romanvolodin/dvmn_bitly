# Считаем клики по ссылкам

Скрипт позволяет быстро сократить длинную ссылку с помощью сервиса [Bitly](https://bitly.com/).
Для коротких ссылок показывает количество переходов за всё время.

## Требования

Для запуска вам понадобится Python 3.6 или выше.

Необходимо получить ключ для доступа к API Bitly. Подробная инструкция [как получить ключ](https://dev.bitly.com/).

## Переменные окружения

Настройки проекта берутся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `bitly.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступные переменные:

- `BITLY_TOKEN` — ключ для доступа к API Bitly. 

Пример:

```env
BITLY_TOKEN=2496bf54e82920wr3478f1ce7b58221d8d6
```

## Запуск

Скачайте код с GitHub. Установите зависимости:

```sh
pip install -r requirements.txt
```

Запустите скрипт:

```sh
python bitly.py
```

Примеры вывода:
```sh
$ python bitly.py
Enter an url: https://dvmn.org/modules/web-api/lesson/bitly/
https://bit.ly/3g6w5Er
```
```sh
$ python bitly.py
Enter an url: https://bit.ly/3g6w5Er
18
```

## Цели проекта

Код написан в учебных целях — для курса по Python на сайте [Devman](https://dvmn.org).