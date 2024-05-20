import json
import os
from datetime import datetime, timedelta
import re

CONTACTS_FILE = "contacts.json"
NOTES_FILE = "notes.json"

def load_data(file):
    if os.path.exists(file):
        with open(file, 'r') as f:
            return json.load(f)
    return []

def save_data(file, data):
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)

def validate_phone(phone):
    return re.fullmatch(r'\d{10,11}', phone) is not None

def validate_email(email):
    return re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email) is not None

def add_contact(name, address, phone, email, birthday):
    contacts = load_data(CONTACTS_FILE)
    if not validate_phone(phone):
        print("Număr de telefon invalid!")
        return
    if not validate_email(email):
        print("Email invalid!")
        return
    contact = {
        "name": name,
        "address": address,
        "phone": phone,
        "email": email,
        "birthday": birthday
    }
    contacts.append(contact)
    save_data(CONTACTS_FILE, contacts)
    print("Contact adăugat cu succes!")

def display_contacts():
    contacts = load_data(CONTACTS_FILE)
    for contact in contacts:
        print(contact)

def search_contacts(query):
    contacts = load_data(CONTACTS_FILE)
    results = [contact for contact in contacts if query.lower() in contact['name'].lower()]
    for result in results:
        print(result)

def edit_contact(name, new_data):
    contacts = load_data(CONTACTS_FILE)
    for contact in contacts:
        if contact['name'] == name:
            contact.update(new_data)
            save_data(CONTACTS_FILE, contacts)
            print("Contact editat cu succes!")
            return
    print("Contactul nu a fost găsit!")

def delete_contact(name):
    contacts = load_data(CONTACTS_FILE)
    contacts = [contact for contact in contacts if contact['name'] != name]
    save_data(CONTACTS_FILE, contacts)
    print("Contact șters cu succes!")

def contacts_with_upcoming_birthdays(days):
    contacts = load_data(CONTACTS_FILE)
    upcoming_birthdays = []
    today = datetime.now()
    for contact in contacts:
        birthday = datetime.strptime(contact['birthday'], "%Y-%m-%d")
        birthday_this_year = birthday.replace(year=today.year)
        if 0 <= (birthday_this_year - today).days <= days:
            upcoming_birthdays.append(contact)
    for contact in upcoming_birthdays:
        print(contact)

def add_note(text):
    notes = load_data(NOTES_FILE)
    note = {"text": text}
    notes.append(note)
    save_data(NOTES_FILE, notes)
    print("Notiță adăugată cu succes!")

def display_notes():
    notes = load_data(NOTES_FILE)
    for note in notes:
        print(note)

def search_notes(query):
    notes = load_data(NOTES_FILE)
    results = [note for note in notes if query.lower() in note['text'].lower()]
    for result in results:
        print(result)

def edit_note(old_text, new_text):
    notes = load_data(NOTES_FILE)
    for note in notes:
        if note['text'] == old_text:
            note['text'] = new_text
            save_data(NOTES_FILE, notes)
            print("Notiță editată cu succes!")
            return
    print("Notița nu a fost găsită!")

def delete_note(text):
    notes = load_data(NOTES_FILE)
    notes = [note for note in notes if note['text'] != text]
    save_data(NOTES_FILE, notes)
    print("Notiță ștearsă cu succes!")

# Exemple de utilizare
if __name__ == "__main__":
    while True:
        print("\nMeniu:")
        print("1. Adaugă contact")
        print("2. Afișează contacte")
        print("3. Caută contact")
        print("4. Editează contact")
        print("5. Șterge contact")
        print("6. Afișează contacte cu zile de naștere apropiate")
        print("7. Adaugă notiță")
        print("8. Afișează notițe")
        print("9. Caută notiță")
        print("10. Editează notiță")
        print("11. Șterge notiță")
        print("12. Ieșire")

        choice = input("Alege o opțiune: ")

        if choice == "1":
            name = input("Nume: ")
            address = input("Adresă: ")
            phone = input("Telefon: ")
            email = input("Email: ")
            birthday = input("Zi de naștere (YYYY-MM-DD): ")
            add_contact(name, address, phone, email, birthday)
        elif choice == "2":
            display_contacts()
        elif choice == "3":
            query = input("Introdu numele contactului: ")
            search_contacts(query)
        elif choice == "4":
            name = input("Introdu numele contactului de editat: ")
            new_data = {}
            new_name = input("Nume nou (lasă gol pentru a păstra neschimbat): ")
            if new_name:
                new_data['name'] = new_name
            new_address = input("Adresă nouă (lasă gol pentru a păstra neschimbat): ")
            if new_address:
                new_data['address'] = new_address
            new_phone = input("Telefon nou (lasă gol pentru a păstra neschimbat): ")
            if new_phone:
                if validate_phone(new_phone):
                    new_data['phone'] = new_phone
                else:
                    print("Număr de telefon invalid!")
            new_email = input("Email nou (lasă gol pentru a păstra neschimbat): ")
            if new_email:
                if validate_email(new_email):
                    new_data['email'] = new_email
                else:
                    print("Email invalid!")
            new_birthday = input("Zi de naștere nouă (YYYY-MM-DD) (lasă gol pentru a păstra neschimbat): ")
            if new_birthday:
                new_data['birthday'] = new_birthday
            edit_contact(name, new_data)
        elif choice == "5":
            name = input("Introdu numele contactului de șters: ")
            delete_contact(name)
        elif choice == "6":
            days = int(input("Introdu numărul de zile: "))
            contacts_with_upcoming_birthdays(days)
        elif choice == "7":
            text = input("Introdu textul notiței: ")
            add_note(text)
        elif choice == "8":
            display_notes()
        elif choice == "9":
            query = input("Introdu textul de căutat în notițe: ")
            search_notes(query)
        elif choice == "10":
            old_text = input("Introdu textul vechii notițe: ")
            new_text = input("Introdu textul noii notițe: ")
            edit_note(old_text, new_text)
        elif choice == "11":
            text = input("Introdu textul notiței de șters: ")
            delete_note(text)
        elif choice == "12":
            break
        else:
            print("Opțiune invalidă! Te rog să încerci din nou.")1
            
