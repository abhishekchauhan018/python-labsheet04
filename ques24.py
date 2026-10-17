data = {"A": 1, "B": 2, "C": 3}
inverted = {}

for key, value in data.items():
    inverted[value] = key

print("Original dictionary:", data)
print("Inverted dictionary:", inverted)