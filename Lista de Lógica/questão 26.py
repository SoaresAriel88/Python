print("IMC")
peso = float(input("Informe seu peso"))
h = float(input("Informe sua altura"))
imc = peso / h ** 2
print("Seu imc é", imc)
if imc < 18.5:
    print("Abaixo do peso")
elif imc > 18.5 and imc <= 25:
    print("Peso normal")
elif imc > 25 and imc <= 30:
    print("Acima do peso")
elif imc > 30:
    print("Obeso")