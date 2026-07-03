import csv
import os

FILE_NAME = "books.csv"



def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Title: ")
    author = input("Enter Author: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([book_id, title, author, "Available"])

    print("Book added successfully!")

def view_books():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print("{:<10} {:<25} {:<20} {:<10}".format(*row))


def search_book():
    search_id = input("Enter Book ID to search: ")

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        found = False
        for row in reader:
            if search_id == row["BookID"] :
                print("\nBook Found:")
                print(f"ID: {row['BookID']}")
                print(f"Title: {row['Title']}")
                print(f"Author: {row['Author']}")
                print(f"Status: {row['Status']}")
                found = True
                break

        if not found:
            print("Book not found.")

def issue_book():
    book_id = input("Enter Book ID to issue: ")

    books = []
    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["BookID"] == book_id:
                found = True
                if row["Status"] == "Available":
                    row["Status"] = "Issued"
                    print("Book issued successfully!")
                else:
                    print("Book is already issued.")
            books.append(row)

    if not found:
        print("Book not found.")
        return

    with open(FILE_NAME, "w", newline="") as file:
        fieldnames = ["BookID", "Title", "Author", "Status"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(books)


def return_book():
    book_id = input("Enter Book ID to return: ")

    books = []
    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["BookID"] == book_id:
                found = True
                if row["Status"] == "Issued":
                    row["Status"] = "Available"
                    print("Book returned successfully!")
                else:
                    print("Book is already available.")
            books.append(row)

    if not found:
        print("Book not found.")
        return

    with open(FILE_NAME, "w", newline="") as file:
        fieldnames = ["BookID", "Title", "Author", "Status"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(books)


while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")    

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        issue_book()
    elif choice == "5":
        return_book()
    elif choice == "6":
        print("Thank you!")
        break
    else:
        print("Invalid choice. Try again.")
'''

with open("books.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)
        print(row.keys())
        break
'''