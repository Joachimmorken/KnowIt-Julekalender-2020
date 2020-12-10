
grid = [[i for i in line] for line in open("1.in").read().split("\n")]

neighbours = [(-1, 0), (+1, 0), (0, -1), (0, +1)]


def traverse(grid):
    new_grid = [row[:] for row in grid]
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            S_count = 0
            if grid[r][c] == "F":
                for n in neighbours:
                    try:
                        if grid[r + n[0]][c + n[1]] == "S":
                            S_count += 1
                    except:
                        continue
            if S_count >= 2:
                new_grid[r][c] = "S"
    return new_grid


count = 0
while grid != traverse(grid):
    count += 1
    grid = traverse(grid)
print(count + 1)
