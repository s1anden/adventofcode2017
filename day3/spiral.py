import math

def computeManhattanDistance(start):
    shellDimension = getNextOddRoot(start)
    stepsIn = math.floor(shellDimension / 2)

    midpoints = getMidpoints(shellDimension)
    stepsAround = min(map(lambda mid: math.fabs(mid - start), midpoints))
    return stepsIn + stepsAround

def getNextOddRoot(start):
    root = math.ceil(math.sqrt(start))
    return root if root % 2 != 0 else root + 1

def getMidpoints(root):
    square = root * root
    midpointLength = math.floor(root / 2)
    return map(lambda x: square - (midpointLength * x), [1, 3, 5, 7])