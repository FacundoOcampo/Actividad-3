import csv
from Manejador import Manejador
from ClassMenu import Menu
from ClaseRegistro import Registro

if __name__ == '__main__':
    Archivo=open("Archivo.csv","r")
    Reader=csv.reader(Archivo,delimiter=",")
    NuevoMenu=Menu()
    NuevoManejador=Manejador()
    NLista=NuevoManejador.CrearLista(30,24,Reader)
    Op=int(input("Seleccione una opcion:\n        1_Mostrar para cada variable el día y hora de menor y mayor valor.\n        2_Indicar la temperatura promedio mensual por cada hora.\n        3_Dado un número de día listar los valores de las tres variables para cada hora del día dado.\n        0_Salir\n"))
    NuevoMenu.Opciones(Op,Archivo,Reader,NLista,NuevoManejador)
    while Op != 0:
        Op=int(input("Seleccione una opcion:\n        1_Mostrar para cada variable el día y hora de menor y mayor valor.\n        2_Indicar la temperatura promedio mensual por cada hora.\n        3_Dado un número de día listar los valores de las tres variables para cada hora del día dado.\n        0_Salir\n"))
        NuevoMenu.Opciones(Op,Archivo,Reader,NLista,NuevoManejador)
    Archivo.close()
