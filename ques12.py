marks = {}
n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    score = float(input("Enter marks: "))
    marks[name] = score

if marks:
    first = True

    for name, score in marks.items():
        if first:
            maximum = minimum = score
            first = False
        else:
            if score > maximum:
                maximum = score
            if score < minimum:
                minimum = score

    print("Maximum marks:", maximum)
    print("Minimum marks:", minimum)
else:
    print("No records available")