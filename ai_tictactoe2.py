def printBoard(board):
        print("",board[0][0],"|",board[0][1],"|",board[0][2])
        print("---|---|---")
        print("",board[1][0],"|",board[1][1],"|",board[1][2])
        print("---|---|---")
        print("",board[2][0],"|",board[2][1],"|",board[2][2])

def shift(p):
    if p == "o":
        p = "x"
    else:
        p = "o"
    return p

def play(player, board, column, row):
    if row < 0 or column < 0 or column > len(board) or row > len(board):
        print("jogada invalida")
        return -1
    elif board[row][column] != " ":
        print("jogada invalida")
        return -1
    else:
        board[row][column] = player
def isMovesLeft(board) :
    jV = []
    for i in range(3) :
        for j in range(3) :
            if (board[i][j] == ' ') :
                jV.append([i,j])   
    return jV
    
def checkVictory(board, p):
    if board[1][1] == p:
        if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            return -1
        elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
            return -1
    for col in range(len(board)):
        if board[0][col] == board[1][col] and board[1][col] == board[2][col]:
            if board[0][col] == p:
                return -1
    for row in range(len(board)):
        if board[row][0] == board[row][1] and board[row][1] == board[row][2]:
            if board[row][0] == p:
                return -1
    if len(isMovesLeft(board)) == 0:
        return 0
    return
def evaluate(b, h, c) :
    if checkVictory(b, c) == -1:
        return 10
    elif checkVictory(b, h) == -1:
        return -10
    else:
        return 0
def deep(board, depth, isMax, h, c) :
    score = evaluate(board, h, c)
    if (score == 10) :
        return score
    if (score == -10) :
        return score
    if (len(isMovesLeft(board)) == 0) :
        return 0
    else:
        jV = isMovesLeft(board)
    if (isMax) :    
        best = -1000
        for i in jV:
            board[i[0]][i[1]] = c
            best = max( best, deep(board, depth + 1, not isMax, h, c) )
            board[i[0]][i[1]] = ' '
        return best
    else :
        best = 1000
        for i in jV: 
            board[i[0]][i[1]] = h
            best = min(best, deep(board, depth + 1, not isMax, h, c))
            board[i[0]][i[1]] = ' '
        return best
def findBestMove(board, h, c) :
    jV = isMovesLeft(board)
    bestVal = -1000
    bestMove = (-1, -1)
    for i in jV:
        board[i[0]][i[1]] = c
        moveVal = deep(board, 0, False, h, c)
        board[i[0]][i[1]] = ' '
        if (moveVal > bestVal) :    
            bestMove = i
            bestVal = moveVal
    return bestMove