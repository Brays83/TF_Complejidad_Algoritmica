

class Grafo:
    def __init__(self,name):
        self.name = name
        self.vertices={}
        self.MoviesRecomendadas=[]

        self.mayor = 0
        self.i_mayor = 0

                 
         
        
        

    def Agregar_Vertice(self,vertice):
        if vertice not in self.vertices:
            self.vertices[vertice]={}
            


    def agregar_arista(self, origen, destino, peso):
        if origen in self.vertices and destino in self.vertices:
            self.vertices[origen][destino] = peso
            #self.vertices[destino][origen] = peso
    
    def MostrarBiblioteca(self):
        print("----------------------")
        print(self.vertices)
        

    
    def mostrar_vertices(self):
        for nodo in self.vertices:
            print(nodo, "-->",[i for i in self.vertices[nodo]],)
      #return self.vertices

    def MostrarPeliculasRecomendadas(self,Plataforma):
        for i in range(len(self.MoviesRecomendadas)):
            print("Indice: {} Pelicula: {} Peso: {}".format(i,self.MoviesRecomendadas[i].getName(),self.vertices[Plataforma][self.MoviesRecomendadas[i]]))

    def VaciarPeliculasRecomendadas(self):
        self.MoviesRecomendadas = []

    def PesoMaximo(self):
        print("Peso maximo: {} Indice: {}".format(self.mayor,self.i_mayor))
    
    def dfs(self, source):
        visited = set()
        Plataforma = source


        def recursion(node):
            # 1er paso: Marcar como visitado
            visited.add(node)
            
            # Procesar el nodo (haz la operación que quieras)
            if(node != Plataforma):
                print("Pelicula: {}, Peso: {}".format(node.getName(),self.vertices[Plataforma][node]))
                if(len(self.MoviesRecomendadas)<15):
                    if(self.mayor== 0):
                        print("if==0")
                        self.MoviesRecomendadas.append(node)
                        self.mayor = self.vertices[Plataforma][node]
                        self.i_mayor = len(self.MoviesRecomendadas)-1
                        
                    else:
                        print("if<0")
                        self.MoviesRecomendadas.append(node)
                        if(self.mayor < self.vertices[Plataforma][node]):
                            self.mayor = self.vertices[Plataforma][node]
                            self.i_mayor = len(self.MoviesRecomendadas)-1
                elif(len(self.MoviesRecomendadas)==15):
                    for movie in self.MoviesRecomendadas:
                        if(self.mayor < self.vertices[Plataforma][movie]):
                            self.mayor = self.vertices[Plataforma][movie]
                            self.i_mayor = self.MoviesRecomendadas.index(movie)
                    print("======================================")
                    #posible erro por aca
                     
                    ##temp=self.MoviesRecomendadas.remove(self.MoviesRecomendadas[self.i_mayor])
                    print("Pelicula eliminada: ",self.MoviesRecomendadas.pop(self.i_mayor).getName())
                    self.MoviesRecomendadas.append(node)    
                    print("Peso + al eliminar: ",self.mayor)
                    print("Indice + al eliminar: ",self.i_mayor)
                    print("Pelicula agregada: ",node.getName())
                    self.MostrarPeliculasRecomendadas(Plataforma)



                    
                


            # Llamo a que la recursión visite los vecinos NO visitados
            for neighbour in self.vertices[node]:
                if neighbour not in visited:
                    

                    recursion(neighbour)

        recursion(source)



    




