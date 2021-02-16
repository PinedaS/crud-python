from os import system


def print_menu():
    print('*' * 10, 'AGENDA', '*' * 10)
    print('[C]Crear contacto')
    print('[R]Listar contactos')
    print('[U]Actualizar contacto')
    print('[D]Eliminar contacto')
    print('[S]Buscar contacto')


def create():
    pass


def read():
    pass


def update():
    pass


def delete():
    pass


def search():
    pass


def run():
    print_menu()
    command = input()
    command.upper()
    system('clear')

    if command == 'C':
        create()
    if command == 'R':
        read()
    if command == 'U':
        update()
    if command == 'D':
        delete()
    if command == 'S':
        search()


if __name__ == "__main__":
    run()
