nome_do_personagem = input("digite o nome do seu personagem: ")
print(f"Bem-vindo ao jogo {nome_do_personagem}!!")

while True:
    print('\n===================================================\n')
    print('O nosso objetivo é explicar o básico de cada jogo.')
    print('Os jogos que nos conseguimos te explicar são:')

    print('(1) Minecraft')
    print('(2) Roblox')
    print('(3) Subnautica')
    print('(4) Astronner')
    print('(5) Stardew valley')
    print('(6) FPS Chess')
    print('(7) Spore') 
    print('(8) Humam Fall Flat')
    print('(9) Cuphead')

    numero_escolhido = input('Digite o número do jogo que você deseja conhecer, se não deseja conhecer nenhum digite "n": ')

    if numero_escolhido == "1":
        print('\nMinecraft, é um jogo de exploração, que consiste em pegar madeira, pedra, minérios, encantamentos e pets.')
        print('Objetivo do jogo é explorar todas as dimensões, se fortalecendo e no final derrotar o dragão do ender.\n')
    elif numero_escolhido == "2":
        print('\nRoblox, é uma plataforma de jogos, com várias categorias, é grátis e pode jogar com vários amigos.')
        print('Os três mais acessados são: 1º Blox fruits, 2º brookhaven e o 3º fisch. Cada um tem propósitos diferentes como rp.\n ')
    elif numero_escolhido == "3":
        print('\nSubnautica, é um jogo de exploração no fundo do mar, no começo sair do bioma inicial já é difícil pelo medo.')
        print('Ao longo do tempo você tem que ir mais fundo, podendo encontrar leviatãs.\n')
    elif numero_escolhido == "4":
        print('\nAstronner, é um jogo de exploração, que consiste em mudar de planeta ao longo do tempo.')
        print('Cada planeta possui materiais diferentes, com esses materias é possível fazer impressoras e outros.\n')
    elif numero_escolhido == "5":
        print('\nStardew valley, é um jogo de farm e exploração, Ao longo do jogo você pode upar de nível e melhorar o colheita.')
        print('Nesse jogo você pode fazer o que quiser, pode escolher sua roupa, casar com os npcs e mais.\n')
    elif numero_escolhido == "6":
        print('\nFPS Chess, é um jogo de combate e estratégia, você pode jogar com 2 pessoas, você e seu amigo, sem pagar.')
        print('O jogo é um xadres com FPS, podendo mudar os ataques de normal para legacy.\n')
    elif numero_escolhido == "7":
        print('\nSpore, é um jogo de aventura, o seu personagem é personalizável, podendo explorar o mundo e fazer amizades.')
        print('Tem 4 fases, a célula, a criatura, a tribo e a cidade, com a DLC tem o espaço.\n')
    elif numero_escolhido == "8":
        print('\nHumam Fall Flat, é um jogo de puzzles, você pode jogar sozinho ou com vários amigos.')
        print('Ele contém várias fases com mapas diferentese e puzzles diferentes.\n')
    elif numero_escolhido == "9":
        print('\nCuphead, é um jogo de plataforma, pode jogar com 2 pessoas, você e seu amigo, o objetivo é derrotar todos os bosses. ')
        print('Quando você derrota um boss você recebe uma nota, de acordo com a dificuldade, especiais, tempo e parry.\n')
    elif numero_escolhido.lower() =="n":
        break
    else:
        print("Está opção não é válida.")

print('\n===================================================\n')

Top=input('Após essa descrição, você gostaria de fazer um top dos melhores jogos de acordo com a descrição? Responda com S ou N: ')


if Top == 'S':
    primeiro = input('\nDigite o primeiro jogo do placar: ')
    segundo = input('Digite o segundo jogo do placar: ')
    terceiro = input('Digite o terceiro jogo do placar: ')

    placar1= {'número 1': 'nº 1:', 'Jogo':{primeiro}}
    placar2= {'número 2': 'nº 2:', 'Jogo':{segundo}}
    placar3= {'número 3': 'nº 3:', 'Jogo':{terceiro}}

    Troca = Top + 'a'

    print('\nSeu top ficou assim:\n')

    for valor in placar1.values():
        print(valor)

    for valor in placar2.values():
        print(valor)
    
    for valor in placar3.values():
        print(valor)

    print ('\nVolte sempre!!\n')
else:
    print ('\nVolte sempre!!\n')

#Adicinar algo sobre tupla, lista ou dicionário.

print('sim')
