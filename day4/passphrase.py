def isValidPassphrase(phrase):
    words = phrase.split()
    uniqueWords = set()
    for word in words:
        if word in uniqueWords:
            return False
        uniqueWords.add(word)
    return True

def isValidPassphraseAnagram(phrase):
    words = phrase.split()
    rearrangedWords = set()
    for word in words:
        alphabetical = arrangeAlphabetically(word)
        if alphabetical in rearrangedWords:
            return False
        rearrangedWords.add(alphabetical)
    return True

def arrangeAlphabetically(word):
    return ''.join(sorted(word))