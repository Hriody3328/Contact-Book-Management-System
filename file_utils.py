import csv

def load_contacts(file_name):
    try:
        with open(file_name, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []

def save_contact(file_name, contact):
    with open(file_name, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Email", "Phone", "Address"])
        if file.tell() == 0:  # Check if file is empty
            writer.writeheader()
        writer.writerow(contact)

def save_all_contacts(file_name, contacts):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Email", "Phone", "Address"])
        writer.writeheader()
        writer.writerows(contacts)
