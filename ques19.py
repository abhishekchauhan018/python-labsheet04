student = {"name": "Abhishek", "marks": 75, "roll": 101}

key = input("Enter key to search: ")

if key in student:
    print("Key exists")
    print("Value:", student[key])
else:
    print("Key does not exist")