#Triângulo
print("Triângulos")
l1 = int(input("Informe o número"))
l2 = int(input("Informe o número"))
l3 = int(input("Informe o número"))
if l1 == l2 and l2 == l3:
    print("Equilâtero")
elif l1 == l2 and l2 != l3:
    print("Isosceles")
elif l2 == l3 and l1 != l3:
    print ("Isosceles")
elif l1 == l3 and l2 != l1:
    print("Isosceles")
elif l1 != l2 and l2 != l3:
    print("Escaleno")