from saludos import *
from text.saludos import Saludo
from text.hola.saludos import Saludo
from text.adios.despedidas import Despedida

saludo = Saludo('Juan')
saludo.saludar()

d = Despedida('Juan')
d.despedir()