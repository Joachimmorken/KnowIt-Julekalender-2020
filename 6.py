pakker = [int(x) for x in open("1.in").read().split(",")]
snop = sum(pakker)

for i in range(len(pakker) - 1, 0, -1):
    if snop % 127 == 0:
        print(snop // 127)
        break
    else:
        snop -= pakker[i]
