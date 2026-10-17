numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

total = 0
for num in numbers:
    total += num

if len(numbers) > 0:
    average = total / len(numbers)
    print("Sum:", total)
    print("Average:", average)
else:
    print("List is empty")