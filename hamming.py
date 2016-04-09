sequence = raw_input("Please enter a DNA sequence to be tested: ")
sequence_2 = raw_input("Great! Please enter another sequence so we can compare them: ")

def hamming(x, y):
    answer = 0

    if len(x) == len(y):
        for num in xrange(0, len(x)):
            if x[num] != y[num]:
                answer += 1
    else:
        print "You need to enter two sequences of the same length!"
    return answer

print hamming(sequence, sequence_2)
