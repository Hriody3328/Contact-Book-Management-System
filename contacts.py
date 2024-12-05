import csv
from file_utils import load_contacts, save_contact, save_all_contacts

CONTACTS_FILE = "contacts.csv"

def validate_name(name):
    if not name.isalpha():
        print("Error: Name must only contain alphabets.")
        return False
    return True

def validate_phone(phone):
    if not phone.isdigit() or len(phone) != 11:
        print("Error: Phone must be a 11-digit number.")
        return False
    return True

def add_contact():
    print("\n--- Add Contact ---")
    contacts = load_contacts(CONTACTS_FILE)

    while True:
        name = input("Name: ")
        if validate_name(name):
            break

    email = input("Email: ")

    while True:
        phone = input("Phone: ")
        if validate_phone(phone) and not any(contact['Phone'] == phone for contact in contacts):
            break
        elif any(contact['Phone'] == phone for contact in contacts):
            print("Error: Phone number already exists.")

    address = input("Address: ")

    contact = {"Name": name, "Email": email, "Phone": phone, "Address": address}
    save_contact(CONTACTS_FILE, contact)
    print("Contact added successfully.")

def view_contacts():
    print("\n--- All Contacts ---")
    contacts = load_contacts(CONTACTS_FILE)
    if not contacts:
        print("No contacts found.")
        return
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. Name: {contact['Name']}, Email: {contact['Email']}, Phone: {contact['Phone']}, Address: {contact['Address']}")

def search_contact():
    print("\n--- Search Contact ---")
    search_term = input("Enter name or phone to search: ").strip()
    contacts = load_contacts(CONTACTS_FILE)
    results = [contact for contact in contacts if search_term in (contact['Name'], contact['Phone'])]
    if results:
        for contact in results:
            print(f"Name: {contact['Name']}, Email: {contact['Email']}, Phone: {contact['Phone']}, Address: {contact['Address']}")
    else:
        print("No contacts found.")

def delete_contact():
    print("\n--- Delete Contact ---")
    phone = input("Enter the phone number of the contact to delete: ").strip()
    contacts = load_contacts(CONTACTS_FILE)
    updated_contacts = [contact for contact in contacts if contact['Phone'] != phone]
    if len(updated_contacts) == len(contacts):
        print("Contact not found.")
    else:
        save_all_contacts(CONTACTS_FILE, updated_contacts)
        print("Contact deleted successfully.")
