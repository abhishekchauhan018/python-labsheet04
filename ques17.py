student = {"name": "Abhishek", "marks": 75}

key = input("Enter key to update: ")

if key in student:
    value = input("Enter new value: ")
    student[key] = value
    print("Updated dictionary:", student)
else:
    print("Key not found")