from collections import defaultdict, OrderedDict

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
