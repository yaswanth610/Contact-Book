contact = {}

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")

    contact[name] = phone
    print("---- Contact Added Successfully ----")


def search_contact():
    name = input("Enter Name: ")

    if name in contact:
        print("Phone Number:", contact[name])
    else:
        print("** Contact Not Found **")


def delete_contact():
    name = input("Enter Name: ")

    if name in contact:
        del contact[name]
        print("--- Contact Deleted Successfully ---")
    else:
        print("** Contact Not Found **")


def display_contact():
    if not contact:
        print("// No Contacts Available //")
    else:
        print("\n--- CONTACTS ---")
        for name, phone in contact.items():
            print(f"{name} : {phone}")


while True:
    print("\n*** CONTACT BOOK ***")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Display Contacts")
    print("5. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        search_contact()

    elif choice == "3":
        delete_contact()

    elif choice == "4":
        display_contact()

    elif choice == "5":
        print("*** THANK YOU ***")
        break

    else:
        print("Invalid Input")