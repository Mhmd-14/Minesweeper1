
#Define a function called mines which is similar to minesweeper chessboard game
#The code will get the number of rows and columns as arguments when the function is called
#The code will return the number of mines available around the "." in all directions : Horizantally, vertically and diagonal
#For example you choose the number of rows 4 and the number of columns 5 and you fill the board as below
#Note you should fill the board either with '*' which is the mine or a dot '.'
#The original matrix you filled is
# [. * . * *]
# [* . . * .]
# [* * . * *]
# [. . * . .]

#The result matrix will be
# [[2, '*', 3, '*', '*']
#  ['*', 4, 5, '*', 5]
#  ['*', '*', 4, '*', '*']
#  ['.', 3, '*', 3, '.']]

def mines(rows,columns):
    adjacent = 0
#Creating the matrix "chessboard" with m: rows, n:columns and filling it with zeroes
    board = [[0 for x in range(0,columns,1)]for y in range(0,rows,1)] 
#Creating a loop to fill the chessboard from the user
    for i in range(0,rows,1):
        for j in range(0,columns,1):
            board[i][j] = input("Please enter a star '*' or space:\t")
        print()

#Create loop to check the top left at corner
    if board[0][0] == ".":
        for i in range(0,2,1):
            for j in range(0,2,1):
                if board[i][j] == "*":
                    adjacent +=1
                    board[0][0] = adjacent
    adjacent = 0
#Create loop to check the top right at corner
    if board[0][columns-1] == ".":
        for i in range(0,2,1):
            for j in range(columns-1,columns-2,-1):
                if board[i][j] == "*":
                    adjacent +=1
                    board[0][columns-1] = adjacent
    adjacent = 0
#Create loop to check the bottom left at corner
    if board[rows-1][0] == ".":
        for i in range(rows-1,rows-2,-1):
            for j in range(0,2,1):
                if board[i][j] == "*":
                    adjacent +=1
                    board[rows-1][0] = adjacent
    adjacent = 0
#Create loop to check the bottom right at corner
    if board[rows-1][columns-1] == ".":
        for i in range(rows-1,rows-2,-1):
            for j in range(columns-1,columns-1,-1):
                if board[i][j] == "*":
                    adjacent +=1
                    board[rows-1][columns-1] = adjacent
    adjacent = 0
#Create loop to check the first row if contain a dot except a boundary
    for i in range(0,1,1):
        for j in range(1,columns-1,1):
            if board[i][j] == ".":
                for k in range(i,i+2,1):
                    for l in range(j-1,j+2,1):
                        if board[k][l] == "*":
                            adjacent +=1
                            board[i][j] = adjacent
            adjacent =0
#Create loop to check the last row if contain a dot except a boundary
    for i in range(rows-1,rows,1):
        for j in range(1,columns-1,1):
            if board[i][j] == ".":
                for k in range(i,i-2,-1):
                    for l in range(j-1,j+2,1):
                        if board[k][l] == "*":
                            adjacent +=1
                            board[i][j] = adjacent
            adjacent =0
#Create loop to check the first column if contain a dot except a boundary
    for i in range(1,rows-1,1):
        for j in range(0,1,1):
            if board[i][j] == ".":
                for k in range(i-1,i+2,1):
                    for l in range(j,j+2,1):
                        if board[k][l] == "*":
                            adjacent +=1
                            board[i][j] = adjacent
            adjacent =0
#Create loop to check the last column if contain a dot except a boundary
    for i in range(1,rows-1,1):
        for j in range(columns-1,columns,1):
            if board[i][j] == ".":
                for k in range(i-1,i+2,1):
                    for l in range(j,j-2,-1):
                        if board[k][l] == "*":
                            adjacent +=1
                            board[i][j] = adjacent
            adjacent =0
#Create loop to check all the remaining spaces except the above ones
    for i in range(1,rows,1):
        for j in range(1,columns-1,1):
            if board[i][j] == ".":
                for k in range(i-1,i+2,1):
                    for l in range(j-1,j+2,1):
                        if board[k][l] == "*":
                            adjacent +=1
                            board[i][j] = adjacent
            adjacent = 0
    return board
print(mines(4,5))







