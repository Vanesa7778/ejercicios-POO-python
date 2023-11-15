# Consulte un ejemplo donde se implemente la herencia

class Bebida:
    def __init__(self,nombre,precio):# __init__ es un constructor de la clase que inicializa las propiedades nombre y precio
        self.nombre=nombre# asigna el nombre al atributo 'nombre'
        self.precio=precio#asigna el precio al atributo 'precio'
# se define la clase Gaseosa que hereda de la clase Bebida
class Gaseosa(Bebida):
    def __init__(self,nombre,precio,sabor):
        super().__init__(nombre,precio)# se llama al constructor de la clase padre usando super()
        self.sabor= sabor#asigna el sabor al atributo 'sabor'
#se crea una instancia de la clase Gaseosa llamada "refresco"
refresco = Gaseosa ("coca-cola",2500,"dulce")
#se imprime informacion sobre la bebida, incluyendo nombre y precio
print(f"Bedida:{refresco.nombre}-Precio:${refresco.precio}")
#se imprime el sabor de la gaseosa
print(f"Sabor:{refresco.sabor}")