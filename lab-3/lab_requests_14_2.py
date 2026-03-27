import requests
import random

def send_requests():
    url = 'http://127.0.0.1:5000/number/'

    print("\nЗапросы:")

    # Отправка GEt-запроса
    param = random.randint(1, 10)
    get_response = requests.get(
        url,
        params={'param': param}
    ).json()

    # Запись первого числа
    number_1 = get_response['result']
    print("GET-запрос:", get_response)

    # Отправка POST-запроса
    json_param = random.randint(1, 10)
    post_response = requests.post(
        url,
        json={'jsonParam': json_param},
        headers={'Content-Type': 'application/json'}
    ).json()

    # Запись первой операции и второго числа
    operation_1 = post_response['operation']
    number_2 = post_response['result']
    print("POST-запрос:", post_response)

    # Отправка DELETE-запроса
    delete_response = requests.delete(url).json()

    # Запись второй операции и третьего числа
    operation_2 = delete_response['operation']
    number_3 = delete_response['result']
    print("DELETE-запрос:", delete_response)

    print()
    print("Получившееся выражение:")

    # Составление выражения из параметров
    expression = f'{number_1} {operation_1} {number_2} {operation_2} {number_3}'

    # Замена функций на символы
    expression = expression.replace("sum", "+")
    expression = expression.replace("sub", "-")
    expression = expression.replace("mul", "*")
    expression = expression.replace("div", "/")

    # Вычисление при помощи eval()
    print(f'{expression} = {int(eval(expression))}')

if __name__ == "__main__":
    send_requests()
