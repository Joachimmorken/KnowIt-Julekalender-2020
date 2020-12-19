ordliste = open("1.in").read().split("\n")


def palinestendrom(o):
    if len(o) == 2 or o == o[::-1]:
        return False
    i = 0
    while i < len(o) // 2 + 1:
        if o[i] == o[-i-1]:
            i += 1
        elif o[i] == o[-i-2] and o[i+1] == o[-i-1]:
            i += 2
        else:
            return False
    return True


print(len([o for o in ordliste if palinestendrom(o)]))
