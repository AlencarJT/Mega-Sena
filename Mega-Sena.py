from random import randint

resultado = list()
c = 0
while c < 6:
    r = randint(1, 60)
    if r not in resultado:
        resultado.append(r)
        c += 1
resultado.sort()

jogo = list()
for i in range(0, 6):
    j = int(input(f'Digite o {i + 1} número jogado: '))
    jogo.append(j)
jogo.sort()
print(f'O jogador apostou os números {jogo}')
acertos = 0
for i in range(0, 6):
    for j in range(0, 6):
        if jogo[j] == resultado[i]:
            acertos += 1
print(f'Os valores sorteados da semana foram: {resultado}')
print(f'Os valores jogados foram: {jogo}')
if acertos == 6:
    print(f'Parabéns, você ficou rico, acertou os {acertos} números da loteria')
elif acertos == 5:
    print(f'Você acertou {acertos} números. Fez a Quina, muito legal')
elif acertos == 4:
    print(f'Você acertou {acertos} números. Fez a Quadra, legal')
else:
    print(f'Você acertou {acertos} números. Mais sorte no próximo jogo!')