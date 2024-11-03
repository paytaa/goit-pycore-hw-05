# декоратор для обработки ошибок 
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as ve:
            return str(ve)  
        except IndexError:
            return "Please provide the necessary arguments for the command."  
        except KeyError as ke:
            return str(ke)  
    return inner

def parse_input(user_input):
    if not user_input.strip():
        raise ValueError("Input cannot be empty. Please enter a command.")
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()  # !!!!!!!!!! НИЖНІЙ РЕГІСТР
    return cmd, args

# функція для додавання нового контакту
@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError("Please provide both name and phone number.")
    
    name, phone = args
    contacts[name] = phone  # додаємо контакт у словник
    return "Contact added."  # повідомляємо про успіх

# функція для зміни телефону існуючого контакту
@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise ValueError("Please provide both name and new phone number.")
    
    name, phone = args
    if name in contacts:
        contacts[name] = phone  # оновлюємо номер телефону
        return "Contact updated."  # успіх
    else:
        raise KeyError("Contact not found.")  

# функція для показу телефону контакту
@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        raise ValueError("Please provide a name.")
    
    name = args[0]
    if name in contacts:
        return f"{name}: {contacts[name]}"  # виводимо ім'я і номер телефон
    else:
        raise KeyError("Contact not found.")  # помилка якщо контакт не знайдено

# функція для показу всіх контактів
@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts found."  # повідомлення якщо контактів немає
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

# головна функція що керує ботом
def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ").strip()
        if user_input.lower() in ["close", "exit"]:
            print("Good bye!")  # завершення роботи 
            break

        try:
            command, args = parse_input(user_input)

            # обробка
            if command == "hello":
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
                print("Invalid command.") 
        except ValueError as e:
            print(e)

        except KeyError as e:
            print(e)

if __name__ == "__main__":
    main()
