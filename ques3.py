numbers = list(map(int, input("Enter numbers: ").split()))
result = []

for num in numbers:
    if num >= 0:
        result.append(num)

print("List without negative numbers:", result)