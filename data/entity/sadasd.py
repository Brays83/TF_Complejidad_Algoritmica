                if(len(self.MoviesRecomendadas) < 10):
                    #Agregamos el nodo y peso a la lista
                    self.MoviesRecomendadas.append(node)
                    
                    print("Tamaño del arreglo",len(self.MoviesRecomendadas))
                    print("============================")
                elif(len(self.MoviesRecomendadas) == 9):
                    ##Buscamos el peso mayor del arreglo con su indice
                   for i in range(len(self.MoviesRecomendadas)):
                       if(self.vertices[Plataforma][self.MoviesRecomendadas[i]]>self.mayor):
                           self.mayor = self.vertices[Plataforma][self.MoviesRecomendadas[i]]
                           self.i_mayor = i
                           print("============================")
                           print("Indice del Peso maximo: ",self.i_mayor)
                           print("Peso maximo: ",self.mayor)
                           print("============================")
                elif(self.vertices[Plataforma][node] < self.mayor):       
                    print("============================")
                    print("Se elimino: ",self.i_mayor)
                    print("Se agrego: ",node.getName())
                    self.MoviesRecomendadas.pop(self.i_mayor)
                    self.MoviesRecomendadas.append(node)
                    print("============================")
                    print("Peliculas recomendadas:")
                    for i in range(len(self.MoviesRecomendadas)):
                        print("indice: {} pelicula: {} peso: {}"
                            .format(i,self.MoviesRecomendadas[i].getName(),self.vertices[Plataforma][self.MoviesRecomendadas[i]]))   