import configuration
import requests

# Создание заказа
def create_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                         json=order_body)

# Получение заказа по его треку
def get_order_info_by_track(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_INFORMATION + str(track_number))