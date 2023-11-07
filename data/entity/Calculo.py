from math import sqrt
def calculo(year,categoria,subcategoria,calificacion,edad,Iyear,Icategoria,Isubcategoria,Icalificacion,Iedad):
    MultiplicacionVectors=(year*Iyear + categoria*Icategoria+subcategoria*Isubcategoria+calificacion*Icalificacion+edad*Iedad)
    Modulovectores=(sqrt(pow(year,2)+pow(categoria,2)+pow(subcategoria,2)+pow(calificacion,2)+pow(edad,2))*sqrt(pow(Iyear,2)+pow(Icategoria,2)+pow(Isubcategoria,2)+pow(Icalificacion,2)+pow(Iedad,2)))
    print(MultiplicacionVectors/Modulovectores)
    return MultiplicacionVectors/Modulovectores