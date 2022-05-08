from Manejador import Manejador

class Menu:
    __Op=None
    def __init__(self):
        self.__Op=None
    def Opciones(self,Op,Archivo,Reader,NLista,NuevoManejador):
        if Op==1:
            self.Opcion1(NLista,NuevoManejador)
        elif Op==2:
            self.Opcion2(NLista)
        elif Op==3:
            self.Opcion3(NLista)
        else:
            print("Caracter no valido. Vuelva a ingresar")

    def Opcion1(self,NLista,NuevoManejador):
        print("Temperatura: ")
        NuevoManejador.MaximoT(NLista,-1)
        NuevoManejador.MinimoT(NLista,99)
        print("Humedad: ")
        NuevoManejador.MaximoH(NLista,-1)
        NuevoManejador.MinimoH(NLista,101)
        print("Presion Atmosferica: ")
        NuevoManejador.MaximoP(NLista,-1)
        NuevoManejador.MinimoP(NLista,5000)
    def Opcion2(self,NLista):
        for i in range(24):
            acum=0
            total=0
            for j in range (30):
                acum=acum + NLista[j][i].GetTemperatura()
            total=acum/30
            print("Temperatura promedio en la hora {}: {:.2f} grados".format(i+1,total))
    def Opcion3(self,NLista):
        Num=int(input("Ingrese un dia\n"))
        xLista=[]
        for i in range(24):
            xLista.append(NLista[Num-1][i])
        for i in range(24):
            print("Hora","Temperatura","Humedad","Presion")
            print(i+1,xLista[i].GetTemperatura(),xLista[i].GetHumedad(),xLista[i].GetPreAtmo(),sep="      ")
