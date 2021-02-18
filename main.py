from os import system
from db import *
from Contact import *


def print_menu():
    print('*' * 10, 'AGENDA', '*' * 10)
    print('[C]Crear contacto')
    print('[R]Listar contactos')
    print('[U]Actualizar contacto')
    print('[D]Eliminar contacto')
    print('[S]Buscar contacto')


def getData():
    print('Ingresa los siguientes datos:')
    name = input('Nombre: ')
    surname = input('Apellido: ')
    phone = input('Teléfono: ')
    email = input('Email: ')

    contact = Contact(name, surname, phone, email)

    return contact


def create():
    data = getData()
    sql = "INSERT INTO contact VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (data.getName, data.getSurname,
                         data.getPhone, data.getEmail))
    connection.commit()


def read():
    sql = "SELECT * FROM contact"
    cursor.execute(sql)

    data = cursor.fetchall()

    for i in data:
        k = 0
        while k < 4:
            if (k == 0):
                print('Nombre: ', i[k])
            if (k == 1):
                print('Apellido: ', i[k])
            if (k == 2):
                print('Teléfono: ', i[k])
            if (k == 3):
                print('Email: ', i[k])

            k += 1

        print('-' * 40)


def update():
    pass


def delete():
    pass


def search():
    pass


def run():
    print_menu()
    command = input()
    command = command.upper()
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
