# This file is actually used to mock a module for the tests.


class Dinosaur:
    def __init__(self):
        self.name = "trex"

    @staticmethod
    def a(value):
        return value

    @classmethod
    def b(cls, value):
        return value

    def hello(self):
        return self.name


def roar():
    """
    Does a roar!
    """
    return "Roarr!!"


def super_roar():
    """
    Does a super roar!
    """
    return "Super Roarr!!"
