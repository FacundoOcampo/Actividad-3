from ClaseRegistro import Registro

class Manejador:
    __Lista=None
    def __init__(self):
        self.__Lista=[]
    def CrearLista(self,Dias,Horas,Reader):
        for i in range (Dias):
            self.__Lista.append([0]*Horas)
        for fila in Reader:
            Dia=int(fila[0])
            Hora=int(fila[1])
            Temperatura=float(fila[2])
            Humedad=int(fila[3])
            PreAtmos=int(fila[4])
            NuevoRegistro=Registro(Temperatura,Humedad,PreAtmos)
            self.__Lista[Dia-1][Hora-1]=(NuevoRegistro)
        return self.__Lista
    def MaximoT(self,NLista,Max):
        Dia=None
        Hora=None
        for i in range(30):
            for j in range(24):
                aux=NLista[i][j].GetTemperatura()
                if(aux>Max):
                    Max=aux
                    Dia=i
                    Hora=j
        return print("      Maxima   Dia:{} Hora: {}".format(Dia+1,Hora+1))

    def MinimoT(self,NLista,Min):
        Dia=None
        Hora=None
        for i in range(30):
            for j in range(24):
                aux=NLista[i][j].GetTemperatura()
                if(aux<Min):
                    Min=aux
                    Dia=i
                    Hora=j
        return print("      Minimo   Dia:{} Hora: {}".format(Dia+1,Hora+1))

    def MaximoH(self,NLista,Max):
        Dia=None
        Hora=None
        for i in range(30):
            for j in range(24):
                aux=NLista[i][j].GetHumedad()
                if(aux>Max):
                    Max=aux
                    Dia=i
                    Hora=j
        return print("      Maxima   Dia:{} Hora: {}".format(Dia+1,Hora+1))

    def MinimoH(self,NLista,Min):
        Dia=None
        Hora=None
        for i in range(30):
            for j in range(24):
                aux=NLista[i][j].GetHumedad()
                if(aux<Min):
                    Min=aux
                    Dia=i
                    Hora=j
        return print("      Minimo   Dia:{} Hora: {}".format(Dia+1,Hora+1))
    def MaximoP(self,NLista,Max):
        Dia=None
        Hora=None
        for i in range(30):
            for j in range(24):
                aux=NLista[i][j].GetPreAtmo()
                if(aux>Max):
                    Max=aux
                    Dia=i
                    Hora=j
        return print("      Maxima   Dia:{} Hora: {}".format(Dia+1,Hora+1))

    def MinimoP(self,NLista,Min):
        Dia=None
        Hora=None
        for i in range(30):
            for j in range(24):
                aux=NLista[i][j].GetPreAtmo()
                if(aux<Min):
                    Min=aux
                    Dia=i
                    Hora=j
        return print("      Minimo   Dia:{} Hora: {}".format(Dia+1,Hora+1))
