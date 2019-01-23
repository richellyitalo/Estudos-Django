# Venv
## Ativar ambiente
`python -m venv ./venv`

## Entrar no ambiente
`./venv/Scripts/activate.bat`

## Sair do ambiente
`deactivate`

## Ver pacotes
`pip freeze`

## Salvar pacotes instalados
`pip freeze > pacotes.txt`

## Instalar Django
`pip install django`

## Criar Projeto
`django-admin startproject PROJECTNAME .`

## Executar Server
`python manage.py runserver`

## Criar App
`python manage.py start app APPNAME`


# Registrando novo App
## Registrando classe
Nos `settings.py` do APP principal, adicione ao INSTALLED_APPS `NOMEAPP.apps.CLASSE` (pages.apps.PagesConfig)
