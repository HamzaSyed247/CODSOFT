# Contact book data structure
contacts = []

# Function to add a new contact
def add_contact():
    name = input("Enter contact name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contact = {
        "Name": name,
        "Phone Number": phone_number,
        "Email": email,
        "Address": address,
    }
    contacts.append(contact)
    print("Contact added successfully.")

# Function to view all contacts
def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. {contact['Name']}: {contact['Phone Number']}")

# Function to search for a contact
def search_contact(query):
    results = []
    for contact in contacts:
        if query in contact["Name"] or query in contact["Phone Number"]:
            results.append(contact)
    
    if not results:
        print("No matching contacts found.")
    else:
        print("Matching Contacts:")
        for contact in results:
            print(f"Name: {contact['Name']}")
            print(f"Phone Number: {contact['Phone Number']}")
            print(f"Email: {contact['Email']}")
            print(f"Address: {contact['Address']}")
            print("")

# Function to update a contact
def update_contact():
    view_contacts()
    index = int(input("Enter the index of the contact to update: ")) - 1

    if 0 <= index < len(contacts):
        name = input("Enter updated name: ")
        phone_number = input("Enter updated phone number: ")
        email = input("Enter updated email: ")
        address = input("Enter updated address: ")

        contacts[index]["Name"] = name
        contacts[index]["Phone Number"] = phone_number
        contacts[index]["Email"] = email
        contacts[index]["Address"] = address

        print("Contact updated successfully.")
    else:
        print("Invalid index. No contact updated.")

# Function to delete a contact
def delete_contact():
    view_contacts()
    index = int(input("Enter the index of the contact to delete: ")) - 1

    if 0 <= index < len(contacts):
        del contacts[index]
        print("Contact deleted successfully.")
    else:
        print("Invalid index. No contact deleted.")

# User Interface
while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        query = input("Enter a name or phone number to search: ")
        search_contact(query)
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")
