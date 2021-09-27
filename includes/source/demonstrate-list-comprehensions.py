L = [(x, y) for x in range(6) if x % 2 == 0 for y in range(6) if y % 3 == 0]

print(L)

L = []
for x in range(6):
    if x % 2 == 0:
        for y in range(6):
            if y % 3 == 0:
                L.append((x, y))

print(L)

