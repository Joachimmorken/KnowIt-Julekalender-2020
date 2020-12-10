grid = [[i for i in line] for line in open("1.in").read().split("\n")]

neighbours = [(-1, 0), (+1, 0), (0, -1), (0, +1),
              (-1, -1), (-1, +1), (+1, -1), (+1, +1)]

words = [word for word in open("words.in").read().split("\n")]


def find_word(word):
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            dfs(r, c, 0, word)


matches = set()


def dfs(r, c, idx, word):
    if idx == len(word) - 1:
        matches.add(word)
    elif grid[r][c] != word[idx]:
        return False
    else:
        idx += 1
        for i in neighbours:
            try:
                if grid[r + i[0]][c + i[1]] == word[idx]:
                    dfs(r + i[0], c + i[1], idx, word)
            except:
                continue


ans = []
for w in words:
    find_word(w)
    if w not in matches:
        ans.append(w)


print(sorted(ans))
