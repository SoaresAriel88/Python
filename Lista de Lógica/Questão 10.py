print("Provas")
n1 = float(input("Informe sua primeira nota"))
n2 = float(input("Informe sua segunda nota"))
med = (n1 + n2) / 2
print("Sua média e", med)
if med >= 7:
    print("Aprovado")
elif med < 7 and med == 3:
    print("Prova final")
else:
    print("Reprovado")