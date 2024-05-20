from contacts import add_contact, display_contacts, search_contacts, edit_contact, delete_contact, contacts_with_upcoming_birthdays
from notes import add_note, display_notes, search_notes, edit_note, delete_note

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
            print("Opțiune invalidă! Te rog să încerci din nou.")
