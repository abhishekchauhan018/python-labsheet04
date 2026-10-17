n = int(input("Enter n: "))
squares = {}

for i in range(1, n + 1):
    squares[i] = i * i

print("Square dictionary:", squares)