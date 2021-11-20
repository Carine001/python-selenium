import os


class Phonebook:
    def __init__(self):
        self.numbers = {}
        self.filename = "scripts/phonebook.txt"
        self.cache = open(self.filename, "w", encoding="utf-8")

    def add(self, name, number):
        self.numbers[name] = number

    def lookup(self, name):
        return self.numbers[name]

    def names(self):
        return set(self.numbers.keys())

    def clear(self):
        self.cache.close()
        os.remove(self.filename)
