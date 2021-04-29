# jogo de Forca

secreta = 'parangaricutirrimirruaro'
digitados = []
chance = 15

while True:
    if chance <= 0:
        print(f'Você tentou {chance} e perdeu!')
        break
    letra = input('Digite uma letra: ')
    if len(letra) > 1:
        print('Digite apenas uma letra.!!')
        continue
    digitados.append(letra)
    if letra in secreta:
        print(f'Você descobriu que a letra {letra} existe na palavra secreta.')
    else:
        print(f'a letra {letra} não existe na palavra secreta.')
        digitados.pop()
    secreta_temporario = ''
    for letra_secreta in secreta:
        if letra_secreta in digitados:
            secreta_temporario += letra_secreta
        else:
            secreta_temporario += '*'
    if secreta_temporario == secreta:
        print(f'UHULLLL, VOCÊ GANHOU!!!!. a palavra secreta éra {secreta_temporario}')
        break
    else:
        print(f'A palavra secreta esta assim: {secreta_temporario}')
    if letra not in secreta:
        chance -= 1
    print(f'Você ainda tem {chance} chances.')
    print()