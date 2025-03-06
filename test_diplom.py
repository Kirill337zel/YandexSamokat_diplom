# Кирилл Гологанов, 27-я когорта — Дипломный проект. Инженер по тестированию плюс

import configuration
import data
import requests

# Создание заказа
def create_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                         json=order_body)

# Получение заказа по номеру трекера
def get_order_info_by_track(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_INFORMATION + str(track_number))

# Автотест
def test_order_creation_and_return():
    response = create_order(data.order_body)
    track_number = response.json()["track"]
    print("Заказ создан. Номер трека:", track_number)

# Получение данных заказа по треку
    order_response = get_order_info_by_track(track_number)
    assert order_response.status_code == 200
    order_data = order_response.json()
    print("Данные заказа:")
    print(order_data)