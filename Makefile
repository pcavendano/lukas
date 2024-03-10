.PHONY:rs
rs:
	poetry run python -m core.manage runserver

.PHONY: migrations
migrations:
	poetry run python -m core.manage makemigrations

.PHONY: show
showmigrations:
	poetry run python -m core.manage showmigrations

.PHONY:migrate
migrate:
	poetry run python -m core.manage migrate

.PHONY:superuser
superuser:
	poetry run python -m core.manage createsuperuser