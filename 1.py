
class user:
    def __init__(self,username,password,email):
        self.__username = username
        self.__password = password
        self.__email = email
        self.__budgets = []
        self.__expenses = []
    
    
    def get_username(self):
        return self.__username

    def set_username(self, username):
        self.__username = username

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email
        
    def addBudget(self,category,amount):
        if amount > 0:
            budget = Budget(category,amount)
            self.__budgets.append(budget)
            print("Budget ajoute avec succes ")
        else:
            print("Veuillez inserer un montant de budget supérieur a zero")
    
    def addTransaction(self, date, description, amount, category):
        if amount > 0:
            transaction = Transaction(date, description, amount, category)
            self.__transactions.append(transaction)
            print("Transaction ajoutée.")
        else:
            print("Le montant de la transaction doit être supérieur à zéro.")
            
    def getBudgetByCategory(self, category):
        for budget in self.__budgets:
            if budget.category == category:
                return budget
        return None
    
    def addTransaction(self, date, description, amount, category):
        if amount <= 0:
            print("Le montant de la transaction doit être supérieur à zéro.")
            return

        total_budget = sum(budget.amount for budget in self.__budgets if budget.category == category)
        total_expenses = sum(transaction.amount for transaction in self.__transactions if transaction.category == category)

        balance = total_budget - total_expenses
        if amount > balance:
            print("Le montant de la transaction dépasse le solde disponible.")
            return

        transaction = Transaction(date, description, amount, category)
        self.__transactions.append(transaction)
        print("Transaction ajoutée.")

    def getBudgets(self):
        return self.__budgets

    def getTransactions(self):
        return self.__transactions

class Transaction:
    def __init__(self, date, description, amount, category):
        self.__date = date
        self.__description = description
        self.__amount = amount
        self.__category = category
        
    def get_date(self):
        return self.__date

    def set_date(self, date):
        self.__date = date

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        self.__amount = amount

    def get_category(self):
        return self.__category

    def set_category(self, category):
        self.__category = category

    def __str__(self):
        return f"{self.date} - {self.description}: {self.amount} ({self.category})"

    def __repr__(self):
        return f"Transaction({self.date}, {self.description}, {self.amount}, {self.category})"


class Budget:
    def __init__(self, category, amount):
        self.__category = category
        self.__amount = amount
    
    def get_category(self):
        return self.__category

    def set_category(self, category):
        self.__category = category

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        self.__amount = amount


class Expense:
    def __init__(self, date, description, amount, category):
        self.__date = date
        self.__description = description
        self.__amount = amount
        self.__category = category
    
    def get_date(self):
        return self.__date

    def set_date(self, date):
        self.__date = date

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        self.__amount = amount

    def get_category(self):
        return self.__category

    def set_category(self, category):
        self.__category = category

import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                               id INTEGER PRIMARY KEY AUTOINCREMENT,
                               username TEXT NOT NULL,
                               email TEXT NOT NULL,
                               password TEXT NOT NULL)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
                               id INTEGER PRIMARY KEY AUTOINCREMENT,
                               user_id INTEGER,
                               date TEXT NOT NULL,
                               description TEXT NOT NULL,
                               amount REAL NOT NULL,
                               category TEXT NOT NULL,
                               FOREIGN KEY (user_id) REFERENCES users(id))''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS budgets (
                               id INTEGER PRIMARY KEY AUTOINCREMENT,
                               user_id INTEGER,
                               category TEXT NOT NULL,
                               amount REAL NOT NULL,
                               FOREIGN KEY (user_id) REFERENCES users(id))''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS expenses (
                               id INTEGER PRIMARY KEY AUTOINCREMENT,
                               user_id INTEGER,
                               date TEXT NOT NULL,
                               description TEXT NOT NULL,
                               amount REAL NOT NULL,
                               category TEXT NOT NULL,
                               FOREIGN KEY (user_id) REFERENCES users(id))''')

        self.conn.commit()

    def add_user(self, username, email, password):
        self.cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password))
        self.conn.commit()

    def add_transaction(self, user_id, date, description, amount, category):
        self.cursor.execute("INSERT INTO transactions (user_id, date, description, amount, category) VALUES (?, ?, ?, ?, ?)",
                            (user_id, date, description, amount, category))
        self.conn.commit()

    def add_budget(self, user_id, category, amount):
        self.cursor.execute("INSERT INTO budgets (user_id, category, amount) VALUES (?, ?, ?)",
                            (user_id, category, amount))
        self.conn.commit()

    def get_user_id(self, username):
        self.cursor.execute("SELECT id FROM users WHERE username=?", (username,))
        user_id = self.cursor.fetchone()
        if user_id:
            return user_id[0]
        else:
            return None

    def get_user_budgets(self, user_id):
        self.cursor.execute("SELECT category, amount FROM budgets WHERE user_id=?", (user_id,))
        return self.cursor.fetchall()

    def get_user_transactions(self, user_id):
        self.cursor.execute("SELECT date, description, amount, category FROM transactions WHERE user_id=?", (user_id,))
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()

    
    
    
     
    
    
