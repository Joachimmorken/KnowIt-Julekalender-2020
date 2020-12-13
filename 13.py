from collections import defaultdict
S = open("1.in").read().strip()

visited = defaultdict(lambda: 0)

ans = ""
for i, c in enumerate(S):
    visited[c] += 1
    if ord(c) - 97 + 1 == visited[c]:
        ans += c

print(ans)
