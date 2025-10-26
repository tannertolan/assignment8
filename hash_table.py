# Contact class
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    # String version of a contact
    def __str__(self):
        return f"{self.name} | {self.phone} | {self.email}"


# ContactBook class
class ContactBook:
    def __init__(self):
        self.contacts = []

    # Add contact
    def add_contact(self, name, phone, email):
        self.contacts.append(Contact(name, phone, email))
        print("Contact added.")

    # Show all contacts
    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for i, contact in enumerate(self.contacts, 1):
                print(f"{i}. {contact}")

    # Search contact
    def search_contact(self, name):
        found = [c for c in self.contacts if name.lower() in c.name.lower()]
        if found:
            for contact in found:
                print(contact)
        else:
            print("No contact found.")

    # Update contact
    def update_contact(self, name, new_phone=None, new_email=None):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                if new_phone:
                    contact.phone = new_phone
                if new_email:
                    contact.email = new_email
                print("Contact updated.")
                return
        print("Contact not found.")

    # Delete contact
    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print("Contact deleted.")
                return
        print("Contact not found.")

    # Save contacts
    def save_contacts(self, filename="contacts.txt"):
        with open(filename, "w") as f:
            for contact in self.contacts:
                f.write(f"{contact.name},{contact.phone},{contact.email}\n")
        print("Contacts saved to file.")

    # Load contacts
    def load_contacts(self, filename="contacts.txt"):
        try:
            with open(filename, "r") as f:
                for line in f:
                    name, phone, email = line.strip().split(",")
                    self.contacts.append(Contact(name, phone, email))
            print("Contacts loaded from file.")
        except FileNotFoundError:
            print("No file found. Starting fresh.")


# Main function
def main():
    book = ContactBook()
    book.load_contacts()

    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Save & Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            book.add_contact(name, phone, email)
        elif choice == "2":
            book.view_contacts()
        elif choice == "3":
            name = input("Search name: ")
            book.search_contact(name)
        elif choice == "4":
            name = input("Name to update: ")
            new_phone = input("New phone (leave blank to skip): ")
            new_email = input("New email (leave blank to skip): ")
            book.update_contact(name, new_phone or None, new_email or None)
        elif choice == "5":
            name = input("Name to delete: ")
            book.delete_contact(name)
        elif choice == "6":
            book.save_contacts()
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


# Run program
if __name__ == "__main__":
    main()
