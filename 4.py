data = open("1.in")

d = {
    "melk": 0,
    "sukker": 0,
    "mel": 0,
    "egg": 0,
}

for line in data.read().splitlines():
    for i in line.split(","):
        d[i.split(":")[0].strip()] += int(i.split(":")[1].strip())

s = d["sukker"] // 2
me = d["melk"] // 3
m = d["mel"] // 3

print(min(s, me, m, d["egg"]))
