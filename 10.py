data = [[i for i in line.split(",")]
        for line in open("1.in").read().split("\n")]
count = {}
for discipline in data:
    for i, c in enumerate(discipline):
        if c not in count:
            count[c] = len(discipline) - i - 1
        else:
            count[c] += len(discipline) - i - 1

max_c = max(count, key=lambda k: count[k])
print(f"{max_c}-{count[max_c]}")
