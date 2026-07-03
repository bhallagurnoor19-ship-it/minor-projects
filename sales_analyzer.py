import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("sales_data.csv")

print("\nOriginal Dataset")
print(df.head())


print("\nChecking Missing Values")
print(df.isnull().sum())


df = df.drop_duplicates()

df["Sales"] = df["Sales"].fillna(df["Sales"].mean())
df["Profit"] = df["Profit"].fillna(df["Profit"].mean())

df.to_csv("cleaned_sales.csv", index=False)


print("\nDataset Information")
print(df.info())


print("\nSummary Statistics")
print(df.describe())


print("\n-----------------------------")
print("BUSINESS QUESTIONS")
print("-----------------------------")


print("\n1. Total Sales")
print(df["Sales"].sum())


print("\n2. Total Profit")
print(df["Profit"].sum())


print("\n3. Average Sales")
print(df["Sales"].mean())


print("\n4. Average Profit")
print(df["Profit"].mean())


print("\n5. Sales by Region")
print(df.groupby("Region")["Sales"].sum())


print("\n6. Profit by Region")
print(df.groupby("Region")["Profit"].sum())


print("\n7. Best Performing Region")
best_region = df.groupby("Region")["Sales"].sum().idxmax()
print(best_region)


print("\n8. Highest Selling Product")
best_product = df.groupby("Product")["Sales"].sum().idxmax()
print(best_product)


print("\n9. Best Salesperson")
best_person = df.groupby("Salesperson")["Sales"].sum().idxmax()
print(best_person)


print("\n10. Average Profit by Product")
print(df.groupby("Product")["Profit"].mean())


region_sales = df.groupby("Region")["Sales"].sum()

plt.figure(figsize=(7,5))
region_sales.plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()


product_sales = df.groupby("Product")["Sales"].sum()

plt.figure(figsize=(7,5))
product_sales.plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.title("Sales Distribution by Product")
plt.tight_layout()
plt.show()