#Consulte un ejemplo donde se implemente el polimorfismo
#el polimorfismo permite que un objeto sea utilizado de diversas maneras

class Estudiante:
#metodo para describir un estudiante
    def describir(self):
        print("soy buen estudiante")

class Docente:
    def describir(self):#metodo para describir un docente
        print("me dedico a enseñar matematicas")

class Trabajador:
    def describir(self):#metodo para describir un trabajador
        print("Soy medico")
#se define la funcion polimorfica describrirPersona 
def describrirPersona(persona):
    persona.describir()
#se crean instancias 
doc1=Docente()
est1=Estudiante()
trab1= Trabajador()
#llamar a la funcion polimorfica
describrirPersona(doc1) # llama al metodo describir de la clase Docente
describrirPersona(est1) # lama al metodo describir de la clase Estudiante
describrirPersona(trab1) #llama al metodo describir de la clase Trabajador