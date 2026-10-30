with open("student.txt", "w") as file:
    file.write("Name: Rahul\n")
    file.write("Course: BCA\n")
    file.write("Semester: 1")

with open("student.txt", "r") as file:
    content = file.read()

print(content)
