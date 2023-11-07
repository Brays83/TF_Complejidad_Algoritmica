import csv
import sys
sys.path.append('./data/entity')

from Calculo import calculo

from movie import Movie
from grafo import Grafo

def ReadData(year,categoria,subcategoria,calificacion,edad,platform):
    ListPlatforms = ["Netflix","Hulu","Amazon","Disney"]
    grafoPadre = Grafo("Padre")

    opciones = {
    "Comedia": 22,
    "Accion": 21,
    "Aventura": 20,
    "Familia": 19,

    "Ciencia Ficcion": 18,
    "Romance": 17,
    "Terror": 16,
    "Misterio": 15,
    "Fantasia": 14,
    "Drama": 13,
    "Suspenso": 12,

    "Crimen": 11,
    "Musical": 10,
    "Super Heroes": 9,
    "Princesas": 8,

    "Navidad": 7,
    "Halloween": 6,
    
    "Biografia": 5,
    "Documental": 4,
    "Stand Up": 3,
    "Deporte": 2,
    
    "Animal": 1,
    "": 0
    }
    
    D_edad = {
    "all": 1,
    "18+": 2,
    "16+": 3,
    "13+": 4,
    "7+": 5
    }

    grafoPadre.Agregar_Vertice("Plataformas")
    for i in ListPlatforms:
        grafoPadre.Agregar_Vertice(i)
        if(i== platform):
            grafoPadre.agregar_arista("Plataformas",i,1)
        else:
            grafoPadre.agregar_arista("Plataformas",i,5)
    

    with open('./data/datos.csv')as data:
        next(data)
        reader=csv.reader(data,delimiter='|')
        for row in reader:
            movie = Movie(row[0],row[1],int(row[2]),row[3],int(row[4]),row[5],row[6],int(row[7]),int(row[8]),int(row[9]),int(row[10]))
            grafoPadre.Agregar_Vertice(movie)
            #Normalizar CATEGORIA Valor actual- valor minimo/valor maximo-valor minimo
            if(movie.getnetflix() == True):
                grafoPadre.agregar_arista("Netflix",
                    movie,
                    calculo(movie.getYear(),
                    opciones[movie.getCategory()]/22,
                    opciones[movie.getsubCategory()]/22,
                    movie.getRating(),
                    D_edad[movie.getAge()],year,categoria,subcategoria,calificacion,edad))
    
            elif(movie.gethulu()==True):
                grafoPadre.agregar_arista("Hulu",
                    movie,
                    calculo(movie.getYear(),
                    opciones[movie.getCategory()]/22,
                    opciones[movie.getsubCategory()]/22,
                    movie.getRating(),
                    D_edad[movie.getAge()],year,categoria,subcategoria,calificacion,edad))
            elif(movie.getPrime()==True):
                grafoPadre.agregar_arista("Amazon",
                    movie,
                    calculo(movie.getYear(),
                    opciones[movie.getCategory()]/22,
                    opciones[movie.getsubCategory()]/22,
                    movie.getRating(),
                    D_edad[movie.getAge()],year,categoria,subcategoria,calificacion,edad))
            elif(movie.getDisney()==True):
                grafoPadre.agregar_arista("Disney",
                    movie,
                    calculo(movie.getYear(),
                    opciones[movie.getCategory()]/22,
                    opciones[movie.getsubCategory()]/22,
                    movie.getRating(),
                    D_edad[movie.getAge()],year,categoria,subcategoria,calificacion,edad))

            #Movies.append(Movie(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]))
        return grafoPadre
    

##h = ReadData(2010,5,5,50,1,'Netflix')

#h.mostrar_vertices()

##h.dfs('Netflix')

##print("----------------------")
##h.mostrar_vertices()
#h.MoviesRecomendadas()
#h.MostrarBiblioteca()
##print("----------------------")
##h.MostrarPeliculasRecomendadas('Netflix')
##h.PesoMaximo()



