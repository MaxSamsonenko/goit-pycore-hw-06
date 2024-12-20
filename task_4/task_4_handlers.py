def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Not enough arguments provided."
    return inner


@input_error
def add_contact(args, contacts):
    name, phone = args 
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return f"Phone number for {name} has been changed."


@input_error
def show_phone(args, contacts):
    name = args[0]  # Можлива помилка IndexError
    if name not in contacts:
        raise KeyError  # Викидає помилку, якщо контакт відсутній
    return f"{name}'s phone is {contacts[name]}"
