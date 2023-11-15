class Perro:
    def __init__(self,nombre,edad):#un constructor de la clase que inicializa las propiedades nombre y edad
        self.nombre=nombre #asigna el nombre de persona a la propiedad 'nombre'
        self.edad=edad#asigna edad de persona  a la propiedad 'edad'
#metodo para simular la accion de sentarse
    def sentarse(self):
        print(f"{self.nombre} esta sentado")
#metodo para simular la accion de rodar 
    def rodar(self):
        print(f"{self.nombre} esta rodando en el piso")

#se crea una instancia de la clase Perro llamada "miPerro"
miPerro= Perro(nombre="willy", edad= 5)
#se imprime un mensaje que muestra el nombre y la edad del perro
print(f"mi perro se llama {miPerro.nombre} y tiene {miPerro.edad} años de edad ")
#llama al metodo sentarse() de la instancia mi perro
miPerro.sentarse()
#llama al metodo roda() de la instancia mi perro
miPerro.rodar()