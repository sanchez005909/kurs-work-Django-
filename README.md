# kurs-work-Django-
1) Установить виртуальное окружение
2) Установка зависимостей  pip install -r requirements.txt
3) Создать базу данных с названием "newsletters"
4) Принять миграции python3 manage.py migrate
5) Загрузить данные в базу данных  python3 manage.py loaddata data.json
6) Запуск сервера: python3 manage.py runserver



Для запуска рассылки иcпользовать команду: 
python manage.py crontab add

Для рассылки вручную:
python manage.py start_mailing
