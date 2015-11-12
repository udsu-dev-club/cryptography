#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib

username = input('Enter username: ')
password = input('Enter password: ')

with open('passwords.txt') as f:
    for line in f.readlines():
        line = line.strip('\n')
        (login, hashed_password_with_salt) = line.split(' ')
        if login == username:
            (salt, hashed_password) = hashed_password_with_salt.split('$')
            entered_hashed_password = hashlib.md5()
            entered_hashed_password.update((password + salt).encode())
            entered_hashed_password = entered_hashed_password.hexdigest()
            if hashed_password == entered_hashed_password:
                print('ok')
                break

            else:
                print('error')
                break

    else:
        print('error')
