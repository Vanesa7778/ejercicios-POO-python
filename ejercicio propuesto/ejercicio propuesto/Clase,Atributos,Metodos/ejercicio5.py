class Operaciones:
    def __init__(self,num1,num2):#constructor de la clase que inicializa las propiedades num1 y num2
        self.num1=num1#asigna el valor de num1 al atributo 'num1'
        self.num2=num2#asigna el valor de num2 al atributo 'num2'

    def suma(self):#metodo para realizar la operación de suma
        return self.num1 + self.num2#retorna el resultado de la suma de num1 y num2
    
    def restar(self):#metodo para realizar la operación de resta
        return self.num1 - self.num2#retorna el resultado de la resta de num1 y num2
#se crea una instancia de la clase Operaciones llamada "resultado" con num1=10 y num2=4   
resultado= Operaciones(10,4)
# se imprime el resultado de la operacion de suma 
print(resultado.suma())
#se imprime el resultado de la operacion de resta 
print(resultado.restar())
