build_requirement:
	poetry export -f requirements.txt --output requirements.txt

run:
	docker-compose up -d

run_build:
	docker-compose up -d --build

restart:
	docker-compose restart

migrate:
	docker-compose exec web python manage.py migrate

collectstatic:
	docker-compose exec web python manage.py collectstatic --no-input

create_superuser:
	docker-compose exec web python manage.py createsuperuser
