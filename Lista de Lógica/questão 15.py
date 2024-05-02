print("Percuso de um carro")
ca = 8.000
cb = 9.000
cc = 12.000
print("Escolha o tipo do carro")
print("Carro A [1]")
print("Carro B [2]")
print("Carro C [3]")
esc = float(input("Informe o tipo de carro"))

gst = float(input("Informe o abastecimento"))
if esc == 1:
    print("Carro A tem", ca,"Km")
    print("Seu consumo será", ca / gst,"Litros")
elif esc == 2:
    print("Carro B tem", cb,"Km")
    print("Seu consumo será", cb / gst,"Litros")
elif esc == 3:
    print("Carro C tem", cc,"Km")
    print("Seu consumo serã", cb / gst,"Litros")
else:
    print("Tipo inválido")