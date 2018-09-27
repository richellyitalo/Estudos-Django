## Instalação do virtualenv
`pip install virtualenv`

## Cria ambiente
`virtualenv venv`

## Ativando ambiente
`.\venv\scripts\activate`

## Saind do ambiente
`deactivate`

## Salvar pacotes instalados
`pip freeze > pacotes.txt`

# Executando no Powershell

`Set-ExecutionPolicy AllSigned`

Agora o comando pode ser executado
`.\venv\scripts\activate.ps1` ps1 de powershell

## Instalando o *mkvirtualenv*
`pip install virtualenvwrapper-win`  
Auxiliador na criação de ENVS.  
Ele mantém todas as envs no mesmo local, por padrão em `%USERPROFILE%\Envs`  
[https://pypi.org/project/virtualenvwrapper-win/](https://pypi.org/project/virtualenvwrapper-win/)
