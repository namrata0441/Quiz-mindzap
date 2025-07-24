# !/usr/bin/python
# -*- coding: utf-8 -*-


class User:
    def __init__(self):
        self.userName = None
        self.password = None
        self.firstName = None
        self.idNumber = None


class Teacher(User):
    pass


class Student(User):
    pass


class Admin(User):
    pass


class Developer(User):
    pass
