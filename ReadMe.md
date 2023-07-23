# Интернет-магазин MEGANO

MEGANO - это проект, написанный на языке Python с использованием фреймворка Django.

## Структура проекта
### Проект состит из следующих частей
1. Приложения:
 - `cart` - приложение корзины товаров пользователя с возможностью добавления и удаления товаров, а так же изменения количества.
 - `orders` - приложение заказов. Содержит сервисы оформления заказа, оплаты, просмотра истории заказов;
 - `products` - приложение товаров магазина. Содержит сервисы просмотра товапров, фильтрации и сортировки, а так же добавления отзывов к товару;
 - `profile` - приложение пользователя. Содержит сервисы регистрации, login/logout, смены пароля, а так же личный кабинет пользователя;
2. Документация:
 - `ReadMe.md` - Описание проекта;
 - `requirements.txt` - Подключение зависимостей;

## Установка проекта
Для установки исходника интернет магазина необходимо клонировать репозиторий из GitHub или ввести следующую команду:
```
https://github.com/Khamer-Ivan/Online-Store_Django.git
```
Чтобы проект работал корректно, необходимо установить зависимости командой:
```
git install -r requirements.txt
```
Далее необходимо создать суперюзера для доступа к админ-панели
```
python manage.py createsuperuser
```
Теперь можно запустить сервер, введя команду
```
python manage.py runserver
```

Вы попадёте в главное меню магазина и сможете пользоваться всем интерфейсом.

