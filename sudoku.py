import numpy as np

GRIDSIZE = 9
fullSet = {1, 2, 3, 4, 5, 6, 7, 8, 9}

sugrid = np.matrix([[5,3,0,0,7,0,0,0,0],
                    [6,0,0,1,9,5,0,0,0],
                    [0,9,8,0,0,0,0,6,0],
                    [8,0,0,0,6,0,0,0,3],
                    [4,0,0,8,0,3,0,0,1],
                    [7,0,0,0,2,0,0,0,6],
                    [0,6,0,0,0,0,2,8,0],
                    [0,0,0,4,1,9,0,0,5],
                    [0,0,0,0,8,0,0,7,9]])

def isValidInPosition(x, y, n):
    #test prints:
    print(sugrid[0:9,y-1:y])
    print(sugrid[x-1:x,0:9])
    
    # check vertical and horizontal
    if (n in sugrid[0:9,y-1:y]): return False #vertical
    if (n in sugrid[x-1:x,0:9]): return False #horizontal

    # check local square
    #TODO
    
    return True

print(isValidInPosition(3,3,2))    