class Persona:
##se utiliza __init__ un constructor de la clase que inicializa las propiedades nombre y edad
    def __init__(self,nombre,edad):
        self.nombre=nombre#asigna el nombre de persona a la propiedad 'nombre'
        self.edad=edad#asigna edad de persona  a la propiedad 'edad'
#metodo para imprimir un mensaje de presentacion
    def presentarse(self):
        print(f"me llamo {self.nombre} y tengo {self.edad} años")#se imprime un mensaje que incluye el nombre y la edad de la persona
# se crea una instancia de la clase Persona llamada "vanesa"
vanesa= Persona(nombre="vanesa", edad=17)

vanesa.presentarse()#se llama al metodo presentarse() de la instancia "vanesa"

        

