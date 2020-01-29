from adventofcode2017.day4.passphrase import isValidPassphrase, isValidPassphraseAnagram
from adventofcode2017.asserts import assertEquals
from adventofcode2017.reader import read

def test():
    assertEquals(True, isValidPassphrase("aa bb cc dd ee"))
    assertEquals(False, isValidPassphrase("aa bb cc dd aa"))
    assertEquals(True, isValidPassphrase("aa bb cc dd aaa"))

    assertEquals(True, isValidPassphraseAnagram("abcde fghij"))
    assertEquals(False, isValidPassphraseAnagram("abcde xyz ecdab"))
    assertEquals(True, isValidPassphraseAnagram("a ab abc abd abf abj"))
    assertEquals(True, isValidPassphraseAnagram("iiii oiii ooii oooi oooo"))
    assertEquals(False, isValidPassphraseAnagram("oiii ioii iioi iiio"))
    

def countValidPassphrases():
    passphrases = read("adventofcode2017/day4/input.txt").split("\n")
    return sum(map(lambda phrase: 1 if isValidPassphraseAnagram(phrase) else 0, passphrases))

def doTest(passphrase, isValid):
    assertEquals(isValid, isValidPassphrase(passphrase))
