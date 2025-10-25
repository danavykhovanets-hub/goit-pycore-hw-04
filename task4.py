def parse_input(user_input):
    # Обробка введеного користувачем рядка
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


# Словник для зберігання контактів
contacts = {}

#Команди бота
def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command format. Use: add [name] [phone]" #обробка помилки

    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command format. Use: change [name] [new phone]"

    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."


def show_phone(args, contacts):
    if len(args) != 1:
        return "Invalid command format. Use: phone [name]" #обробка помилки

    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."


def show_all(contacts):
    if not contacts:
        return "No contacts saved."
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result)


def main():
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.") #обробка помилки


if __name__ == "__main__":
    main()
