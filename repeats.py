
#identifies repeat letters
def repeatLetters(word):
    repeats = {}
    for char in word:
        if ord(char) in repeats:
            repeats[ord(char)] += 1 
        else:
            repeats[ord(char)] = 1
        
    return repeats
