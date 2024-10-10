class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def mostrar_info(self):
        return f'Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}'
