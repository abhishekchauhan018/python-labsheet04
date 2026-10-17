numbers = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target sum: "))

found = False

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(numbers[i], numbers[j])
            found = True

if not found:
    print("No pairs found")