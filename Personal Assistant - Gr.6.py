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

if __name__ == "__main__":
    main()

