import csv

class Student:

    def __init__(self, name, math, science, english):
        self.name = name
        self.math = math
        self.science = science
        self.english = english

    def average(self):
        return (
            self.math +
            self.science +
            self.english
        ) / 3

    def grade(self):

        avg = self.average()

        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"


students = []

with open("results.csv","r") as file:

    reader = csv.DictReader(file)

    for row in reader:

        students.append(
            Student(
                row["Name"],
                float(row["Math"]),
                float(row["Science"]),
                float(row["English"])
            )
        )

students.sort(
    key=lambda s: s.average(),
    reverse=True
)

print("Rankings")

for i, student in enumerate(students, start=1):

    print(
        f"{i}. {student.name} "
        f"Average={student.average():.2f} "
        f"Grade={student.grade()}"
    )