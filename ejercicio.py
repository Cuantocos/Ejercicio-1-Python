class Vehiculo():
    color = None
    ruedas = None
    puertas = None

    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

class Coche(Vehiculo):
    velocidad = None
    cilindrada = None

    def __init__(self, puertas, color, velocidad, cilindrada):
        self.ruedas = 4
        self.puertas = puertas
        self.color = color
        self.velocidad = velocidad
        self.cilindrada = cilindrada


mi_coche = Coche(4, "Amarillo", "120km/h", 5)
print(dir(mi_coche))