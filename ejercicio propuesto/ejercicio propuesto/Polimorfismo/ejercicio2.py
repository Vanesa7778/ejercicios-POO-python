class Pais:
    #metodo para obtener la capital del pais 
    def capital(self):
        pass
    
    # metodo para obtener el idioma del pais 
    def idioma(self):
        pass

# se define la clase Colombia que hereda de Pais
class Colombia(Pais):
    # se implementa de manera especifica el metodo capital para Colombia
    def capital(self):
        print("Bogotá")
    
    # se implementa de manera especifica el metodo idioma para Colombia
    def idioma(self):
        print("Español")

# se define la clase Canada que hereda de Pais
class Canada(Pais):
    # se implementa de manera especifica el metodo capital para Canada
    def capital(self):
        print("Ottawa")

    # se implementa de manera especifica el metodo idioma para Canada
    def idioma(self):
        print("Inglés")

# define la funcion polimorfica describirPais
def describirPais(pais):
    # se llama a los metodos capital() y idioma() independientemente de la clase 
    pais.capital()
    pais.idioma()

#se crean instancias de las clases
paisColombia = Colombia()
paisCanada = Canada()

#se llama a la funcion polimorfica
describirPais(paisColombia)  # llama a los metodos especificos de Colombia
describirPais(paisCanada)  # llama a los metodos especificos de Canada