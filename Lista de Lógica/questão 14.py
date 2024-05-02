print("Eleições")
cidade = 'Fortaleza'
print("O municipio é",cidade)
ele = int(input("Informe o número de eleitores"))
print("são", ele, "eleitores")
cand1 = int(input("Informe o número de votos do candidato 1"))
print("candidato 1 tem", cand1,"votos")
cand2 = int(input("Informe o número de votos do candidato 2"))
print("candidato 2 tem", cand2,"votos")
voto = 100
if cand1 > voto:
    print("Não terá segundo turno")
elif cand2 > voto:
    print("Não terá segundo turno")
elif cand1 <= voto:
    print("Terá segundo turno")
elif cand2 <= voto:
    print("Terá segundo turno")