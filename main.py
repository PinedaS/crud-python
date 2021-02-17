from os import system
from db import *


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

    return [name, surname, phone, email]


def create():
    data = getData()
    print(data[0])
    sql = "INSERT INTO contact VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (data[0], data[1], data[2], data[3]))
    connection.commit()


def read():
    sql = "SELECT * FROM contact"
    cursor.execute(sql)

    data = cursor.fetchall()
    print(data)


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
