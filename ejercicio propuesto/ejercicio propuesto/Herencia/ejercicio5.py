class Persona:
    # Constructor de la clase que inicializa las propiedades nombre, edad e identificacion
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Asigna el nombre al atributo 'nombre'
        self.edad = edad      # Asigna la edad al atributo 'edad'
      

    # metodo para imprimir un mensaje de presentacion
    def presentarse(self):
        # imprime un mensaje que incluye el nombre y la edad de la persona
        print(f"Hola!! Me llamo {self.nombre} y tengo {self.edad} años")

#crea  una instancia de la clase Persona llamada "vanesa"
vanesa = Persona(nombre="Vanesa", edad=17)

#se llama al metodo presentarse() de la instancia "vanesa"
vanesa.presentarse()

#se define la clase Trabajador que hereda de Persona
class Trabajador(Persona):
    pass

#se crea una instancia de la clase Trabajador llamada "trabajador"
trabajador = Trabajador(nombre="Sandra", edad=39 )

#se llama al metodo presentarse() de la instancia "trabajador"
trabajador.presentarse()