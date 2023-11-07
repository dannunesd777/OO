class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado

    def perimetro(self):
        return 4 * self.lado

def calcular_quadrado():
    lado = float(input("Digite o valor do lado do quadrado: "))
    quadrado = Quadrado(lado)
    area = quadrado.area()
    perimetro = quadrado.perimetro()

    print(f"A área do quadrado é: {area}")
    print(f"O perímetro do quadrado é: {perimetro}")