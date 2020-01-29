from adventofcode2017.day3.spiral import computeManhattanDistance
from adventofcode2017.asserts import assertEquals

def test():
    doTest(1, 0)
    doTest(12, 3)
    doTest(23, 2)
    doTest(1024, 31)

def doTest(input, expected):
    result = computeManhattanDistance(input)
    assertEquals(expected, result)