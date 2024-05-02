
print("Masculino digite 1")
print("Feminino digite 2")
sexo = int(input("Informe o seu sexo"))
if sexo == 1:
 h = float(input("Qual é sua altura"))
 peso = (72.2 * h) - 58
 print("Seu peso ideal é", peso)
elif sexo == 2:
 h = float(input("Qual é sua altura"))
 peso = (62.1 * h) - 44.7
 print("Seu peso ideal é", peso)