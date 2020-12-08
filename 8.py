nodes = {}
count = {}

data = open("1.in", encoding="utf-8")

for i in range(50):
    lsplit = data.readline().strip().split(":")
    x = lsplit[1].split(",")[0].split("(")[1]
    y = lsplit[1].split(",")[1].split(")")[0][1:]
    nodes[lsplit[0]] = (int(x), int(y))
    count[lsplit[0]] = 0

locations = data.read().split("\n")


def distance(curr_pos, location_pos):
    return abs(curr_pos[0] - location_pos[0]) + abs(curr_pos[1] - location_pos[1])


def get_time(d):
    if d == 0:
        return 0
    if d < 5:
        return 0.25
    if d < 20:
        return 0.5
    if d < 50:
        return 0.75
    return 1


curr_pos = [0, 0]
for i in locations:
    i_pos = nodes[i]
    x, y = curr_pos
    while x != i_pos[0]:
        x = x + 1 if x < i_pos[0] else x - 1
        for k, v in nodes.items():
            count[k] += get_time(distance((x, y), v))

    while y != i_pos[1]:
        y = y + 1 if y < i_pos[1] else y - 1
        for k, v in nodes.items():
            count[k] += get_time(distance((x, y), v))
    curr_pos = [x, y]

print(max(list(count.values())) - min(list(count.values())))
