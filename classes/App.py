from tkinter import *

from classes.UserDB import UserDB
from classes.TransactionDB import TransactionDB

class App:
    def __init__(self, root, mydb):
        self.root = root
        self.root.title("Main")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        self.userdb = UserDB(mydb)
        self.transactiondb = TransactionDB(mydb)

        self.container = Frame(self.root)
        self.container.pack()

        self.display_transactions()

    def display_transactions(self):
        transactions = self.transactiondb.find_all()
        
        for i in range(len(transactions)):
            self.e = Label(self.container, text=transactions[i][0])
            self.e.grid(row=i, column=0)

            self.type = Label(self.container, text=transactions[i][1])
            self.type.grid(row=i, column=1)

            self.amount = Label(self.container, text=transactions[i][2])
            self.amount.grid(row=i, column=2)

            self.date = Label(self.container, text=transactions[i][3])
            self.date.grid(row=i, column=3)

            self.description = Label(self.container, text=transactions[i][4])
            self.description.grid(row=i, column=4)

            self.user_id = Label(self.container, text=transactions[i][5])
            self.user_id.grid(row=i, column=5)