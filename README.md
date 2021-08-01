DB <br>

sudo -u postgres psql postgres <br>
create user postgres with password 'postgres'; <br>
alter role postgres set client_encoding to 'utf8'; <br>
alter role postgres set timezone to 'Europe/Moscow'; <br>
create database postgres owner postgres; <br>
alter user postgres createdb; <br>

PROJECT DOCKER-COMPOSE <br>

docker-compose up <br>
docker-compose run web /usr/local/bin/python manage.py makemigrations post <br>
docker-compose run web /usr/local/bin/python manage.py migrate <br>
docker-compose run web /usr/local/bin/python manage.py createsuperuser <br>
login: admin <br>
email: admin@admin.ru <br>
password: admin <br>

Задание: Реализовать REST API для системы комментариев блога. 
------ 
Функциональные требования: 
У системы должны быть методы API, которые обеспечивают 
- Добавление статьи (Можно чисто номинально, как сущность, к которой крепятся комментарии). <br>
-- Комментарий: /create
- Добавление комментария к статье. <br>
-- Комментарий: /comment
- Добавление коментария в ответ на другой комментарий (возможна любая вложенность). <br>
-- Комментарий: /comment
- Получение всех комментариев к статье вплоть до 3 уровня вложенности. <br>
-- Комментарий: /level_max/<int:pk>/<int:pk_sub>
- Получение всех вложенных комментариев для комментария 3 уровня. <br>
-- Комментарий: /level_comments/<int:pk>
- По ответу API комментариев можно воссоздать древовидную структуру. <br>
-- Комментарий: Реализовано

Нефункциональные требования: 
- Использование Django ORM. <br>
-- Комментарий: Реализовано
- Следование принципам REST. <br>
-- Комментарий: Реализовано
- Число запросов к базе данных не должно напрямую зависеть от количества комментариев, уровня вложенности. <br>
-- Комментарий: Реализовано
- Решение в виде репозитория на Github, Gitlab или Bitbucket. <br>
-- Комментарий: Реализовано
- readme, в котором указано, как собирать и запускать проект. Зависимости указать в requirements.txt либо использовать poetry/pipenv. <br>
-- Комментарий: Реализовано
- Использование свежих версий python и Django. <br>
-- Комментарий: Реализовано

Будет плюсом: 
- Использование PostgreSQL. <br>
-- Комментарий: Реализовано
- docker-compose для запуска api и базы данных. <br>
-- Комментарий: Реализовано 
- Swagger либо иная документация к апи.

Всё остальное (авторизация, админки, тесты) - по желанию, оцениваться не будет