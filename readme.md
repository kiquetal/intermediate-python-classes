### Class: Intermediate python classes
### Date: 05-09-2022


- If method within class, it's equivalent to  `self` parameter.
- The first argument has to be self .



- Exercises

    Bank Account

    This is the BankAccount exercise in classes.py. To test it, run python test.py BankAccount from the exercises directory.

    Make a BankAccount class that allows depositing and withdrawing money:

      from classes import BankAccount
      trey_account = BankAccount(20)
      trey_account.balance
      20
      trey_account.deposit(100)
      trey_account.balance
      120
      trey_account.withdraw(40)
      trey_account.balance
      80
      trey_account
      BankAccount(balance=80)

Your BankAccount class should also support transfers:

    mary_account = BankAccount(100)
    dana_account = BankAccount()
    mary_account.transfer(dana_account, 20)
    mary_account.balance
    80
    dana_account.balance
    20
