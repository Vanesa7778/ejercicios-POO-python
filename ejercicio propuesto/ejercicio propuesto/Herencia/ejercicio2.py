
class Comida:
    def __init__(self, nombre):#se utiliza __init__ un constructor de la clase que inicializa la propiedad nombre
        self.nombre = nombre
#metodo para describir comida
    def describir(self):
        print(f"Este postre se llama {self.nombre}")
#la clase Postre hereda de la clase Comida
class Postre(Comida):
    def __init__(self, nombre, sabor):
        super().__init__(nombre)#se llama al constructor de la clase padre usando super()
        self.sabor = sabor#asigna el sabor al atributo 'sabor'

    def disfrutar(self):
        print(f"¡Disfruta el postre a sabor {self.sabor}!")

# Se crea una instancia llamada miPostre
miPostre = Postre(nombre="Tiramisu", sabor="cafe")

miPostre.describir()  # Se llama al eétodo describir de la instancia miPostre
miPostre.disfrutar()  # Se llama al metodo disfrutar de la instancia miPostre


