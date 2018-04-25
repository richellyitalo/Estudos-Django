# django

## Alterar tabela
Mude seus modelos (em models.py).
Rode python 'manage.py makemigrations' para criar migrações para suas modificações
Rode python 'manage.py migrate' para aplicar suas modificações no banco de dados
*EXTRA: 'python manage.py sqlmigrate polls 0001' para visualizar o sql

## shell do python
```python manage.py shell```

## criar super usuário
```python manage.py createsuperuser```

## iniciar o server
```python manage.py runserver```

## salvando sem race conditions
from django.db.models import F
registro.votos = F('votos') + 1