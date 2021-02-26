from os import system
import sys
from db import *
from Contact import *
import re  # Para expresiones regulares
from validate_email import validate_email


def print_menu():
    print('*' * 30, 'AGENDA', '*' * 30)
    print('[C]Crear contacto')
    print('[R]Listar contactos')
    print('[U]Actualizar contacto')
    print('[D]Eliminar contacto')
    print('[S]Buscar contacto')
    print('[E]Salir')


def validate_phone(phone):
    # Validar si existe o no en la base de datos
    sql = "SELECT phones FROM contact"
    cursor.execute(sql)
    data = cursor.fetchall()
    flag = 0  # Cambia a 1 si el teléfono existe

    for i in data:
        if i[0] == int(phone):
            flag = 1

    if flag == 1:
        return True

    if flag == 0:
        return False


def getData():
    print('Ingresa los siguientes datos:')
    name = input('Nombre: ')
    surname = input('Apellido: ')
    phone = input('Teléfono: ')

    if validate_phone(phone) == True:
        print('El teléfono ya existe. Ingrese uno diferente')
        getData()

    if validate_phone(phone) == False:
        email = input('Email: ')

        try:
            is_valid = validate_email(email, verify=True)

            if is_valid is False:
                print('Correo electrónico incorrecto')
                getData()

            else:
                contact = Contact(name, surname, phone, email)

                return contact
        except:
            print('Error. Debe estar conectado a internet para verificar su email.')
            run()


def create():
    data = getData()
    sql = "INSERT INTO contact VALUES (%s, %s, %s, %s)"

    try:
        cursor.execute(sql, (data.getName(), data.getSurname(),
                             data.getPhone(), data.getEmail()))
        connection.commit()

        print('Usuario creado correctamente.')
    except pymysql.err.OperationalError:
        print('Error con la base de datos.')


def read():
    sql = "SELECT * FROM contact"
    cursor.execute(sql)

    data = cursor.fetchall()

    if data == ():
        print('No se han agregado contactos')

    else:
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
    phone = search()

    option = input('Seleccione una opción para actualizar: ')
    option = option.upper()
    value = input('Nuevo valor: ')

    if option == 'A':
        sql = "UPDATE contact SET names=(%s) WHERE phones=(%s)"
        cursor.execute(sql, (value, phone))

    elif option == 'B':
        sql = "UPDATE contact SET surnames=(%s) WHERE phones=(%s)"
        cursor.execute(sql, (value, phone))

    elif option == 'C':
        sql = "UPDATE contact SET phones=(%s) WHERE phones=(%s)"
        cursor.execute(sql, (value, phone))

    elif option == 'D':
        sql = "UPDATE contact SET emails=(%s) WHERE phones=(%s)"
        cursor.execute(sql, (value, phone))

    else:
        print('Opción incorrecta')
        update()

    print('Datos actualizados: ')

    if option == 'A' or option == 'B' or option == 'D':
        sql = "SELECT * FROM contact WHERE phones=(%s)"
        cursor.execute(sql, phone)

    elif option == 'C':
        sql = "SELECT * FROM contact WHERE phones=(%s)"
        cursor.execute(sql, value)

    data = cursor.fetchone()

    print('a. Nombre: ', data[0])
    print('b. Apellido: ', data[1])
    print('c. Teléfono: ', data[2])
    print('d. Email: ', data[3])

    connection.commit()


def delete():
    phone = search()
    option = input('¿Realmente desea eliminar este contacto? (Y/n)')
    option = option.upper()

    if option == 'Y':
        sql = "DELETE FROM contact WHERE phones=(%s)"
        cursor.execute(sql, phone)
        connection.commit()
        print('Contacto eliminado correctamente.')

    elif option == 'N':
        run()

    elif option != 'Y' and option != 'N':
        print('Opción incorrecta')
        run()


def search():
    phone = input('Ingrese el número de télefono: ')
    sql = "SELECT * FROM contact WHERE phones=(%s)"
    cursor.execute(sql, phone)
    data = cursor.fetchone()

    if data is None:
        print('El usuario no existe.')
        run()

    else:
        print('a. Nombre: ', data[0])
        print('b. Apellido: ', data[1])
        print('c. Teléfono: ', data[2])
        print('d. Email: ', data[3])

        return phone


def run():
    create_table()
    print_menu()
    command = input()
    command = command.upper()
    system('clear')

    if command == 'C':
        create()
    elif command == 'R':
        read()
    elif command == 'U':
        update()
    elif command == 'D':
        delete()
    elif command == 'S':
        search()
    elif command == 'E':
        sys.exit()
    else:
        print('Opción ingresada inválida')
        run()

    while command == 'C' or command == 'R' or command == 'U' or command == 'D' or command == 'S':
        run()


if __name__ == "__main__":
    run()
