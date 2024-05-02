#Calculadora
while True:


    def soma (a, b):
        return (a + b)

    def subtracao (a, b):
        return (a - b)

    def multiplicacao (a, b):
        return (a * b)

    def divisao (a, b):
        return (a / b)
    print("Calculadora")
    print("soma [1]")
    print("subtracao [2]")
    print("multiplicacao [3]")
    print("divisao [4]")
    esc = int(input("Escolha sua operação "))
    num1 = float(input("Digite seu primeiro número "))
    num2 = float(input("Digite seu segundo número "))

    if esc == 1:
        print(soma(num1, num2))
    elif esc == 2:
        print(subtracao(num1, num2))
    elif esc == 3:
        print(multiplicacao(num1, num2))
    elif esc == 4:
        print(divisao(num1, num2))
    else:
        print("Erro")
    


