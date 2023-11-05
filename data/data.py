import csv
import sys
sys.path.append('./data/entity')
from movie import Movie
from grafo import Grafo

def ReadData(year,platform):
    grafoPadre = Grafo("Padre")
    grafoPadre.Agregar_Vertice("Netflix")
    grafoPadre.Agregar_Vertice("Hulu")
    grafoPadre.Agregar_Vertice("Amazon")
    grafoPadre.Agregar_Vertice("Disney")

    grafoPadre.agregar_arista("Netflix","Hulu",5)


    with open('./data/datos.csv')as data:
        next(data)
        reader=csv.reader(data,delimiter='|')
        for row in reader:
            movie = Movie(row[0],row[1],row[2],row[3],row[4],row[5],row[6],int(row[7]),int(row[8]),int(row[9]),int(row[10]))
            grafoPadre.Agregar_Vertice(movie.getName())
            if(movie.getnetflix() == True):
                grafoPadre.agregar_arista("Netflix",movie.getName(),1)
            elif(movie.gethulu()==True):
                grafoPadre.agregar_arista("Hulu",movie.getName(),1)
            elif(movie.getPrime()==True):
                grafoPadre.agregar_arista("Amazon",movie.getName(),1)
            elif(movie.getDisney()==True):
                grafoPadre.agregar_arista("Disney",movie.getName(),1)
            #Movies.append(Movie(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]))
        return grafoPadre
    

h = ReadData()

#h.mostrar_vertices()

h.dfs('Netflix')




