DB

sudo -u postgres psql postgres
create user postgres with password 'postgres';
alter role postgres set client_encoding to 'utf8';
alter role postgres set timezone to 'Europe/Moscow';
create database postgres owner postgres;
alter user postgres createdb;

PROJECT DOCKER-COMPOSE

docker-compose up
docker-compose run web /usr/local/bin/python manage.py makemigrations post
docker-compose run web /usr/local/bin/python manage.py migrate
docker-compose run web /usr/local/bin/python manage.py createsuperuser
login: admin
email: admin@admin.ru
password: admin

Задание: Реализовать REST API для системы комментариев блога. 
------ 
Функциональные требования: 
У системы должны быть методы API, которые обеспечивают 
- Добавление статьи (Можно чисто номинально, как сущность, к которой крепятся комментарии).
-- Комментарий: /create
- Добавление комментария к статье.
-- Комментарий: /comment
- Добавление коментария в ответ на другой комментарий (возможна любая вложенность).
-- Комментарий: /comment
- Получение всех комментариев к статье вплоть до 3 уровня вложенности.
-- Комментарий: /level_max/<int:pk>/<int:pk_sub>
- Получение всех вложенных комментариев для комментария 3 уровня.
-- Комментарий: /level_comments/<int:pk>
- По ответу API комментариев можно воссоздать древовидную структуру.
-- Комментарий: Реализовано

Нефункциональные требования: 
- Использование Django ORM.
-- Комментарий: Реализовано
- Следование принципам REST.
-- Комментарий: Реализовано
- Число запросов к базе данных не должно напрямую зависеть от количества комментариев, уровня вложенности.
-- Комментарий: Реализовано
- Решение в виде репозитория на Github, Gitlab или Bitbucket.
-- Комментарий: Реализовано
- readme, в котором указано, как собирать и запускать проект. Зависимости указать в requirements.txt либо использовать poetry/pipenv.
-- Комментарий: Реализовано
- Использование свежих версий python и Django.
-- Комментарий: Реализовано

Будет плюсом: 
- Использование PostgreSQL.
-- Комментарий: Реализовано
- docker-compose для запуска api и базы данных.
-- Комментарий: Реализовано 
- Swagger либо иная документация к апи.

Всё остальное (авторизация, админки, тесты) - по желанию, оцениваться не будет