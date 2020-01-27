def computeChecksum(sheet):
    sum = 0
    for record in sheet:
        sum += (max(record) - min(record))
    return sum

def computeDivisibleChecksum(sheet):
    sum = 0
    for record in sheet:
        sum += findEvenDivisibleResult(record)
    return sum


def findEvenDivisibleResult(record):
    for idx in range(len(record)):
        for idx2 in range(idx + 1, len(record)):
            bigger = max(record[idx], record[idx2])
            smaller = min(record[idx], record[idx2])
            if bigger % smaller == 0:
                return bigger / smaller
    raise Exception('Could not find an evenly divisible pair in record: ', record)