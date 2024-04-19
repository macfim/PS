from tkinter import *
from tkinter import messagebox

from classes.UserDB import UserDB
from classes.TransactionDB import TransactionDB

class App:
    def __init__(self, root, mydb):
        self.root = root
        self.root.title("Main")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        self.user_id = None

        self.userdb = UserDB(mydb)
        self.transactiondb = TransactionDB(mydb)

        # Container Frame
        self.container_frame = Frame(self.root)
        self.container_frame.pack()

        # Login Frame
        self.login_frame = Frame(self.container_frame)
        self.login_frame.pack()

        # Main Frame
        self.main_frame = Frame(self.container_frame)
        self.main_frame.pack()

        self.display_login_form()

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        user = self.userdb.find_by_email_and_password(email, password)

        if not user:
            messagebox.showerror("Error", "Invalid email or password")
            return

        self.user_id = user[0]

        self.login_frame.pack_forget()
        self.display_transactions()

    def display_login_form(self):
        self.email_label = Label(self.login_frame, text="Email")
        self.email_label.grid(row=0, column=0)

        self.email_entry = Entry(self.login_frame)
        self.email_entry.grid(row=0, column=1)

        self.password_label = Label(self.login_frame, text="Password")
        self.password_label.grid(row=1, column=0)

        self.password_entry = Entry(self.login_frame, show="*")
        self.password_entry.grid(row=1, column=1)

        self.login_button = Button(self.login_frame, text="Login", command=self.login)
        self.login_button.grid(row=2, column=0, columnspan=2)

    def display_transactions(self):
        transactions = self.transactiondb.find_all_by_user_id(self.user_id)

        self.total = 0
        for transaction in transactions:
            if transaction[2] == "Income":
                self.total += int(transaction[3])
            else:
                self.total -= int(transaction[3])

        self.total_label = Label(self.main_frame, text="Total: " + str(self.total))
        self.total_label.grid(row=0, column=0, columnspan=5)

        self.id_label = Label(self.main_frame, text="ID")
        self.id_label.grid(row=1, column=0)

        self.type_label = Label(self.main_frame, text="Type")
        self.type_label.grid(row=1, column=1)

        self.amount_label = Label(self.main_frame, text="Amount")
        self.amount_label.grid(row=1, column=2)

        self.date_label = Label(self.main_frame, text="Date")
        self.date_label.grid(row=1, column=3)

        self.description_label = Label(self.main_frame, text="Description")
        self.description_label.grid(row=1, column=4)

        for i in range(len(transactions)):
            self.id = Label(self.main_frame, text=transactions[i][0])
            self.id.grid(row=i+2, column=0)

            self.type = Label(self.main_frame, text=transactions[i][2])
            self.type.grid(row=i+2, column=1)

            self.amount = Label(self.main_frame, text=transactions[i][3])
            self.amount.grid(row=i+2, column=2)

            self.date = Label(self.main_frame, text=transactions[i][4])
            self.date.grid(row=i+2, column=3)

            self.description = Label(self.main_frame, text=transactions[i][5])
            self.description.grid(row=i+2, column=4)