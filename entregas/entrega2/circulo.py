import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio
        self.pi = math.pi

    def area(self):
        return self.pi * (self.raio ** 2)

    def perimetro(self):
        return 2 * self.pi * self.raio

def calcular_circulo():
    raio = float(input("Digite o raio do círculo: "))
    circulo = Circulo(raio)
    area = circulo.area()
    perimetro = circulo.perimetro()

    print(f"A área do círculo é: {area}")
    print(f"O perímetro do círculo é: {perimetro}")