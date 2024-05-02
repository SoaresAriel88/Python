sal = 1
n = 0
a = 0
while sal > 0:
        sal = int(input("Informe o salário: "))
        a = sal * 0.2
        n = n + 1
        abono = a
        print("Funcionário",n, "recebeu:", a)
        if a < 100:
            abono = 100
            a = abono
            print("Seu abono é:", abono)
         
        
