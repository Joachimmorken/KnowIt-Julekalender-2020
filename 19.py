data = open("1.in").read().split("\n")


def lek_en(alver, steg):
    while len(alver) > 1:
        r = steg % len(alver)
        alver = alver[-r:] + alver[:-r]
        alver.pop(0)
    return alver[0]


def lek_to(alver, steg):
    idx = 0
    while len(alver) > 1:
        r = steg % len(alver)
        alver = alver[-r:] + alver[:-r]
        alver.pop(idx)
        idx = idx + 1 if idx < len(alver) - 1 else 0
    return alver[0]


def lek_tre(alver, steg):
    while len(alver) > 2:
        r = steg % len(alver)
        alver = alver[-r:] + alver[:-r]
        mid = len(alver) // 2
        if len(alver) % 2 == 0:
            alver.pop(mid) and alver.pop(mid - 1)
        else:
            alver.pop(mid)
    r = steg % len(alver)
    alver = alver[-r:] + alver[:-r]
    return alver[1]


def lek_fire(alver, steg):
    while len(alver) > 1:
        r = steg % len(alver)
        alver = alver[-r:] + alver[:-r]
        alver.pop(len(alver) - 1)
    return alver[0]


seirende_alver = []
leker = {1: lek_en, 2: lek_to, 3: lek_tre, 4: lek_fire, }
for line in data:
    lek, steg, alver = line.split(" ", 2)
    alver = alver.replace(" ", "")[1:-1].split(",")
    seirende_alver.append(leker[int(lek)](alver, int(steg)))

print(max(seirende_alver, key=seirende_alver.count))
