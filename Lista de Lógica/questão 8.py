print("Salários")
sb = int(input("Informe seu salário"))
if sb <= 2000:
    sl = sb * 0.1
    print("O seu salário liquido é", sl)
elif sb >= 2000:
    sl = sb * 0.2
    print("O seu salário liquido é", sl)