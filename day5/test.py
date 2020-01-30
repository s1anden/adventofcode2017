from adventofcode2017.asserts import assertEquals
from adventofcode2017.reader import read

def test():
    assertEquals(5, countStepsSingleIncrement([0, 3, 0, 1, -3]))
    
    input = list(map(lambda instr: int(instr), read("adventofcode2017/day5/input.txt").split()))
    assertEquals(354121, countStepsSingleIncrement(input.copy()))

    assertEquals(10, countStepsIncrementTowardsZero([0, 3, 0, 1, -3]))
    print(countStepsIncrementTowardsZero(input.copy()))

def countStepsSingleIncrement(instructions):
    return countSteps(instructions, lambda instr: instr + 1)

def countStepsIncrementTowardsZero(instructions):
    return countSteps(instructions, lambda instr: instr + 1 if instr < 3 else instr - 1)

def countSteps(instructions, incrementFn):
    idx = 0
    steps = 0
    while idx >= 0 and idx < len(instructions):
        instruction = instructions[idx]
        instructions[idx] = incrementFn(instruction)
        idx += instruction
        
        steps += 1
    return steps
    