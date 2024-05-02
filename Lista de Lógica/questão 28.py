print("Média")
n1 = float(input("Informe sua primeira nota"))
n2 = float(input("Informe sua segunda nota"))
n3 = float(input("Informe sua terceira nota"))
me = float(input("Informe sua nota dos exercícios"))
ma = (n1 + n2 * 2 + n3 * 3 + me) / 7
print(ma)
if ma >= 9.0:
    print("O conceito da sua nota é A")
elif ma >= 7.5 and ma < 9.0:
    print("O conceito da sua nota é B")
elif ma >= 6.0 and ma < 7.5:
    print("O conceito da sua nota é C")
elif ma >= 4.0 and ma < 6.0:
    print("O conceito da sua nota é D")
else:
    print("O conceito da sua nota é E")