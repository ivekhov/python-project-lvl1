#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import prompt


def welcome_user():
    user_name = prompt.string(prompt='May I have your name? ')
    print('Hello, {}!'.format(user_name))

