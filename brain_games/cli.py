#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""User`s greeting function."""


import prompt


def welcome_user():
    """Ask user`s name and greet him."""
    user_name = prompt.string(prompt='May I have your name? ')
    print('Hello, {0}!'.format(user_name))
