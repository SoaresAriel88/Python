print("Impar ou par")
n1 = int(input("Informe um número"))
n2 = int(input("Informe um número"))
d = n1 % n2
if d == 0:
    print("Par")
elif d > 0:
    print("Impar")