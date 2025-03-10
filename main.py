from Catalogo import Catalogo
from Pelicula import Pelicula

def main():
    p = Pelicula("El Padrino", 175, 1972)
    c = Catalogo([p]) # Añado una lista con una película desde elprincipio
    c.mostrar()
    c.agregar(Pelicula("El Padrino: Parte 2", 202, 1974)) # Añadimos otra
    c.agregar(Pelicula("El padrino: Parte 3", 176, 1980))
    c.mostrar()


if __name__=="__main__":
    main()