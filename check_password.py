#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib

username = input('Enter username: ').encode('utf-8')
password = input('Enter password: ').encode('utf-8')

hashed_password = hashlib.md5(password).hexdigest()

with open('passwords.txt') as f:
    for line in f.readlines():
        if line == '{0} {1}\n'.format(username, hashed_password):
            print('ok')
            break

    else:
        print('error')
