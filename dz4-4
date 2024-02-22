def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def show_all(contacts: dict):
    # return contacts
    if not contacts:
        return "no contacts"
    res = ""
    for key, value in contacts.items():
        res += f"name: {key} phone: {value}\n"
    return res

def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "contact update"
    return "contact not updatet"

def show_phone(args, contacts):
    name = args[0]
    phone = contacts.get(name)
    if phone:
        return phone
    return "no contact in base"

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print (show_phone(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
