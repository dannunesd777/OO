class Cubo:
# Calcular a área e o volume do cubo
    @staticmethod
def calcular_cubo():
    lado = float(input("Digite o valor do lado do cubo: "))

    # Calcular a área do cubo
    def area_cubo():
        area = 6 * (lado ** 2)
        return area

    # Calcular o volume do cubo
    def volume_cubo():
        volume = lado ** 3
        return volume

    area = area_cubo()
    volume = volume_cubo()

    print(f"A área do cubo é: {area}")
    print(f"O volume do cubo é: {volume}")