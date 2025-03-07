# YandexSamokat_diplom
Кирилл Гологанов, 27-я когорта, Дипломный проект - Инженер по тестированию плюс

Автоматизация теста к API

Сценарий, который подготовили коллеги-тестировщики:

1. Клиент создает заказ.
2. Проверяется, что по треку заказа можно получить данные о заказе.

Шаги автотеста:

1. Выполнить запрос на создание заказа.
2. Сохранить номер трека заказа.
3. Выполнить запрос на получение заказа по треку заказа.
4. Проверить, что код ответа равен 200.

Файлы проекта YandexSamokat_diplom:

.gitignore: нужен для указания Git, какие файлы не следует отслеживать в этом репозитории.

README.md: содержит общую информацию об автоматизации теста к API дипломного проекта.

configuration.py: содержит URL тестового стенда и пути запросов, используемых в этом проекте.

data.py: содержит тело POST-запросов, которые будут использоваться в тестах.

sender_stand_request.py: содержит функции для отправки запросов (создание заказа и получение информации о заказе по треку).

order_test.py: содержит автоматизированные проверки по сценарию дипломного проекта.

Инструкции по запуску тестов.

Нужно убедиться, что в Visual Studio Code установлены:

1. Интерпретатор Python.
2. Дополнительные модули: pytest и requests.

Если какой-либо компонент отсутствует, установите его согласно документации.

Откройте терминал и перейдите в корневую папку проекта.

Для запуска тестов используйте следующую команду:

pytest test.py -v
