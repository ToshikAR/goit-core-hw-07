'''
Настав час об'єднати наші попередні домашні завдання в одне.
Зараз ми нарешті ми об'єднаємо попередні домашні завдання в один функціональний проєкт
'''
from bookPackage import AddressBook, function


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def get_commands():
    help = [
        "close",
        "exit",
        "all",
        "add [name] [phone]",
        "change [name] [old phone] [new phone]",
        "phone [name]",
        "add-birthday [name] [birth date]",
        "show-birthday [name]",
        "birthdays"
    ]
    text = "Command: \n" 
    for i in help:
        text += i + "\n"
    return text

def main():
    print("Welcome to the assistant bot!")
    book = AddressBook()

    while True:
        user_input = input("Enter a command: ")
        if user_input.strip() == '': 
            print('Enter the command')
            continue
        
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            # реалізація
            print(function.add_contact(args, book))

        elif command == "change":
            # реалізація
            print(function.change_contact(args, book))

        elif command == "phone":
            # реалізація
            print(function.find_contact(args, book))

        elif command == "all":
            # реалізація
            print(book)

        elif command == "add-birthday":
            # реалізація
            print(function.add_birthday(args, book))

        elif command == "show-birthday":
            # реалізація
            print(function.show_birthday(args, book))

        elif command == "birthdays":
            # реалізація
            print(book.get_upcoming_birthdays())

        elif command == "help":
            # реалізація
            print(get_commands())

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()