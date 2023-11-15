# se define  la clase Terrestre
class Terrestre:
    # metodo para describir el desplazamiento terrestre del animal
    def desplazar(self):
        print("El animal se desplaza")

# se define la clase Acuatico
class Acuatico:
    # metodo para describir el desplazamiento  del animal
    def nadar(self):
        print("El animal nada")

# se define  la clase Cocodrillo que hereda de Terrestre y Acuatico
class Cocodrillo(Terrestre, Acuatico):
    pass

# se crea  una instancia de la clase Cocodrillo
animal = Cocodrillo()

#se llama al metodo heredado desplazar() de la clase Terrestre
animal.desplazar()

#se llamar al metodo heredado nadar() de la clase Acuatico
animal.nadar()


