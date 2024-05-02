#Credito
while True:

    print("Crédito")
    cr = float(input("Informe seu crédito: "))
    if cr <= 2000:
        print("Infelizmente não possui crédito suficiente")
    elif cr > 2001 and cr < 4001:
        print("Você terá um saldo de  ", cr * (20 / 100), "$")
    elif cr > 4001 and cr < 6000:
        print("Você terá um saldo de ", cr * (30 / 100), "$")
    else:
        print("Vcoê téra um saldo de", cr * (40 / 100), "$")

