#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib
import random

ALPHABET = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def gen_salt(length=8):

    return ''.join(random.choice(ALPHABET) for i in range(length))

username = input('Enter username: ')
password = input('Enter password: ')

salt = gen_salt()

hashed_password = hashlib.md5('{0}{1}'.format(password, salt).encode()).hexdigest()

with open('passwords.txt', 'a') as f:
    f.write('{0} {1}${2}\n'.format(username, salt, hashed_password))
