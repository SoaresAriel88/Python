#Cardápio
while True:

    cac = 7.90
    br = 4.90
    bro = 6.50
    ham = 9.90
    che = 10.90
    ref = 3.60
    print("Cardápio")
    print("Cachorro quente [100]")
    print("Bauru Simples [101]")
    print("Bauru c/ovo [102]")
    print("Hamburguer [103]")
    print("Cheeseburguer [104]")
    print("Refrigerante [105]")
    esc = int(input("Escolha seu lache "))
    q = int(input("Quantos vão ser "))
    if esc == 100:
        print("O preço será ", cac * q, "$")
    elif esc == 101:
        print("O preço será ", br * q, "$")
    elif esc == 102:
        print("O preço será ", bro * q, "$")
    elif (esc == 103):
        print("O preço será ", ham * q, "$")
    elif esc == 104:
        print("O preço será ", che * q, "$")
    elif esc == 105:
        print("O preço será ", ref * q, "$")

    else:
        print("Este item não se encontra no cardápio")







