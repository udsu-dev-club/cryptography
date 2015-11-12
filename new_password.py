#!/usr/bin/env python3
# -*- coding: utf-8 -*-

username = input('Enter username: ')
password = input('Enter password: ')

with open('passwords.txt', 'a') as f:
    f.write('{0} {1}\n'.format(username, password))
