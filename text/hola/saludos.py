class Saludo():

    def __init__(self, nombre):
        self.nombre = nombre
    
    def saludar(self):
        print('Hola soy ', self.nombre)

def saludar():
    print("Hola, te estoy saludando desde la función saludar() " \
            "del módulo saludos")
