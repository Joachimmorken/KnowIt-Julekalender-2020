from itertools import zip_longest

words = open("1.in").read().split("\n")
password = "eamqia"


def transform(o):
    w1 = ""
    for i in o[1:]:
        w1 += chr(ord(i) + 1) if i != "z" else chr(ord(i) - 25)
    w2 = ""
    for i in range(len(w1)):
        w2 += chr(97 + (((ord(w1[i]) - 97) + (ord(o[i]) - 97)) % 26))
    return w2


for w in words:
    word_matrix = [list(w)]
    current = w
    while len(current) > 1:
        t = transform(current)
        word_matrix.append(list(t))
        current = t

    transposed = [list(filter(None, i)) for i in zip_longest(*word_matrix)]
    for c in transposed:
        if password in "".join(map(str, c)):
            print(w)
