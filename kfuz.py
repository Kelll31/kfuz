import requests
import argparse

def fuzz_url(base_url, wordlist=None, range_numbers=None, headers=None, cookies=None, method='GET', show_all=False, hide_responses=None):
    if 'FUZZ' not in base_url:
        raise ValueError("Базовый URL должен содержать точку вставки 'FUZZ'.")

    if wordlist:
        with open(wordlist, 'r') as f:
            paths = f.read().splitlines()
    elif range_numbers:
        start, end = map(int, range_numbers.split('-'))
        paths = [str(i) for i in range(start, end + 1)]
    else:
        raise ValueError("Необходимо указать либо список слов, либо диапазон.")

    for path in paths:
        url = base_url.replace('FUZZ', path)
        try:
            response = requests.request(method, url, headers=headers, cookies=cookies)
            if hide_responses and response.status_code in hide_responses:
                continue
            print(f"URL: {url} | Код: {response.status_code}")
            if show_all:
                print(response.text)
        except requests.RequestException as e:
            print(f"Ошибка с URL {url}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Скрипт для фазинга веб-страниц.")
    parser.add_argument('-u', '--url', required=True, help='Базовый URL для фазинга с точкой вставки FUZZ')
    parser.add_argument('-w', '--wordlist', help='Путь к файлу списка слов')
    parser.add_argument('-r', '--range', help='Диапазон чисел (например, 1-100)')
    parser.add_argument('-H', '--header', action='append', help='Пользовательский заголовок  (например, "User-Agent: custom")')
    parser.add_argument('-b', '--cookie', action='append', help='Пользовательский файл cookie (например, "sessionid=abc123")')
    parser.add_argument('-X', '--method', default='GET', help='Используемый HTTP-метод (по умолчанию: GET)')
    parser.add_argument('-sa', '--show-all', action='store_true', help='Показать содержимое страницы')
    parser.add_argument('-hr', '--hide-responses', type=int, nargs='+', help='Скрыть ответы с этими кодами состояния')

    args = parser.parse_args()

    headers = {h.split(':')[0]: h.split(':')[1].strip() for h in args.header} if args.header else None
    cookies = {c.split('=')[0]: c.split('=')[1] for c in args.cookie} if args.cookie else None

    fuzz_url(
        base_url=args.url,
        wordlist=args.wordlist,
        range_numbers=args.range,
        headers=headers,
        cookies=cookies,
        method=args.method,
        show_all=args.show_all,
        hide_responses=args.hide_responses
    )

if __name__ == "__main__":
    main()