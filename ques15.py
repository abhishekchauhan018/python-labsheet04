data = {"banana": 20, "apple": 10, "mango": 30}

sorted_keys = sorted(data.keys())
result = {}

for key in sorted_keys:
    result[key] = data[key]

print("Dictionary sorted by keys:", result)