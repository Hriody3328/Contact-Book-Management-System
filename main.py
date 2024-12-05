from contacts import add_contact, view_contacts, search_contact, delete_contact
from constants import MENU_OPTIONS

def display_menu():
    print("\nContact Book Management System")
    for key, value in MENU_OPTIONS.items():
        print(f"{key}. {value}")
    print()

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
