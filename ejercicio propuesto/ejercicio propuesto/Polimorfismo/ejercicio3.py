class Pajaro:
    def intro(self):#metodo introduccion general sobre pajaros 
        print("hay diferentes tipos de pajaros")

    def vuelo (self):#metodo para describir el vuelo de los pajaros
        print("la mayoria de los pajaros pueden volar pero algunos no ")
#clase Loro que hereda de clase Pajaro
class Loro(Pajaro):
    def vuelo(self):#metodo vuelo sobre los loros
        print("los loros pueden volar")

#clase Pinguino que hereda de clase Pajaro
class Pinguino(Pajaro):
    def vuelo(self):#metodo vuelo sobre pinguinos
        print("los pinguinos no vuelan")
#se crea instancias 
objetoPajaro= Pajaro()
obejetoLoro= Loro()
objetoPinguino= Pinguino()
##se llama al metodo de las instancias
objetoPajaro.intro()
objetoPajaro.vuelo()

obejetoLoro.intro()
obejetoLoro.vuelo()

objetoPinguino.intro()
objetoPinguino.vuelo()