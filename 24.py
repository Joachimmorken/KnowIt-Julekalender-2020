hus = open("1.in").read()
hus_tilgode = 10
hus_besokt = 0

for i in hus:
    hus_tilgode += 1 if int(i) == 1 else -1
    hus_besokt += 1
    if hus_tilgode == 0:
        break
print(hus_besokt)

# Alternativ løsning
print(hus.count("1") * 2 + 10)
