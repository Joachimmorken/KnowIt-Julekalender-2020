par = open("par.in").read().split("\n")
ordbok = open("1.in").read().split("\n")

limord = set()

for p in par:
    first, second = p.split(", ")
    s = list(filter(lambda w: w.startswith(first), ordbok))
    for w in s:
        if w[len(first):] + second in ordbok and w[len(first):] in ordbok:
            limord.add(w[len(first):])


print(sum([len(i) for i in limord]))
