import numpy as np

grid =   np.matrix([[5,3,0,0,7,0,0,0,0],
                    [6,0,0,1,9,5,0,0,0],
                    [0,9,8,0,0,0,0,6,0],
                    [8,0,0,0,6,0,0,0,3],
                    [4,0,0,8,0,3,0,0,1],
                    [7,0,0,0,2,0,0,0,6],
                    [0,6,0,0,0,0,2,8,0],
                    [0,0,0,4,1,9,0,0,5],
                    [0,0,0,0,8,0,0,7,9]])

def isValidInPosition(x,y, n):
    global grid

    # check vertical and horizontal
    row = grid[x,:]
    col = grid[:,y]
    if (n in row): return False #vertical
    if (n in col): return False #horizontal

    # check local square
    xO = (x // 3) * 3
    yO = (y // 3) * 3
    block = grid[xO:xO+3,yO:yO+3]
    if (n in block): return False

    return True

print(isValidInPosition(2,1,7))    

def solveGrid():
    global grid
    for x in range(9):
        for y in range(9):
            if grid[x,y] == 0:
                for n in range(1,10):
                    if (isValidInPosition(x,y,n)):
                        grid[x,y] = n
                        solveGrid()
                        grid[x,y] = 0
                return
    print(grid)


solveGrid()