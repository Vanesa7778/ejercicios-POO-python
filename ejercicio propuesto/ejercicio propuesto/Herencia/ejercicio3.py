class Animal:
    def __init__(self,especie):#__init__ inicializa la propiedad especie
        self.especie=especie 
#se define la clase Perro que hereda de la clase Animal
class Perro(Animal):
    def __init__(self,nombre,raza):#__init__ inicializa la propiedad nombre, raza 
        super().__init__(especie="canino")#se llama al constructor de la clase padre usando super()
        self.nombre=nombre
        self.raza=raza
#se crea una instancia llamada perro 
mascota = Perro(nombre="Tony", raza="Ladrador")
#se imprime el nombre , raza y especie del perro
print(f"Nombre:{mascota.nombre}")
print(f"Raza:{mascota.raza}")
print(f"Especie:{mascota.especie}")