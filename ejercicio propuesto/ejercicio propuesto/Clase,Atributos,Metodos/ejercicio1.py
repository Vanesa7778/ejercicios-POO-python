#Consulte un ejemplo donde se declare una clase con atributos y métodos
#la clase es una plantilla para crear objetos y definir atributos y metodos comunes para los objeto que crearan a partir de ella
#Self nos permite acceder a los atributos y metodos de esa instancia dentro de los metodos de la clase

#se define la clase Lapiz
class Lapiz:
#se establece un atributo de clase que representa el color del lapiz, establecido como "negro"
    color="negro"
#metodo para simular la accion de dibujar con el lapiz
    def dibujar(self):
        print("el lapiz esta dibujando")
#metodo para simular la accion de borrar con el lapiz
    def borrar(self):
        print("el lapiz esta borrando")
#seb crea instancia cuaderno
cuaderno= Lapiz()
cuaderno.dibujar()#se llama al metodo dibujar
cuaderno.borrar()#se llama al metodo borrar