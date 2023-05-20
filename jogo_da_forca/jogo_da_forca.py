import random

def jogar_forca():
    palavras = ['cadeira', 'mesa', 'laranja', 'morango', 'uva', 'computador']  # Lista de palavras
    palavra = random.choice(palavras)  # Escolha aleatória de uma palavra
    letras_corretas = set()
    letras_erradas = set()
    tentativas = 6

    while True:
        # Exibir estado atual da palavra
        for letra in palavra:
            if letra in letras_corretas:
                print(letra, end=' ')
            else:
                print('_', end=' ')
        print('\n')

        # Verificar se o jogador ganhou ou perdeu
        if letras_corretas == set(palavra):
            print('Parabéns! Você ganhou!')
            break
        elif tentativas == 0:
            print('Você perdeu! A palavra era:', palavra)
            break

        # Exibir letras erradas e tentativas restantes
        if len(letras_erradas) > 0:
            print('Letras erradas:', ', '.join(letras_erradas))
        print(f'Tentativas restantes: {tentativas}\n')

        # Obter uma nova letra do jogador
        letra_jogador = input('Digite uma letra: ').lower()

        # Verificar se a letra já foi usada
        if letra_jogador in letras_corretas or letra_jogador in letras_erradas:
            print('Essa letra já foi usada. Tente novamente.\n')
            continue

        # Verificar se a letra está na palavra
        if letra_jogador in palavra:
            letras_corretas.add(letra_jogador)
        else:
            letras_erradas.add(letra_jogador)
            tentativas -= 1

        print()

jogar_forca()
