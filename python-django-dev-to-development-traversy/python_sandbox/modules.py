# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules
import datetime
from datetime import date

# time
import time
from time import time as t

# módulo customizado
import validator
from validator import validate_email

# módulo instalado via pip3
import camelcase
from camelcase import CamelCase

today = date.today()
today_datetime = datetime.date.today()

timestamp = time.time()
timestamp_t = t()

email = 'rijel@email.com'

# if validate_email(email):
if validator.validate_email(email):
    print('email válido')
else:
    print('email inválido')

# camel case
camel = CamelCase()
nome = 'rijelly toaster'
nome_cameled = camel.hump(nome)
print(nome_cameled)
