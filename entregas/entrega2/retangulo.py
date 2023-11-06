class Retangulo:
    @staticmethod
    def calcular():
        base = float(input("Digite o valor da base do retangulo: "))
        altura = float(input("Digite o valor da altura do retangulo: "))

        # Calcular a área do retangulo
        def area_retangulo():
            area = base * altura
            return area

        # Calcular o perímetro do retangulo
        def perimetro_retangulo():
            perimetro = 2 * (base + altura)
            return perimetro

        area = area_retangulo()
        perimetro = perimetro_retangulo()

        print(f"A área do retangulo é: {area}")
        print(f"O perímetro do retangulo é: {perimetro}")