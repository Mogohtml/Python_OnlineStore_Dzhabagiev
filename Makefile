# For docker-compose
# Команда для запуска контейнера
up:
	docker-compose up --build

# Команда для остановки контейнера
down:
	docker-compose down

# Команда для выполнения произвольной команды в контейнере
exec:
	docker-compose exec ${SS} python manage.py ${CMD}

# Команда для создания суперпользователя
createsuperuser:
	docker-compose exec web python manage.py createsuperuser

# Команда для выполнения миграций
migrate:
	docker-compose exec web python manage.py migrate

# Команда для выполнения тестов
test:
	docker-compose exec web python manage.py test


# For Dockerfile
