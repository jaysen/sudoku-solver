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
    print("vertical:")
    print(sugrid[0:9,x:x+1])
    print("horizontal:")
    print(sugrid[y:y+1,0:9])
    print()
    # check vertical and horizontal
    if (n in sugrid[0:9,x:x+1]): return False #vertical
    if (n in sugrid[y:y+1,0:9]): return False #horizontal

    # check local square
    xO = (x // 3) * 3
    yO = (y // 3) * 3
    print("local square: ")
    print(sugrid[xO:xO+3,yO:yO+3])
    print()
    if (n in sugrid[xO*3:xO*3+3,yO*3:yO*3+3]): return False

    return True

print(isValidInPosition(3,3,2))    