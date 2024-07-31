

def make_lists(letters):
    alphabet = []
    indices = []
    for number, letter in enumerate(letters,1):
        alphabet.append(letter)
        indices.append(number)
    return alphabet,indices


L = "abcdefghijklmnopqrstuvwxyz"
print(make_lists(L))
