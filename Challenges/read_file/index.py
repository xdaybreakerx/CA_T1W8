def show_shopping_list():
    with open("shopping_list.txt", "r") as file:
        for line in file:
            print(f"* {line.strip()}")
            
if __name__ == '__main__':
    show_shopping_list()