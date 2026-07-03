import csv


def calculate_total(maths, science, english):
    return maths + science + english


def calculate_percentage(total):
    return total / 3


def assign_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def process_student_records(input_file, output_file):
    try:
        with open(input_file, "r", newline="") as infile:
            reader = csv.DictReader(infile)

            with open(output_file, "w", newline="") as outfile:
                fieldnames = [
                    "RollNo",
                    "Name",
                    "Maths",
                    "Science",
                    "English",
                    "Total",
                    "Percentage",
                    "Grade",
                ]

                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()

                for row in reader:
                    maths = int(row["Maths"])
                    science = int(row["Science"])
                    english = int(row["English"])

                    total = calculate_total(maths, science, english)
                    percentage = calculate_percentage(total)
                    grade = assign_grade(percentage)

                    writer.writerow(
                        {
                            "RollNo": row["RollNo"],
                            "Name": row["Name"],
                            "Maths": maths,
                            "Science": science,
                            "English": english,
                            "Total": total,
                            "Percentage": f"{percentage:.2f}",
                            "Grade": grade,
                        }
                    )

        print("Records processed successfully!")
        print(f"Updated file saved as '{output_file}'")

    except FileNotFoundError:
        print("Input CSV file not found.")

    except ValueError:
        print("Invalid marks found in the file.")

    except KeyError as e:
        print(f"Missing column: {e}")


process_student_records("students.csv", "student_results.csv")