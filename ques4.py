numbers = list(map(int, input("Enter numbers: ").split()))

product = 1
for num in numbers:
    product *= num

print("Product:", product if numbers else 0)