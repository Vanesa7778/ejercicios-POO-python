class Marino:#clase padre
    def hablar(self):#metodo para hablar 
        print("hola")

class Pulpo(Marino):#clase Pulpo hereda clase Marino
    def hablar(self):#metodo espcifico de hablar de un pulpo 
        print("soy un pulpo")

class Foca(Marino):#clase Foca hereda clase Marino
    def hablar(self):#metodo espcifico de hablar de una Foca
        print("soy una foca")
#se crean instancias
objetoPulpo= Pulpo()
objetoFoca= Foca()
#se llama metodo hablar de las instancias 
objetoPulpo.hablar()
objetoFoca.hablar()