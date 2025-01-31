print("Simple Contact Book!")
contacts={}

def inp():
    choice = input("Enter Choice: ")
    if(choice.isdigit()):
        choice=int(choice)
        if(1<=choice<=6):
            return choice
        else:
            print("Invalid Input, Number must be from 1 to 6.\n")
            return inp()
    else:
        print("Invalid Input, Please choose a number.\n")
        return inp()

def add():
    contact = checkName()
    number = checkNum(contact)

def view():
    if(empty()):
        print("\nContacts:")
        for i in contacts:
            print(f"Contact Name: {i}, Contact Number: {contacts[i]}")
        print()

def update():
    if(empty()):
        contact =  input("\nEnter the Contacts Name to be updated: ").strip().lower()
        if(check(contact)):
            number = updateNum(contact)
            contacts[contact]=number

def delete():
    if(empty()):
        contact =  input("\nEnter Contact Name to be deleted: ").strip().lower()
        if(check(contact)):
            del contacts[contact]
            print("Contact Deleted successfully!\n")

def search():
    if(empty()):
        contact=input("Enter Contact Name: ")
        if(check(contact)):
            print(f"Contact Found!\nContact's Number is {contacts[contact]}\n")

def leave():
    print("Thank You!")
    exit()

def checkName():
    contact =  input("\nEnter Contact Name: ").strip().lower()
    if not contact:
        print("Cant enter an empty name.")
        return checkName()
    return contact

def checkNum(contact):
    number = input("Enter Contact Number: ")
    if(number.isdigit()):
        contacts[contact] = number
        print("Contact added successfully!\n")
        return number
    else:
        print("Not a Valid Phone number.\n")
        return checkNum(contact)

def updateNum(contact):
    number = input("Enter Updated Contact Number: ")
    if(number.isdigit()):
        contacts[contact] = number
        print("Contact updated successfully!\n")
        return number
    else:
        print("Not a Valid Phone number.\n")
        return updateNum(contact)

def empty():
    if not contacts:
        print("There are no Contacts in the Phonebook.\n")
        return False
    else:
        return True

def check(contact):
    if contact not in contacts:
        print("Contact not found!")
        view()
        return False
    else:
        return True

while True:
    print("1. Add a New Contact")
    print("2. View all Contacts")
    print("3. Update a Contact's Information")
    print("4. Delete a Contact")
    print("5. Search a Contact by Name")
    print("6. Exit\n")
    choice = inp()
    if choice == 1:
        add()
    elif choice == 2:
        view()
    elif choice == 3:
        update()
    elif choice == 4:
        delete()
    elif choice == 5:
        search()
    else:
        leave()