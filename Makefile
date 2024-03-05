.PHONY:install
rs:
	poetry run python -m core.manage runserver

.PHONY: mmigrations
mimgrations:
	poetry run python -m core.manage makemigrations

.PHONY: show
mimgrations:
	poetry run python -m core.manage showmigrations

.PHONY:migrate
migrate:
	poetry run python -m core.manage migrate

.PHONY:superuser
superuser:
	poetry run python -m core.manage createsuperuser