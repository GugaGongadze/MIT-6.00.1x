def sumOfInts(a, b):
    return a + b

def score(word, f):

    letter_scores = []

    for letter in list(enumerate(word)):
        if letter[1].isupper():
            letter_scores.append((ord(letter[1]) - 64) * letter[0])
        else:
            letter_scores.append((ord(letter[1]) - 96) * letter[0])

    return f(sorted(letter_scores, reverse=True)[0], sorted(letter_scores, reverse=True)[1])

print(score('Guga', sumOfInts))