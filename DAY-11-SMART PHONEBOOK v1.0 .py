# IGL AUSBILDUNG 2028 - DAY 11
# PROJECT: IGL SMART PHONEBOOK v1.0
# GOAL: Dictionary {key:value} + methods master karna

# ===== GLOBAL DATA - DICTIONARY =====
# Structure: {name: [phone, city, sap_skill]}
igl_contacts = {
    "nikhil": ["9876543210", "Jaipur", "Python"],
    "rohit": ["8765432109", "Leipzig", "SAP ABAP"],
    "ansh": ["7654321098", "Delhi", "JavaScript"]
}

def show_menu():
    """Menu dikhao"""
    print("\n----- IGL PHONEBOOK MENU -----")
    print("1. Search Contact")
    print("2. Add New Contact")
    print("3. Delete Contact")
    print("4. Show All Contacts")
    print("5. Update SAP Skill")
    print("6. Exit")
    print("------------------------------")

def search_contact(name):
    """Naam se contact dhoondo"""
    name = name.lower()
    if name in igl_contacts:
        details = igl_contacts[name]
        return f"Found: {name.title()}\nPhone: {details[0]}\nCity: {details[1]}\nSAP Skill: {details[2]}"
    else:
        return f"{name.title()} phonebook mein nahi hai 😅"

def add_contact(name, phone, city, skill):
    """Naya contact jodo"""
    name = name.lower()
    igl_contacts[name] = [phone, city, skill]
    return f"{name.title()} add ho gaya ✅"

def delete_contact(name):
    """Contact delete karo"""
    name = name.lower()
    if name in igl_contacts:
        del igl_contacts[name] # dict se hatao
        return f"{name.title()} delete ho gaya 🗑️"
    else:
        return "Contact mila hi nahi bhai"

def show_all():
    """Saare contact dikhao"""
    if not igl_contacts:
        return "Phonebook khali hai 📭"

    result = "----- ALL IGL CONTACTS -----\n"
    for name, details in igl_contacts.items(): #.items() important
        result += f"{name.title()}: {details[0]} | {details[1]} | {details[2]}\n"
    return result

# ===== MAIN PROGRAM - WHILE LOOP =====
def main():
    print("----- IGL SMART PHONEBOOK v1.0 DICT WALA -----")

    while True: # Day 10 ka while use
        show_menu()
        choice = input("IGL Choice daal 1-6: ")

        if choice == "1": # Search
            name = input("Naam likh: ")
            print(search_contact(name))

        elif choice == "2": # Add
            name = input("Naam: ")
            phone = input("Phone: ")
            city = input("City: ")
            skill = input("SAP Skill: ")
            print(add_contact(name, phone, city, skill))

        elif choice == "3": # Delete
            name = input("Kisko delete karna: ")
            print(delete_contact(name))

        elif choice == "4": # Show All
            print(show_all())

        elif choice == "5": # Update Skill
            name = input("Kiska skill update: ").lower()
            if name in igl_contacts:
                new_skill = input("Naya SAP Skill: ")
                igl_contacts[name][2] = new_skill # list ka 3rd item
                print(f"{name.title()} ka skill update ✅")
            else:
                print("Contact nahi mila")

        elif choice == "6": # Exit
            print("Phonebook band. Leipzig 2028 mein milte 🇩🇪")
            break # Day 10 ka break

        else:
            print("Galat choice bhai. 1-6 mein se daal 😅")
            continue # Day 10 ka continue

# ===== PROGRAM START =====
main()