from auto import Auto
from moto import Moto

def main():
    vehiculos = []

    # Crear objetos de tipo Auto
    auto1 = Auto("Toyota", "Corolla", 2020, 4, True)
    auto2 = Auto("Honda", "Civic", 2019, 4, False)

    # Crear objetos de tipo Moto
    moto1 = Moto("Yamaha", "MT-09", 2021, 847, "Deportiva")
    moto2 = Moto("Honda", "CBR500R", 2018, 471, "Deportiva")

    # Agregar los vehículos a la lista
    vehiculos.append(auto1)
    vehiculos.append(auto2)
    vehiculos.append(moto1)
    vehiculos.append(moto2)

    # Mostrar la información de cada vehículo
    for vehiculo in vehiculos:
        print(vehiculo.mostrar_info())

if __name__ == "__main__":
    main()
