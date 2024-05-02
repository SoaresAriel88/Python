print("Caixa")
n1 = 1
n10 = 10
n100 = 100
com = int(input("Informe o valor da compra"))
pag = int(input("Informe o valor do pagamento"))
if com > pag:
    print("Pagamento negado")
else:
    tro = pag - com
    print("Seu troco ficou",tro,"$")
    tro1 = tro // n100
    tro = tro % n100
    tro2 = tro // n10
    tro = tro % n10
    n1 = tro
    print("Ficaram ", tro1, "notas de 100","e", tro2,"notas de 10",n1,"notas de 1" )

