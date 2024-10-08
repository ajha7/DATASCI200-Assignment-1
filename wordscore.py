
def score_word(word):
    """
    This function takes a word and returns the score of the word and the adjusted word

    @param word: a string of letters
    @return: a tuple of the score of the word and the adjusted word
    """
    scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10, "*": 0, "?": 0}
    
    res = 0
    for char in word:
        if not char.isupper():
            word = word.replace(char, char.upper(), 1)
            continue
        char = char.lower()
        if char in scores:
            res += scores[char]
    
    return (res, word)