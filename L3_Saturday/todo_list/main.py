from todo_functions import add_todo, remove_todo, complete_todo, view_todo

file_name = "list.csv"

try:
    # open the file in read mode
    todo_file = open(file_name, "r")
    todo_file.close()
    print("In try block")
    # if it throws error, it means the file doesn't exist
    # if no error, it means the file exist
except FileNotFoundError:
    # Now, we know the file doesn't exist
    # Create the file
    todo_file = open(file_name, "w")
    # We can also insert the first line into the file
    todo_file.write("title,completed\n")
    todo_file.close()
    print("In except block")

print("Welcome to your TODO List")

def create_menu():
    print("1. Enter 1 to add item to your list")
    print("2. Enter 2 to remove item from your list")
    print("3. Enter 3 to mark an item as completed")
    print("4. Enter 4 to view your todo list")
    print("5. Enter 5 to exit\n")
    choice = input("Enter your selection: ")
    return choice

users_choice = ""

while users_choice != "5":
    users_choice = create_menu()
    if (users_choice == "1"):
        add_todo(file_name)
    elif (users_choice == "2"):
        remove_todo(file_name)
    elif (users_choice == "3"):
        complete_todo(file_name)
    elif (users_choice == "4"):
        view_todo(file_name)
    elif (users_choice == "5"):
        continue
    else:
        print("Invalid Input - Please input 1-5")
        
print("Thank you for using todo list! \ngood bye!")