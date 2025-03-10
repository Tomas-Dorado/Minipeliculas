class Pelicula:

    # Constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento


    def __str__(self):
        return 'Se ha creadp la peliculas: {} ({})'.format(self.titulo, self.lanzamiento)
    
