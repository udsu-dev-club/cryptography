#!/usr/bin/env python3
# -*- coding: utf-8 -*-

username = input('Enter username: ')
password = input('Enter password: ')

with open('passwords.txt') as f:
    for line in f.readlines():
        if line == '{0} {1}\n'.format(username, password):
            print('ok')
            break

    else:
        print('error')
