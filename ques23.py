keys = input("Enter keys separated by spaces: ").split()
values = input("Enter values separated by spaces: ").split()

if len(keys) != len(values):
    print("Both lists must have equal lengths")
else:
    result = {}

    for i in range(len(keys)):
        result[keys[i]] = values[i]

    print("Dictionary:", result)