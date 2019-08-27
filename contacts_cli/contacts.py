import os
import csv


class Contact:

    def __init__(self, name, phone, email):
        self._name = name
        self._phone = phone
        self._email = email


class ContactBook:

    def __init__(self):
        self._contacts = []

    def _print_contact(self, contact):
        print('\n--- * --- * --- * --- * --- * --- * --- * ---')
        print(f'Nombre: {contact._name}')
        print(f'Teléfono: {contact._phone}')
        print(f'Email: {contact._email}')
        print('--- * --- * --- * --- * --- * --- * --- * ---')

    def _not_found(self):
        os.system('cls')
        print('\n**********************')
        print('Contacto no encontrado')
        print('**********************')

    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact)
        self._save()

    def show_all(self):
        os.system('cls')
        if len(self._contacts) != 0:
            for contact in self._contacts:
                self._print_contact(contact)
        else:
            print('\nNo hay contactos!')

    def delete(self, name):
        for idx, contact in enumerate(self._contacts):
            if name.lower() == contact._name.lower():
                del self._contacts[idx]
                print('\nContacto borrado exitosamente!')
                break
        else:
            self._not_found()
        self._save()

    def search(self, name):
        for contact in self._contacts:
            if contact._name.lower() == name.lower():
                self._print_contact(contact)
                break
        else:
            self._not_found()

    def _update_menu(self, contact):
        os.system('cls')
        self._print_contact(contact)
        option = input('''

            ¿Qué deseas actualizar?

            [n]ombre
            [t]eléfono
            [e]mail
            [s]alir

            Escribe una opción: ''')
        return option

    def update(self, name):
        for idx, contact in enumerate(self._contacts):
            if name.lower() == contact._name.lower():
                option = self._update_menu(contact)
                while option != 's':
                    if option == 'n':
                        new_name = input('\nEscribe el nuevo nombre: ')
                        contact._name = new_name
                    elif option == 't':
                        new_phone = input('\nEscribe el nuevo teléfono: ')
                        contact._phone = new_phone
                    elif option == 'e':
                        new_email = input('\nEscribe el nuevo email: ')
                        contact._email = new_email
                    else:
                        print('\nOpción inválida! ')
                    input('\nPresione enter para volver al menú...')
                    option = self._update_menu(contact)
                break
        else:
            self._not_found()
            return
        self._save()

    def _save(self):
        with open('contacts.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(('name', 'phone', 'email'))
            for contact in self._contacts:
                writer.writerow(
                    (contact._name, contact._phone, contact._email))


def show_options():
    os.system('cls')  # Si estas en UNIX, cambiar por 'clear'
    choice = input('''
    AGENDA DE CONTACTOS

    [a]ñadir contacto
    [ac]tualizar contacto
    [b]uscar contacto
    [e]liminar contacto
    [l]istar contactos
    [s]alir

    ¿Qué deseas hacer?: ''')
    return choice


def run():
    choice = show_options()
    contact_book = ContactBook()

    try:
        with open('contacts.csv', 'r') as f:
            reader = csv.reader(f)
            for idx, row in enumerate(reader):
                if idx == 0 or row == []:
                    continue
                contact_book.add(row[0], row[1], row[2])
    except FileNotFoundError:
        pass

    while choice != 's':
        if choice == 'a':
            name = input('\nEscribe el nombre del contacto: ')
            phone = input('Escribe el teléfono del contacto: ')
            email = input('Escribe el email del contacto: ')
            contact_book.add(name, phone, email)
        elif choice == 'ac':
            name = input('\nEscribe el nombre del contacto: ')
            contact_book.update(name)
        elif choice == 'b':
            name = input('\nEscribe el nombre del contacto: ')
            contact_book.search(name)
        elif choice == 'e':
            name = input('\nEscribe el nombre del contacto: ')
            contact_book.delete(name)
        elif choice == 'l':
            os.system('cls')
            contact_book.show_all()
        else:
            print('\nOpción no válida')
        input('\nPresione enter para volver al menú...')
        choice = show_options()


if __name__ == '__main__':
    run()
