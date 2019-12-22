'''Faça um programa que o usuário tem que adivinha o número mágico.
- Caso o usuário escolha um número maior que o mágico, aponte que o número é muito alto.
- Caso o usuário escolha um número menor que o mágico, aponte que o número é muito baixo.
- Caso o usuário acerte o número, mostre: Você acertou, parabens
O usuário deve ter apenas 3 tentativas.
'''

tentativa = 1
print(tentativa)

while tentativa <= 3:
    try:
        user_num = int( input("Tente acertar o número entre 1 e 20: ") )
    except ValueError as err:
        print("Entre com um número válido!")
        continue

    if user_num == 10:
        print("Você Acertou! FODAAA!")
        break

    elif user_num > 10:
        print("Muito alto! Tente um valor menor!")

    else:
        print("Muito baixo! Tente um valor maior!")
        
    tentativa += 1

else:
    print("Acabaram suas chances: LOOOOOSER", tentativa)