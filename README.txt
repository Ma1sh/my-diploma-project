BACKEND
# Запуск сервера
python manage.py runserver



FRONTEND
# Установка зависимостей
npm install

# Запуск dev-сервера
npm run dev

# Сборка для продакшена
npm run build

# Предпросмотр собранного проекта
npm run preview


Если не работает надо установить Note.js

# Перейди в папку бэкенда
cd C:\Users\Имя\Desktop\твой-проект\backend

# Создай виртуальное окружение (один раз)
python -m venv venv

# Активируй его
venv\Scripts\activate

# Установи зависимости
pip install -r requirements.txt

# Примени миграции
python manage.py migrate

# Запусти Django
python manage.py runserver


cd C:\Users\Имя\Desktop\твой-проект\frontend

# Установи зависимости (может занять время)
npm install

# Запусти Vue
npm run dev
