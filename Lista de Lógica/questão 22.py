print('1. Idoso')
print('2. Gestante')
print('3. Cadeirante')
print('4. Nenhum destes')
resposta=int( input('Você é: ') )

if (resposta==1) or (resposta==2) or (resposta==3) :
    print('Você tem direito a fila prioritária')
else:
    print('Você não tem direito a nada. Vá pra fila e fique quieto')

