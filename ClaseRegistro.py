class Registro:
    __Temperatura=None
    __Humedad=None
    __PreAtmos=None
    def __init__(self,Temperatura,Humedad,PreAtmos):
        self.__Temperatura=Temperatura
        self.__Humedad=Humedad
        self.__PreAtmos=PreAtmos
    def GetTemperatura(self):
        return self.__Temperatura
    def GetHumedad(self):
        return self.__Humedad
    def GetPreAtmo(self):
        return self.__PreAtmos
    def MostrarDatos(self):
        print(self.__Temperatura,self.__Humedad,self.__PreAtmos)
