# Função para calcular a área e o perímetro de um retangulo
def calcular_retangulo():
    lado = float(input("Digite o valor do lado do retangulo: "))

    # Função para calcular a área do retangulo
    def area_retangulo():
        area = base * altura
        return area

    # Função para calcular o perímetro do retangulo
    def perimetro_retangulo():
        perimetro = 4 * (base + altura)
        return perimetro

    area = area_retangulo()
    perimetro = perimetro_retangulo()

    print(f"A área do retangulo é: {area}")
    print(f"O perímetro do retangulo é: {perimetro}")