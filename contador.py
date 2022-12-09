from collections import Counter

l = [1,2,3,4,1,2,3,1,2,1]
c = Counter(l)
print(c)
Counter({1: 4, 2: 3, 3: 2, 4: 1})
Counter('palabra')
Counter({'a': 3, 'b': 1, 'l': 1, 'p': 1, 'r': 1})
c = Counter('palabra')
print(c)
animales = "gato perro canario perro canario perro"
c = Counter(animales.split())
Counter({'gato': 3, 'perro': 2, 'canario': 1})
print(c.most_common(1))  # Primeros elementos más repetidos
print(c.most_common(2))  # Primeros dos elementos más repetidos
print(c.most_common())   # Elementos ordenadores por repeticiones

l = [10,20,30,40,10,20,30,10,20,10]
c = Counter(l)

print(c.items())        # Registros del contador por clave-valor
print(c.keys())         # Registros del contador por clave
print(c.values())       # Registros del contador por valor

print(sum(c.values()))  # Suma total de elementos del contador

print(list(c))          # Conversión a lista
print(dict(c))          # Conversión a conjunto
print(set(c))           # Conversión a conjunto

