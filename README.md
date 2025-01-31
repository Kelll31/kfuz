kfuz
======

kfuz - скрипт для фазинга HTTP/S с возможностью вывода содержимого. Скрипт позволяет тестировать различные URL-адреса, заменяя часть URL на значения из списка слов или диапазона чисел. Это может быть полезно для поиска скрытых страниц или ресурсов на веб-сайте.


Install
-----

Убедитесь, что у вас установлен Python 3.x.

Установите необходимые зависимости:

    pip install requests

Склонируйте этот репозиторий:

    git clone https://github.com/yourusername/fuzzing-script.git
    cd fuzzing-script


Usage
-----
![2024-12-09_10-59-11](https://github.com/user-attachments/assets/7292184c-5fb2-4ac1-9b2c-3582cd8e65e4)


Запустите скрипт с необходимыми параметрами:


    python fuzzing_script.py -u <базовый_URL> [опции]

#### Обязательные аргументы

    -u, --url: Базовый URL для фазинга с точкой вставки FUZZ.

#### Опциональные аргументы

    -w, --wordlist: Путь к файлу списка слов для замены FUZZ.
    -r, --range: Диапазон чисел для замены FUZZ (например, 1-100).
    -H, --header: Пользовательский заголовок (например, "User-Agent: custom"). Можно указать несколько заголовков.
    -b, --cookie: Пользовательский файл cookie (например, "sessionid=abc123"). Можно указать несколько cookies.
    -X, --method: Используемый HTTP-метод (по умолчанию: GET).
    -sa, --show-all: Показать содержимое страницы.
    -hr, --hide-responses: Скрыть ответы с указанными кодами состояния (например, 404).

Examples
-----

Фазинг с использованием списка слов:

    python kfuz.py -u "http://example.com/FUZZ" -w wordlist.txt
    
Фазинг с использованием диапазона чисел:

    python kfuz.py -u "http://example.com/FUZZ" -r "1-100"

Использование пользовательских заголовков и cookies:

    python kfuz.py -u "http://example.com/FUZZ" -w wordlist.txt -H "User-Agent: custom" -b "sessionid=abc123"

Вывод и сортировка ответов JSON:
    
    python kfuz.py -u "http://example.com/FUZZ" -w wordlist.txt -sa -k 'id'
