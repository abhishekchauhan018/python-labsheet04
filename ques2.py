numbers = list(map(int, input("Enter numbers: ").split()))
n = int(input("Enter number of positions to rotate: "))

if numbers:
    n = n % len(numbers)
    rotated = numbers[n:] + numbers[:n]
    print("Rotated list:", rotated)
else:
    print("List is empty")