numbers = list(map(int, input("Enter numbers: ").split()))
sorted_list = True

for i in range(len(numbers) - 1):
    if numbers[i] > numbers[i + 1]:
        sorted_list = False
        break

if sorted_list:
    print("List is sorted in ascending order")
else:
    print("List is not sorted")