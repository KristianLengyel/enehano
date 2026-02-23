numbers = [5, 3, 8, 5, 2, 3, 9, 1, 4, 8, 8, 6, 2, 7, 5, 3, 10, 9, 1, 5]

unikatne = []
opakujuce = []
pocet = {}

for num in numbers:
    if num in pocet:
        pocet[num] += 1
    else:
        pocet[num] = 1

    if num not in unikatne:
        unikatne.append(num)

for x, y in pocet.items():
    if y > 1:
        opakujuce.append(x)

print(f"unikatne: {unikatne}")

print(f"opakujuci: {opakujuce}")

for x, y in pocet.items():
    if y > 1:
        print(f"{x}: {y}x")
