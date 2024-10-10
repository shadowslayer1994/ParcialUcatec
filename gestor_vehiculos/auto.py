from vehiculo import Vehiculo

class Auto(Vehiculo):
    def __init__(self, marca, modelo, año, numero_puertas, es_automatico):
        super().__init__(marca, modelo, año)
        self.numero_puertas = numero_puertas
        self.es_automatico = es_automatico

    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f'{info_base}, Número de Puertas: {self.numero_puertas}, Es Automático: {self.es_automatico}'
