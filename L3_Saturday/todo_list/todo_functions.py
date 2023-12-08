import csv

def add_todo(file_name):
    print("Add todo: ")
    # ask the title of the to-do item
    todo_name = input("Enter title of to-do: ")
    # insert that value into the file - list.csv
    with open(file_name, "a") as f:
        writer = csv.writer(f)
        # while inserting - title = user input
        #    - completed = False
        writer.writerow([todo_name, "False"])

def remove_todo(file_name):
    print("Remove todo: ")

def complete_todo(file_name):
    print("Mark todo as complete: ")

def view_todo(file_name):
    print("View todo list: ")