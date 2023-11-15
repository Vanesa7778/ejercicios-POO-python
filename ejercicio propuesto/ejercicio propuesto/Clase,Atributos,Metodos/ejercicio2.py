# __init__ sirve para inicializar valores de una variable al crear una nueva instancia de una clase

#se define una clase llamada fruta 
class Fruta:
#se utiliza __init__ un constructor de la clase que inicializa las propiedades nombre y color
    def __init__(self,nombre,color):
        self.nombre=nombre#asigna el nombre de la fruta a la propiedad 'nombre'
        self.color=color#asigna el color de la fruta a la propiedad 'color'
#metodo para mostrar información sobre la fruta
    def mostrarInformacion(self):
        print(f"{self.nombre} es de color {self.color}")#se imprime un mensaje con el nombre y el color de la fruta
#se crea una instancia llamada miFruta
miFruta = Fruta(nombre="fresa", color="rojo")
#se llama al metodo mostrarInformacion() de la instancia "miFruta"
miFruta.mostrarInformacion()