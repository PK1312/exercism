sentence = raw_input("What sentence would you like to check? ")
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def pan(sentence):
    for letter in alphabet:
        if letter in sentence:
            return True
        else:
            return False
print pan(sentence)
