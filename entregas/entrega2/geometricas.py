# Função principal
import Circulo
import Cubo
import Quadrado
import Retangulo
import Triangulo

def main():
    while True:
        print("Escolha uma das opções:")
        print("1. Calcular área e o perímetro do círculo")
        print("2. Calcular área e o volume do cubo")
        print("3. Calcular área e o perímetro do quadrado")
        print("4. Calcular área e o perímetro do retangulo")
        print("5. Calcular área e o perímetro do triângulo")
        print("6. Sair")

        opcao = int(input("Digite o número da opção desejada: "))

        if opcao == 1:
            Circulo.calcular_circulo()
        elif opcao == 2:
            Cubo.calcular_cubo()
        elif opcao == 3:
            Quadrado.calcular_quadrado()
        elif opcao == 4:
            Retangulo.calcular_retangulo()
        elif opcao == 5:
            Triangulo.calcular_triangulo()
        elif opcao == 6:
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
