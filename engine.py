#list of lists containing the board, note that zero represents a blank space
board = [[0, 8, 0, 0, 1, 0, 0, 7, 0],
         [5, 0, 0, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 8, 3, 9, 0, 0, 0],
         [0, 0, 8, 9, 0, 7, 1, 0, 0],
         [3, 0, 7, 0, 5, 0, 2, 0, 9],
         [0, 0, 1, 2, 0, 3, 6, 0, 0],
         [0, 0, 0, 5, 2, 4, 0, 0, 0],
         [4, 0, 0, 0, 0, 0, 0, 0, 8],
         [0, 1, 0, 0, 9, 0, 0, 5, 0]]

# traverse from top left to bottom right horizontally from left to right
# recursively guess spots until we reach the end of the board or the board is unsolvable
def backtracker(row, col):
    if col >= len(board[row]):
        col = 0 #reset column and advance row
        row += 1
        if row >= len(board):
            return True #reached the end of the board
    #make sure we ony guess numbers on blank spaces
    if board[row][col] != 0:
        return backtracker(row, col+1)

    for num in range(1,10):
        if checkConstraints(num, row, col):
            board[row][col] = num
            if backtracker(row, col+1):
                return True
            board[row][col] = 0 #must clear the spot if our guess was wrong

    return False

def checkConstraints(num, row, col):
    #check the column
    for rows in board:
        if num == rows[col]: return False

    #check the row
    for colVal in board[row]:
         if num == colVal: return False

    #check 3x3 grid
    horizontalBoxCoord = row // 3 * 3
    verticalBoxCoord = col // 3 * 3
    i = horizontalBoxCoord
    while i < horizontalBoxCoord + 3:
        j = verticalBoxCoord
        while j < verticalBoxCoord + 3:
            if num == board[i][j]: return False
            j += 1
        i += 1
    return True

def printBoard(board):
    for row in board:
        row_str = ""
        for value in row:
            row_str += str(value) + " "
        print(row_str)

def inputBoard():
    while True:
        board = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
        row = 0
        while row < 9:
            print(f"row{row}:")
            col = 0
            while col < 9:
                try:
                    val = int(input("input number between 0 and 9:\n"))
                    if val >= 0 and val <= 9:
                        board[row][col] = val
                    else:
                        print("try again")
                        continue
                except:
                    col += 1
                    continue
                col += 1
            row += 1
        print("your inputed board:")
        printBoard(board)
        response = input("is this correct? y/n")
        if response[0].lower() == 'y':
            break
        else:
            print("input board again")


# inputBoard()
# backtracker(0, 0)
printBoard(board)


