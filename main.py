
    print()
    userInput = int(input("Enter the id of the student you want to delete: "))

    global database
    database.remove(userInput-1)

    print("Student removed!")

def print_error():
    print("Invalid choice!")

def main_menu():
    while True:
        print()
        print("=== SUNWAY TECH CLUB MANAGEMENT SOFTWARE ===")
        print("1. Create member")
        print("2. View member")
        print("3. Edit member")
        print("4. Delete member")
        print("5. Exit")
        
        choice = int(input("Please choose an option: "))

        if choice == 5:
            print()
            print("Have a nice day!")
            break

        switcher = {
            1: create,
            2: view,
            3: edit,
            4: delete,
        }

        

def main():
    main_menu()

if __name__ == "__main__":
    main()