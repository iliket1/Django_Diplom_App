# Social Network Project

## Описание

Это социальная сеть, позволяющая пользователям регистрироваться, публиковать посты, оставлять комментарии и ставить лайки.

## Требования

- Python 3.10+
- PostgreSQL
- Django 4.x
- Django REST Framework
- Python-библиотеки из `requirements.txt`

## Установка и запуск проекта

1. **Клонирование репозитория**  
git clone https://github.com/iliket1/Django_Diplom_App.git
cd social_network

2. **Создание виртуального окружения и установка зависимостей**
python -m venv venv
source venv/bin/activate  # Для macOS/Linux
venv\Scripts\activate  # Для Windows
pip install -r requirements.txt

3. **Настройка переменных окружения**
Создайте файл .env и добавьте в него:
DB_NAME=social_network
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432

4. **Применение миграций**
python manage.py makemigrations
python manage.py migrate

5. **Создание суперпользователя**
python manage.py createsuperuser

6. **Запуск сервера**
python manage.py runserver

API Эндпоинты
Метод   URL                     Описание                Требует авторизации
GET     /api/posts/             Получить все посты      ❌ Нет
POST    /api/posts/             Создать новый пост      ✅ Да
POST    /api/posts/{id}/like/   Поставить лайк          ✅ Да
POST    /api/comments/          Добавить комментарий    ✅ Да