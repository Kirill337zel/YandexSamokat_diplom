# Кирилл Гологанов, 27-я когорта — Дипломный проект. Инженер по тестированию плюс

import sender_stand_request
import data

#Автотест
def test_get_order_info_by_track():
    track_number = sender_stand_request.create_order(data.order_body).json()['track']
    response = sender_stand_request.get_order_info_by_track(track_number)
    assert response.status_code == 200