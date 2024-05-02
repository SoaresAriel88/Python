com = int(input("Qual é o valor da compra"))
print("Pagamento a vista no dinheiro ou cheque, 10% desconto[1]")
print("Pagamento a vista no cartão, 15% desconto[2]")
print("Em duas vezes, preço normal sem juros[3]")
print("Em duas vezes, preço normal mais 10% juros[4]")
esc = int(input("Escolha sua forma de pagamento"))
if esc == 1:
    d = com // 10
    print("O preço ficará ", com - d)
elif esc == 2:
    d = com // 15
    print("O preço ficará ", com - d)
elif esc == 3:
    d = com / 2
    print("O preço em duas vezes ficará", d)
elif esc == 4:
    j = com * (10/100)
    d = com / 2 + j
    print("O preço ficará", d)

