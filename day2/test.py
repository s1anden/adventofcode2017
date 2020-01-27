from adventofcode2017.day2.checksum import computeChecksum, computeDivisibleChecksum
from adventofcode2017.asserts import assertEquals
from adventofcode2017.reader import read

def test():
    doTest("5 1 9 5\n7 5 3\n2 4 6 8", 18)
    doDivisibleTest("5 9 2 8\n9 4 7 3\n3 8 6 5", 9)
    
    input = read("adventofcode2017/day2/input.txt")
    print(computeDivisibleChecksum(parseInput(input)))

def doTest(input, expected):
    parsedInput = parseInput(input)
    actual = computeChecksum(parsedInput)
    assertEquals(expected, actual)

def doDivisibleTest(input, expected):
    parsedInput = parseInput(input)
    actual = computeDivisibleChecksum(parsedInput)
    assertEquals(expected, actual)

def parseInput(input):
    lines = input.split("\n")
    result = []
    for line in lines:
        chars = line.split()
        digits = []
        for char in chars:
            digits.append(int(char))
        result.append(digits)
    return result