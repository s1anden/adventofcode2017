# input is a string composed of digits between 1 and 9 inclusive
def solveCaptchaNextDigit(input):
    sum = 0
    for idx in range(len(input)):
        digit = input[idx]
        next = input[(idx + 1) % len(input)]
        if digit == next:
            sum += int(digit)
    return sum

def solveCaptchaHalfwayRound(input):
    sum = 0
    for idx in range(len(input)):
        digit = input[idx]
        next = input[(idx + int(len(input) / 2)) % len(input)]
        if digit == next:
            sum += int(digit)
    return sum