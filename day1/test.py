from adventofcode2017.day1.captcha import solveCaptchaNextDigit, solveCaptchaHalfwayRound
from adventofcode2017.asserts import assertEquals

def test():
    testNextDigit("1122", 3)
    testNextDigit("1111", 4)
    testNextDigit("1234", 0)
    testNextDigit("91212129", 9)

    testHalfwayRound("1212", 6)
    testHalfwayRound("1221", 0)
    testHalfwayRound("123425", 4)
    testHalfwayRound("123123", 12)
    testHalfwayRound("12131415", 4)

# input is a string of digits, expected is a number
def testNextDigit(input, expected):
    resultNext = solveCaptchaNextDigit(input)
    assertEquals(expected, resultNext)

def testHalfwayRound(input, expected):
    resultHalf = solveCaptchaHalfwayRound(input)
    assertEquals(expected, resultHalf)