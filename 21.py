data = open("1.in").read().split("\n")

pasients = []
for i, line in enumerate(data):
    if (line != "---"):
        candidate, priority = line.split(",")
        pasients.append((candidate, priority))
    else:
        pasients.append(line)

queue = []
ans = 0

for p in pasients:
    if p == "---":
        queue.sort(key=lambda x: x[1])
        queue.pop(0)
        ans += 1
    else:
        queue.append(p)

queue.sort(key=lambda x: x[1])
i = 0
while queue[i][0] != "Claus":
    i += 1
    ans += 1
print(ans)
