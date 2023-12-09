import csv

def add_todo(file_name):
    print("\nAdd todo:\n")
    # ask the title of the to-do item
    todo_name = input("Enter title of to-do: ")
    # insert that value into the file - list.csv
    with open(file_name, "a") as f:
        writer = csv.writer(f)
        # while inserting - title = user input
        #    - completed = False
        writer.writerow([todo_name, "False"])

def remove_todo(file_name):
    print("\nRemove todo:\n")

def complete_todo(file_name):
    print("\nMark todo as complete:\n")

def view_todo(file_name):
    print("\nView todo list:\n")
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        reader.__next__()
        for row in reader:
            if (row[1] == "True"):
                print(f"* {row[0]} is completed\n")
            else:
                print(f"* {row[0]} is not complete\n")