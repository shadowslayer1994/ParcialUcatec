from vehiculo import Vehiculo

class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, cilindraje, tipo):
        super().__init__(marca, modelo, año)
        self.cilindraje = cilindraje
        self.tipo = tipo

    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f'{info_base}, Cilindraje: {self.cilindraje}, Tipo: {self.tipo}'
