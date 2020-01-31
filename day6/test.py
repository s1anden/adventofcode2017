from adventofcode2017.asserts import assertEquals

def test():
    doTest("0\t2\t7\t0")
    doTest("11	11	13	7	0	15	5	5	4	4	1	1	7	1	15	11")


def doTest(input):
    banks = list(map(lambda bank: int(bank), input.split()))
    cycles, firstRepeat = findNumDistributionsBeforeFirstRepeat(banks)
    print("First repeat found in ", cycles, " cycles: ", firstRepeat)
    
    cyclesToNextRepeat = findNumDistributionsBeforeInitialRepeats(firstRepeat)
    print("Repeat of first seen config seen in ", cyclesToNextRepeat, " cycles")

def findNumDistributionsBeforeFirstRepeat(banks):
    previousConfigurations = set()
    while stringify(banks) not in previousConfigurations:
        previousConfigurations.add(stringify(banks))
        reallocateMemory(banks)
    return len(previousConfigurations), banks

def findNumDistributionsBeforeInitialRepeats(banks):
    initialConfiguration = stringify(banks)
    cycles = 0
    while True:
        reallocateMemory(banks)
        cycles += 1
        if (stringify(banks) == initialConfiguration):
            break
    return cycles

def stringify(banks):
    return ''.join(map(lambda blocks: str(blocks), banks))

def reallocateMemory(banks):
    largestBankBlocks = max(banks)
    largestBankIdx = banks.index(largestBankBlocks)
    banks[largestBankIdx] = 0
    distributeMemory(banks, largestBankBlocks, nextIdx(largestBankIdx, len(banks)))

def distributeMemory(banks, blocks, startIdx):
    idx = startIdx
    while blocks > 0:
        banks[idx] += 1
        blocks -= 1
        idx = nextIdx(idx, len(banks))

def nextIdx(index, length):
    return (index + 1) % length