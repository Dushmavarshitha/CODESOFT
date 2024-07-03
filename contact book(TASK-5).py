class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address
    
    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone_number}, Email: {self.email}, Address: {self.address}"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("Contact list is empty.")
        else:
            print("\nContact List:")
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"{idx}. {contact}")
    
    def search_contact(self, keyword):
        found_contacts = []
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower() or keyword in contact.phone_number:
                found_contacts.append(contact)
        
        if not found_contacts:
            print("No matching contacts found.")
        else:
            print("\nMatching Contacts:")
            for idx, contact in enumerate(found_contacts, start=1):
                print(f"{idx}. {contact}")
    
    def update_contact(self, keyword):
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower() or keyword in contact.phone_number:
                print(f"Updating contact: {contact}")
                contact.name = input("Enter updated name: ")
                contact.phone_number = input("Enter updated phone number: ")
                contact.email = input("Enter updated email: ")
                contact.address = input("Enter updated address: ")
                print("Contact updated successfully!")
                return
        
        print("Contact not found.")

    def delete_contact(self, keyword):
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower() or keyword in contact.phone_number:
                print(f"Deleting contact: {contact}")
                self.contacts.remove(contact)
                print("Contact deleted successfully!")
                return
        
        print("Contact not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone_number, email, address)
            contact_book.add_contact(new_contact)
        
        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            keyword = input("Enter name or phone number to search: ")
            contact_book.search_contact(keyword)

        elif choice == '4':
            keyword = input("Enter name or phone number to update: ")
            contact_book.update_contact(keyword)
        
        elif choice == '5':
            keyword = input("Enter name or phone number to delete: ")
            contact_book.delete_contact(keyword)

        elif choice == '6':
            print("Exiting the Contact Management System. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
