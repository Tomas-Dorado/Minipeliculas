from Pelicula import Pelicula

class Catalogo:

    peliculas = [] # Esta lista contendrá objetos de la clasePelicula

    def __init__(self, peliculas=[]):
        self.peliculas = peliculas

    def agregar(self, p): # p será un objeto Pelicula
        self.peliculas.append(p)

    def mostrar(self):
        for p in self.peliculas:
            print(p) # Print toma por defecto str(p)