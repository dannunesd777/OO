class Retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def calcular_area(self):
        return self.comprimento * self.largura

    def calcular_perimetro(self):
        return 2 * (self.comprimento + self.largura)
    
def calcular_retangulo():
    comprimento = float(input("Digite o comprimento do retângulo: "))
    largura = float(input("Digite a largura do retângulo: "))
    reta = Retangulo(comprimento, largura)


    print(f"A área do retângulo é: {reta.calcular_area()}")
    print(f"O perímetro do retângulo é: {reta.calcular_perimetro()}")