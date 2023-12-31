# Тестовое задание для Простых Решений

## Описание
Реализация Django + Stripe API бэкенда с указанным функционалом и условиями.

## Функционал
- Django Модель Item с полями (name, description, price)
- API с двумя методами:
  - `GET /buy/{id}` - для получения Stripe Session Id для оплаты выбранного Item. Выполняет запрос stripe.checkout.Session.create(...) с использованием python библиотеки stripe и возвращает полученный session.id.
  - `GET /item/{id}` - для получения простейшей HTML страницы с информацией о выбранном Item и кнопкой Buy. При нажатии на кнопку Buy происходит запрос на `/buy/{id}`, получение session_id и далее с помощью JS библиотеки Stripe происходит редирект на Checkout форму `stripe.redirectToCheckout(sessionId=session_id)`.

## Выполненные бонусные задачи
- Запуск через Docker, размещение на сервер через github workflow
- Использование переменных среды
- Просмотр Django Моделей в Django Admin панели
- Запуск приложения на удаленном сервере для тестирования