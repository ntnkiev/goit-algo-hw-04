def parse_input(user_input): #розбір команди та аргументів
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts): #додавання контакту до словника
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts): #зміна контакту якщо знайдений
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact changed."
    else:
        return "Contact not found." #якщо не знайдений - помилка

def phone_num(args, contacts): #друк номеру телефону за ім'ям якщо знайдено
    name = args[0]
    if name in contacts:
        return f"{name.capitalize()} phone number is {contacts[name]}."
    else:
        return "Contact not found." #якщо не знайдений - помилка
    
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        match command:
            case "close" | "exit":
                print("Good bye!")
                break
            case "hello":
                print("How can I help you?")
            case "add":
                if len(args) == 2:
                    print(add_contact(args, contacts))
                else:
                    print("Error")
            case "change":
                if len(args) == 2:
                    print(change_contact(args, contacts))           
                else:
                    print("Error")
            case "phone":
                if len(args) == 1:
                    print(phone_num(args, contacts))
                else:
                    print("Error")
            case "all":
                for key, value in contacts.items():
                    print(f"{key.capitalize():<10}{value}")
            case _:
                print("Invalid command.")

if __name__ == "__main__":
    main()

