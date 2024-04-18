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

        self.display_transactions()

    def display_transactions(self):
        transactions = self.transactiondb.find_all()
        
        for i in range(len(transactions)):
            for j in range(len(transactions[i])):
                self.e = Entry(self.root, width=10, fg='blue')
                self.e.grid(row=i, column=j)
                self.e.insert(END, transactions[i][j])