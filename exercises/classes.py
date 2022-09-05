"""Class exercises"""


class BankAccount:

    def __init__(self):
        self.balance = 0

    def __init__(self, balance=0):
        self.balance = balance

    """Bank account including an account balance."""

    def balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance = self.balance + int(amount)

    def withdraw(self, amount):
        self.balance = self.balance - int(amount)

    def transfer(self, account, amount):
        self.balance = self.balance - int(amount)
        account.balance = account.balance + int(amount)

    def __repr__(self):
        return f"BankAccount(balance={self.balance})"


class SuperMap:
    """Data structure for quickly finding objects based on their attributes."""


class MinHeap:
    """Heap-like data structure."""


class Flavor:
    """Flavor of ice cream."""


class Size:
    """Ice cream size."""


class IceCream:
    """Ice cream to be ordered in our ice cream shop."""


class Month:
    """Class representing an entire month."""


class MonthDelta:
    """Class representing the difference between months."""


class Row:
    """Row class that stores all given arguments as attributes."""
