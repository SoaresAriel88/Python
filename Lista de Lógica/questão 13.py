print("Ordem")
n1 = int(input("Informe o primeiro número"))
n2 = int(input("Informe o segundo número"))
n3 = int(input("Informe o terceiro número"))
if n1 and n2 and n3:
    print(n1, n2, n3)
elif n1 and n3 and n3:
    print(n1, n3, n2)
elif n2 and n3 and n1:
    print(n2, n3, n1)
elif n2 and n1  and n3:
    print(n2, n1, n3)
elif n3 and n1 and n3:
    print(n3, n1, n3)
elif n3 and n2 and n1:
    print(n3, n2, n1)