import numpy as np
import pandas as pd


def display_menu(df):
    print("\nAvailable Numeric Columns:")

    numeric_columns = df.select_dtypes(include=np.number).columns.tolist()

    for i, column in enumerate(numeric_columns, start=1):
        print(f"{i}. {column}")

    return numeric_columns


def generate_report(data, column_name):
    print("\n" + "=" * 45)
    print(f"STATISTICAL REPORT FOR '{column_name.upper()}'")
    print("=" * 45)

    print(f"Count                : {len(data)}")
    print(f"Mean                 : {np.mean(data):.2f}")
    print(f"Median               : {np.median(data):.2f}")
    print(f"Minimum              : {np.min(data)}")
    print(f"Maximum              : {np.max(data)}")
    print(f"Range                : {np.ptp(data):.2f}")
    print(f"Variance             : {np.var(data):.2f}")
    print(f"Standard Deviation   : {np.std(data):.2f}")

    unique, counts = np.unique(data, return_counts=True)
    mode = unique[np.argmax(counts)]
    print(f"Mode                 : {mode}")

    print(f"25th Percentile      : {np.percentile(data,25):.2f}")
    print(f"50th Percentile      : {np.percentile(data,50):.2f}")
    print(f"75th Percentile      : {np.percentile(data,75):.2f}")

    print("=" * 45)


def main():

    try:
        df = pd.read_csv("sample_data.csv")
    except FileNotFoundError:
        print("Dataset not found.")
        return

    print("\nNumPy Statistics Dashboard")
    print("-" * 30)

    numeric_columns = display_menu(df)

    try:
        choice = int(input("\nSelect a column number: "))

        if choice < 1 or choice > len(numeric_columns):
            print("Invalid choice.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    column = numeric_columns[choice - 1]

    data = df[column].to_numpy()

    generate_report(data, column)


if __name__ == "__main__":
    main()