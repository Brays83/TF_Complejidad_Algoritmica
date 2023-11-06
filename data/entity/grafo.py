

class Grafo:
    def __init__(self,name):
        self.name = name
        self.vertices={}
        self.MoviesRecomendadas=[]
        self.mayor=0
        self.index_mayor=0
        
        

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

    
    
    def dfs(self, source):
        visited = set()
        Plataforma = source

        def recursion(node):
            # 1er paso: Marcar como visitado
            visited.add(node)

            # Procesar el nodo (haz la operación que quieras)
            if(node != Plataforma):
                

                if(len(self.MoviesRecomendadas)<10):
                    self.MoviesRecomendadas.append(node)
                else:
                    ##Buscamos el peso mayor del arreglo con su indice
                    for i in range(len(self.MoviesRecomendadas)):
                        if(self.vertices[Plataforma][self.MoviesRecomendadas[i]] >= self.mayor):
                            self.mayor= self.vertices[Plataforma][self.MoviesRecomendadas[i]] 
                            self.index_mayor = i
                            print("----------------------")
                            print("peso mayor: ",self.mayor)
                            print("Indice del Peso mayor: ",self.index_mayor)
                            
                            print("Peso del nodo anaizar: ",self.vertices[Plataforma][node])
                            print("----------------------")
                    
                    ##Comparamos si el nuevo peso supera al mayor

                    if(self.vertices[Plataforma][node]<=self.mayor):
                        print("----------------------")
                        for i in range(len(self.MoviesRecomendadas)):
                            print(self.MoviesRecomendadas[i].getName())

                        self.MoviesRecomendadas.pop(self.index_mayor)
                        self.MoviesRecomendadas.append(node)
                        print("----------------------")
                        for i in range(len(self.MoviesRecomendadas)):
                            print(self.MoviesRecomendadas[i].getName())
                        print("----------------------")
                        ##self.MoviesRecomendadas[self.index_mayor]=node
                print("Pelicula:{}, Peso:{}".format(node.getName(),self.vertices[Plataforma][node]))
                    


                            
                
            # Llamo a que la recursión visite los vecinos NO visitados
            for neighbour in self.vertices[node]:
                if neighbour not in visited:
                    recursion(neighbour)

        recursion(source)




    




