student = {"name": "Abhishek", "marks": 75, "roll": 101}

key = input("Enter key to remove: ")

if key in student:
    del student[key]
    print("Updated dictionary:", student)
else:
    print("Key not found")