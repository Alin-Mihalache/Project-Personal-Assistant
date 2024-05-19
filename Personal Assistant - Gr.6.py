import json
 import re
class Contact:
    def __init__(self, name, address, phone, email, birthday):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        self.birthday = birthday
from datetime import datetime, timedelta
class ContactsBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def upcoming_birthdays(self, days):
        today = datetime.now().date()
        upcoming = today + timedelta(days=days)
        upcoming_birthdays = []
        for contact in self.contacts:
            if contact.birthday.month == upcoming.month and contact.birthday.day == upcoming.day:
                upcoming_birthdays.append(contact)
        return upcoming_birthdays

    def display_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}, Address: {contact.address}, Phone: {contact.phone}, Email: {contact.email}, Birthday: {contact.birthday}")

def main():
    # Create ContactsBook object
    my_contacts = ContactsBook()

    # Add sample contacts
    contact1 = Contact("Ana Maria", "Strada Livezii", "123-456-7890", "ana@example.com", datetime(1990, 8, 10))
    contact2 = Contact("Dan Iom", "Strada Tisa", "987-654-3210", "dan@example.com", datetime(1985, 3, 15))
    my_contacts.add_contact(contact1)
    my_contacts.add_contact(contact2)

    # Display all contacts
    print("All Contacts:")
    my_contacts.display_contacts()

    # Display contacts with upcoming birthdays within 7 days
    print("\nUpcoming Birthdays (within 7 days):")
    upcoming = my_contacts.upcoming_birthdays(7)
    if upcoming:
        for contact in upcoming:
            print(f"Name: {contact.name}, Birthday: {contact.birthday}")
    else:
        print("No upcoming birthdays within 7 days.")
import re
from datetime import datetime

class Contact:
    def __init__(self, name, address, phone, email, birthday):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        self.birthday = datetime.strptime(birthday, '%Y-%m-%d')

    def validate_contact(self):
        # Validează numărul de telefon și adresa de email
        phone_pattern = r'\d{3}-\d{3}-\d{4}'
        email_pattern = r'[^@]+@[^@]+\.[^@]+'
        valid_phone = re.match(phone_pattern, self.phone) is not None
        valid_email = re.match(email_pattern, self.email) is not None
        if not valid_phone or not valid_email:
            raise ValueError("Invalid phone number or email.")
        return True

class Note:
    def __init__(self, content):
        self.content = content

class ContactsBook:
    def __init__(self):
        self.contacts = []
        self.notes = []

    def add_contact(self, contact):
        if contact.validate_contact():
            self.contacts.append(contact)

    def find_contact(self, search_term):
        # Caută contacte după un termen specific
        return [contact for contact in self.contacts if search_term.lower() in contact.name.lower()]

    def edit_contact(self, name, **kwargs):
        # Editează un contact existent
        for contact in self.contacts:
            if contact.name == name:
                for key, value in kwargs.items():
                    setattr(contact, key, value)
                contact.validate_contact()  # Re-validate contact after edit

    def delete_contact(self, name):
        # Șterge un contact după nume
        self.contacts = [contact for contact in self.contacts if contact.name != name]

    def add_note(self, note):
        self.notes.append(note)

    def find_note(self, search_term):
        # Caută note după un termen specific
        return [note for note in self.notes if search_term.lower() in note.content.lower()]

    def edit_note(self, old_content, new_content):
        # Editează o notă existentă
        for note in self.notes:
            if note.content == old_content:
                note.content = new_content

    def delete_note(self, content):
        # Șterge o notă după conținut
        self.notes = [note for note in self.notes if note.content != content]

if __name__ == "__main__":
    main()

