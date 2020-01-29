import math

# Part 1
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

# Part 2
def findFirstLargerValue(input):
    spiral = {(0,0): 1}
    coordinate = (0, 0)
    level = 0
    last = 1

    while last < input:
        (currX, currY) = coordinate
        if currY == -1 * level:
            coordinate = (currX + 1, currY)
        elif currX == level and currY < level:
            coordinate = (currX, currY + 1)
        elif currY == level and currX > (-1 * level):
            coordinate = (currX - 1, currY)
        else:
            coordinate = (currX, currY - 1)
        
        if coordinate == (level + 1, -1 * level):
            level += 1
        
        last = sumNeighbors(spiral, coordinate)
        spiral[coordinate] = last

    return last

def sumNeighbors(spiral, coordinate):
    sum = 0
    coordX, coordY = coordinate
    for x in range(coordX - 1, coordX + 2):
        for y in range(coordY - 1, coordY + 2):
            # NOTE: it's unnecessary to exclude coordinate itself here since it won't have a value
            if (x, y) in spiral:
                sum += spiral[(x, y)]
    return sum
