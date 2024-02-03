def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact changed."
    else:
        return "Contact not found."

def phone_num(args, contacts):
    name = args[0]
    if name in contacts:
        return f"{name.capitalize()} phone number is {contacts[name]}."
    else:
        return "Contact not found."
    
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
            if len(args) == 2:
                print(add_contact(args, contacts))
            else:
                print("Error")
        elif command == "change":
            if len(args) == 2:
                print(change_contact(args, contacts))           
            else:
                print("Error")
        elif command == "phone":
            if len(args) == 1:
                print(phone_num(args, contacts))
            else:
                print("Error")
        elif command == "all":
            for key, value in contacts.items():
                print(f"{key.capitalize():<10}{value}")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

