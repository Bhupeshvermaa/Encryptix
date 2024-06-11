def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email (optional): ")
    address = input("Enter address (optional): ")
    contacts[name] = {"phone": phone, "email": email, "address": address}
    print(f"Contact '{name}' added!")

def view_contacts(contacts):
    if not contacts:
        print("Contact book is empty.")
        return

    for name, info in contacts.items():
        print(f"{name}: {info['phone']}")
        if info['email']:
            print(f"  Email: {info['email']}")
        if info['address']:
            print(f"  Address: {info['address']}")

def search_contacts(contacts):
    query = input("Enter name or phone number to search: ")
    matches = [(name, info) for name, info in contacts.items() 
                if query in name or query in info['phone']]
    if matches:
        for name, info in matches:
            print(f"{name}: {info['phone']}")
            if info['email']:
                print(f"  Email: {info['email']}")
            if info['address']:
                print(f"  Address: {info['address']}")
    else:
        print("No matching contacts found.")

def update_contact(contacts):
    name = input("Enter name of contact to update: ")
    if name in contacts:
        add_contact(contacts)  # Reuse the add_contact function to update
    else:
        print(f"Contact '{name}' not found.")

def delete_contact(contacts):
    name = input("Enter name of contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted.")
    else:
        print(f"Contact '{name}' not found.")

def main():
    contacts = {}  # Use a dictionary to store contacts

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contacts")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contacts(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
