sequence = raw_input("Please enter a sequence to be tested: ")

def rna(sequence):
    answer = ""
    for character in sequence:
        if character.lower() == "g":
            answer += "C"
        elif character.lower() == "c":
            answer += "G"
        elif character.lower() == "t":
            answer += "A"
        elif character.lower() == "a":
            answer += "U"
        else:
            print "Oops! Looks like you had acharacter in there that wasn't a valid nucleotide."
            break
    return answer

print rna(sequence)
