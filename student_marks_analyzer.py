import pandas as pd


def calculate_grade(percentage):
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


df = pd.read_csv("marks.csv")

print("\nOriginal Dataset")
print(df)

df = df.drop_duplicates()

df.fillna(0, inplace=True)

df["Total"] = df["Math"] + df["Science"] + df["English"]

df["Percentage"] = (df["Total"] / 300) * 100

df["Grade"] = df["Percentage"].apply(calculate_grade)

df["Result"] = df["Percentage"].apply(
    lambda x: "Pass" if x >= 40 else "Fail"
)

df = df.sort_values(by="Percentage", ascending=False)

print("\nTop 5 Students")
print(df.head())

print("\nStudents Who Passed")
print(df[df["Result"] == "Pass"])

print("\nStudents Who Failed")
print(df[df["Result"] == "Fail"])

print("\nAverage Marks")

print("Math :", round(df["Math"].mean(), 2))
print("Science :", round(df["Science"].mean(), 2))
print("English :", round(df["English"].mean(), 2))

print("\nHighest Scorer")
print(df.iloc[0][["Name", "Percentage"]])

print("\nLowest Scorer")
print(df.iloc[-1][["Name", "Percentage"]])

print("\nGrade Distribution")
print(df["Grade"].value_counts())

df.to_csv("cleaned_marks.csv", index=False)

print("\nCleaned dataset exported as cleaned_marks.csv")