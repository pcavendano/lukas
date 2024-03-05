.PHONY:install
rs:
	poetry run python -m core.manage runserver

.PHONY: mmigrations
mmimgrations:
	poetry run python -m core.manage makemigrations

.PHONY:migrate
mmigrate:
	poetry run python -m core.manage migrate

.PHONY:superuser
superuser:
	poetry run python -m core.manage createsuperuser