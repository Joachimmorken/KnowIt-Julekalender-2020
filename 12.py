from collections import defaultdict

generation = 0
generations = defaultdict(lambda: "")

for i in open("1.in").read().strip():
    if i == "(":
        generation += 1
    if i == ")":
        generation -= 1
    else:
        generations[generation] += i

print(max([len(i.replace("(", " ").replace("  ", " ").strip().split(" "))
           for i in generations.values()]))
