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
    todo_name = input("Enter a to-do item that you want to remove: ")
    # copy all the contents of the csv into a new csv 
    # while doing this
    # check if todo from user is in list
    # when we encounter we do not copy that todo list
    # final new todo will be written in the csv file
    todo_lists = []
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if (row[0] != todo_name):
                todo_lists.append(row)
            else:
                continue
    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(todo_lists)
    

def complete_todo(file_name):
    print("\nMark todo as complete:\n")
    todo_lists = []
    todo_name = input("Enter the to-do name you have completed: ")
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if (row[0] != todo_name):
                todo_lists.append(row)
            else:
                todo_lists.append([row[0], "True"])
    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(todo_lists)
                

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
                