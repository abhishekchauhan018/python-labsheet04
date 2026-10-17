data = {"A": 50, "B": 80, "C": 40, "D": 70}

if data:
    first = True

    for key, value in data.items():
        if first or value > maximum:
            maximum = value
            max_key = key
            first = False

    print("Key with maximum value:", max_key)
    print("Maximum value:", maximum)
else:
    print("Dictionary is empty")