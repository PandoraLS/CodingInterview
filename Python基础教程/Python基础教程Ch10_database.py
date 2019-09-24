# -*- coding: utf-8 -*-
# @Time: 2019/9/24 23:06
# @Author: Li Sen

import sys, shelve


def store_person(db):
    pid = input('enter unique ID number: ')
    person = {}
    person['name'] = input('Enter name: ')
    person['age'] = input('Enter age: ')
    person['phone'] = input('Enter phone number: ')

    db[pid] = person


def lookup_person(db):
    pid = input('Enter ID number: ')
    field = input('What would you like to know? (name, age, phone): ')
    field = field.strip().lower()
    print(field.capitalize() + ':', db[pid][field])


def print_help():
    print('The available commands are: ')
    print('store  : Stores information about a person')
    print('lookup : Looks up a person from ID number')
    print('quit   : Save changes and exit')
    print('?      : Prints this message')


def enter_command():
    cmd = input('Enter commmand (? for help): ')
    cmd = cmd.strip().lower()
    return cmd


def main():
    database = shelve.open("C:\\Education\\code\\CodingInterview\\Python基础教程\\database.dat")
    try:
        while True:
            cmd = enter_command()
            if cmd == 'store':
                store_person(database)
            elif cmd == 'lookup':
                lookup_person(database)
            elif cmd == '?':
                print_help()
            elif cmd == 'quit':
                return
    finally:
        database.close()


if __name__ == '__main__':
    main()
