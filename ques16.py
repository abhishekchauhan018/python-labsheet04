data = {"A": 50, "B": 20, "C": 40, "D": 10}

items = list(data.items())

for i in range(len(items)):
    for j in range(len(items) - i - 1):
        if items[j][1] > items[j + 1][1]:
            items[j], items[j + 1] = items[j + 1], items[j]

result = {}
for key, value in items:
    result[key] = value

print("Dictionary sorted by values:", result)