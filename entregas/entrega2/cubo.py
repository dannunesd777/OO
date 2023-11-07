class Cubo:
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return 6 * (self.lado ** 2)

    def volume(self):
        return self.lado ** 3

def calcular_cubo():
    lado = float(input("Digite o valor do lado do cubo: "))
    cubo = Cubo(lado)
    area = cubo.area()
    volume = cubo.volume()

    print(f"A área do cubo é: {area}")
    print(f"O volume do cubo é: {volume}")