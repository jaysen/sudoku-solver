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

                    
grid =   np.matrix([[1,0,0,2,0,0,0,0,7],
                    [0,0,0,0,0,0,6,9,0],
                    [7,0,0,3,0,0,8,0,0],
                    [5,6,0,9,0,8,0,0,0],
                    [0,2,0,7,0,0,0,0,1],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,4,0,7,0,0,0,5],
                    [2,5,0,8,0,0,9,0,0],
                    [0,0,0,0,4,0,0,0,0]])


# check if n is valid at position x,y
def valid(x,y, n):
    global grid

    # check vertical and horizontal
    if (n in grid[x,:]): return False #vertical
    if (n in grid[:,y]): return False #horizontal

    # check local square
    xO = (x // 3) * 3
    yO = (y // 3) * 3
    if (n in grid[xO:xO+3,yO:yO+3]): return False

    return True


# Recursively brute force the grid to solve
# backtrack when your solution leads to something with no valid options for a cell
def solve():
    global grid
    for x in range(9):
        for y in range(9):
            if grid[x,y] == 0:
                for n in range(1,10):
                    if valid(x,y,n):
                        grid[x,y] = n
                        solve()
                        grid[x,y] = 0
                return
    print(grid)

if __name__ == "__main__":
    solve()
