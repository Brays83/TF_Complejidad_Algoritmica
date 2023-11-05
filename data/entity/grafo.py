

class Grafo:
    def __init__(self,name):
        self.name = name
        self.vertices={}
        
        

    def Agregar_Vertice(self,vertice):
        if vertice not in self.vertices:
            self.vertices[vertice]={}
            


    def agregar_arista(self, origen, destino, peso):
        if origen in self.vertices and destino in self.vertices:
            self.vertices[origen][destino] = peso
            self.vertices[destino][origen] = peso
        

    
    def mostrar_vertices(self):
        for nodo in self.vertices:
            print(nodo, "-->",[i for i in self.vertices[nodo]])
      #return self.vertices
    
    def dfs(self, source):
        visited = set()

        def recursion(node):
            # 1er paso: Marcar como visitado
            visited.add(node)

            # Procesar el nodo (haz la operación que quieras)
            print(node)

            # Llamo a que la recursión visite los vecinos NO visitados
            for neighbour in self.vertices[node]:
                if neighbour not in visited:
                    recursion(neighbour)

        recursion(source)




    




