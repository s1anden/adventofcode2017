from adventofcode2017.asserts import assertEquals
from adventofcode2017.reader import read

def test():
    assertEquals(5, countSteps([0, 3, 0, 1, -3]))

    input = list(map(lambda instr: int(instr), read("adventofcode2017/day5/input.txt").split()))
    print(countSteps(input))

def countSteps(instructions):
    idx = 0
    steps = 0
    while idx >= 0 and idx < len(instructions):
        instruction = instructions[idx]
        instructions[idx] += 1
        idx += instruction
        steps += 1
    return steps
    