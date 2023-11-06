import math

# Calcular a área e o perímetro do círculo
@staticmethod
def calcular_circulo():
    pi = 3.1415926
    raio = float(input("Digite o raio do círculo: "))

    # Calcular a área do círculo
    def area_circulo():
        area = pi * (raio ** 2)
        return area

    # Calcular o perímetro do círculo
    def perimetro_circulo():
        perimetro = 2 * pi * raio
        return perimetro

    area = area_circulo()
    perimetro = perimetro_circulo()

    print(f"A área do círculo é: {area}")
    print(f"O perímetro do círculo é: {perimetro}")