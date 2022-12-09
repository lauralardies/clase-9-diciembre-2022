from collections import defaultdict, OrderedDict, namedtuple

# DICCIONARIOS POR DEFECTO
d = defaultdict(float)
print(d['algo'])
print(d)

d = defaultdict(str)
print(d['algo'])
print(d)

d = defaultdict(object)
print(d['algo'])
print(d)

# DICCIONARIOS ORDENADOS
n = OrderedDict()
n['uno'] = 'one'
n['dos'] = 'two'
n['tres'] = 'three'
print(n)

n1 = {}
n1['uno'] = 'one'
n1['dos'] = 'two'
n2 = {}
n2['dos'] = 'two'
n2['uno'] = 'one'
print(n1 == n2)

n1 = OrderedDict()
n1['uno'] = 'one'
n1['dos'] = 'two'
n2 = OrderedDict()
n2['dos'] = 'two'
n2['uno'] = 'one'
print(n1 == n2)

# TUPLAS CON NOMBRE
Persona = namedtuple('Persona','nombre apellido edad sexo')
p = Persona(nombre="Laura",apellido="Rodríguez",edad=19, sexo='F')
print(p)
print(p.nombre)
print(p.edad)
print(p[0])
print(p[-1])