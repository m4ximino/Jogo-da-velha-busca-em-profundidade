import ai_tictactoe2 

def checkVictory(board, p):
    aux=[]
    aux1=[]
    aux2=[]
    if board[1][1] != ' ':
        if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            print("Fim do jogo, vitoria do jogador ", p, "!")
            return -1
        elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
            print("Fim do jogo, vitoria do jogador ", p, "!")
            return -1
    for i in board:
        aux.append(i[0]), aux1.append(i[1]), aux2.append(i[2])
        if i[0] != ' ':
            if i[0] == i[1] and i[1] == i[2]:
                print("Fim do jogo, vitoria do jogador ", p, "!")
                return -1
    if aux == ["x","x","x"] or aux == ["o","o","o"] or aux1 == ["x","x","x"] or aux1 == ["o","o","o"] or aux2 == ["x","x","x"] or aux2 == ["o",'o',"o"]:
        print("Fim do jogo, vitoria do jogador ", p, "!")
        return -1
    if len(ai_tictactoe2.isMovesLeft(board)) == 0:
        print("Fim do jogo, empate!")
        return -1
    else:
        return 1 

def vsIA():
    jogador = 0
    p = "x"
    while not int(jogador) in range (1, 3):
        jogador = int(input("Selecione que jogador será 1 ou 2:"))
    if jogador == 1:
        human = 'x'
        computer = 'o'
        c = "o"
    else:
        human = 'o'
        computer = 'x'
        c = "x"
    end = 1
    board = [[' ',' ',' '], 
             [' ',' ',' '],
             [' ',' ',' '],
             ]

    while end == 1:
        print("vez do jogador ", p)
        jogada = []
        if p == c:
            for i in ai_tictactoe2.findBestMove(board, human, computer):
                jogada.append(i)
            print("AI: [ coluna:",jogada[1]+1,", linha:", jogada[0]+1,"]")
            redo = ai_tictactoe2.play(p, board, jogada[1], jogada[0])
        else:
            jogada.append(int(input("digite a coluna de sua escolha: "))-1)
            jogada.append(int(input("digite a linha de sua escolha: "))-1)
            redo = ai_tictactoe2.play(p, board, jogada[0], jogada[1])
        ai_tictactoe2.printBoard(board)
        end = checkVictory(board, p)
        if redo == -1:
            print("jogada invalida")
            p = ai_tictactoe2.shift(p)
        p = ai_tictactoe2.shift(p)

def vsPlayer():
    p = "x"
    end = 1
    board = [[' ',' ',' '], 
             [' ',' ',' '],
             [' ',' ',' '],
             ]
    while end == 1:
        print("vez do jogador ", p)
        jogada = []
        jogada.append(int(input("digite a coluna de sua escolha: "))-1)
        jogada.append(int(input("digite a linha de sua escolha: "))-1)
        redo = ai_tictactoe2.play(p, board, jogada[0], jogada[1])
        ai_tictactoe2.printBoard(board)
        end = checkVictory(board, p)
        if redo == -1:
            print("jogada invalida")
            p = ai_tictactoe2.shift(p)
        p = ai_tictactoe2.shift(p)

def menu ():
    print('Selecione uma opção: ')
    print('1 - Jogar contra o computador')
    print('2 - Jogar contra outro jogador')
    print('3 - Encerrar')
    opcao = int(input())
    while not int(opcao) in range (1,4):
        opcao = int(input("Opção invalida :"))
    if opcao == 1:
        vsIA()
        menu()
    elif opcao == 2:
        vsPlayer()
        menu()
    else:
        return

menu()
