import mysql.connector

##############################
# Category Table
##############################

def getAllCategories():
    sql = "SELECT * FROM categories"

    mycursor = mydb.cursor()
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    return myresult

def getCategoryById(id):
    sql = "SELECT * FROM categories WHERE id = %s"
    val = (id,)

    mycursor = mydb.cursor()
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()

    return myresult

def createCategory(name):
    sql = "INSERT INTO categories (name) VALUES (%s)"
    val = (name,)

    mycursor = mydb.cursor()
    mycursor.execute(sql, val)
    mydb.commit()

    return mycursor.lastrowid

def updateCategory(id, name):
    sql = "UPDATE categories SET name = %s WHERE id = %s"
    val = (name, id)

    mycursor = mydb.cursor()
    mycursor.execute(sql, val)
    mydb.commit()

    return mycursor.rowcount

def deleteCategory(id):
    sql = "DELETE FROM categories WHERE id = %s"
    val = (id,)

    mycursor = mydb.cursor()
    mycursor.execute(sql, val)
    mydb.commit()

    return mycursor.rowcount

##############################
# Users Table
##############################

def getAllUsers():
    sql = "SELECT * FROM users"

    mycursor = mydb.cursor()
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    return myresult

def getUserById(id):
    sql = "SELECT * FROM users WHERE id = %s"
    val = (id,)

    mycursor = mydb.cursor()
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()

    return myresult

def createUser(email, username, password):
    sql = "INSERT INTO users (email, username, password) VALUES (%s, %s, %s)"
    val = (email, username, password)

    mycursor = mydb.cursor()
    mycursor.execute(sql, val)
    mydb.commit()

    return mycursor.lastrowid

def updateUser(id, email, username, password):
    sql = "UPDATE users SET email = %s, username = %s, password = %s WHERE id = %s"
    val = (email, username, password, id)

    mycursor = mydb.cursor()
    mycursor.execute(sql, val)
    mydb.commit()

    return mycursor.rowcount

def deleteUser(id):
    sql = "DELETE FROM users WHERE id = %s"
    val = (id,)

    mycursor = mydb.cursor()
    mycursor.execute(sql, val)
    mydb.commit()

    return mycursor.rowcount

##############################
# Expense Table
##############################

# id, amount, description(optional), transaction_type(income/expense)
# user_id(foreign key), category_id(foreign key), created_at

def getAllExpenses():
    sql = "SELECT * FROM expenses"

    mycursor = mydb.cursor()
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    return myresult

def getExpenseById(id):
    sql = "SELECT * FROM expenses WHERE id = %s"
    val = (id,)

    mycursor = mydb.cursor()
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()

    return myresult

def createExpense(
    amount,
    transaction_type,
    user_id,
    category_id,
    description=None
):
    sql = "INSERT INTO expenses "
    sql += "(amount, transaction_type, user_id, category_id, description) "
    sql += "VALUES (%s, %s, %s, %s, %s)"
    val = (amount, transaction_type, user_id, category_id, description)

    mycursor = mydb.cursor()
    mycursor.execute(sql, val)
    mydb.commit()

    return mycursor.lastrowid

def updateExpense(
    id,
    amount,
    transaction_type,
    user_id,
    category_id,
    description=None
):
    sql = "UPDATE expenses SET amount = %s, transaction_type = %s,"
    sql += " user_id = %s, category_id = %s, description = %s WHERE id = %s"
    val = (amount, transaction_type, user_id, category_id, description, id)

    mycursor = mydb.cursor()
    mycursor.execute(sql, val)
    mydb.commit()

    return mycursor.rowcount

def deleteExpense(id):
    sql = "DELETE FROM expenses WHERE id = %s"
    val = (id,)

    mycursor = mydb.cursor()
    mycursor.execute(sql, val)
    mydb.commit()

    return mycursor.rowcount

##############################
# Main
##############################

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="joe",
    password="EfFaazcJv_l(3@]M",
    database="main"
)

if not mydb.is_connected():
    print("Failed to connect to MySQL")
    exit()

print("Connected to MySQL")

print("Options:")
print("01. Get all users")
print("02. Get user by id")
print("03. Create user")
print("04. Update user")
print("05. Delete user")
print("06. Get all categories")
print("07. Get category by id")
print("08. Create category")
print("09. Update category")
print("10. Delete category")
print("11. Get all expenses")
print("12. Get expense by id")
print("13. Create expense")
print("14. Update expense")
print("15. Delete expense")
print("99. Exit")

while True:
    choice = input(">")

    if choice == "1":
        users = getAllUsers()

        for user in users:
            print(user)

    elif choice == "2":
        id = input("Enter user id: ")
        user = getUserById(id)

        print(user)

    elif choice == "3":
        email = input("Enter email: ")
        username = input("Enter username: ")
        password = input("Enter password: ")

        id = createUser(email, username, password)

        print("User created with id", id)

    elif choice == "4":
        id = input("Enter user id: ")
        email = input("Enter email: ")
        username = input("Enter username: ")
        password = input("Enter password: ")

        rows = updateUser(id, email, username, password)

        print(rows, "user updated")

    elif choice == "5":
        id = input("Enter user id: ")

        rows = deleteUser(id)

        print(rows, "user deleted")

    elif choice == "6":
        categories = getAllCategories()

        for category in categories:
            print(category)

    elif choice == "7":
        id = input("Enter category id: ")

        category = getCategoryById(id)

        print(category)

    elif choice == "8":
        name = input("Enter category name: ")

        id = createCategory(name)

        print("Category created with id", id)

    elif choice == "9":
        id = input("Enter category id: ")
        name = input("Enter category name: ")

        rows = updateCategory(id, name)

        print(rows, "category updated")

    elif choice == "10":
        id = input("Enter category id: ")

        rows = deleteCategory(id)

        print(rows, "category deleted")

    elif choice == "11":
        expenses = getAllExpenses()

        for expense in expenses:
            print(expense)

    elif choice == "12":
        id = input("Enter expense id: ")

        expense = getExpenseById(id)

        print(expense)

    elif choice == "13":
        amount = input("Enter amount: ")

        transaction_type = input("Enter transaction type(income/expense): ")
        while True:
            if transaction_type == "income" or transaction_type == "expense":
                break
            else:
                transaction_type = input("Enter transaction type(income/expense): ")      

        user_id = input("Enter user id: ")
        while True:
            if getUserById(user_id):
                break
            else:
                user_id = input("Enter user id: ")


        category_id = input("Enter category id: ")
        while True:
            if getCategoryById(category_id):
                break
            else:
                category_id = input("Enter category id: ")

        description = input("Enter description: ")

        id = createExpense(amount, transaction_type, user_id, category_id, description)

        print("Expense created with id", id)

    elif choice == "14":
        id = input("Enter expense id: ")
        amount = input("Enter amount: ")
        transaction_type = input("Enter transaction type: ")
        user_id = input("Enter user id: ")
        category_id = input("Enter category id: ")
        description = input("Enter description: ")

        rows = updateExpense(id, amount, transaction_type, user_id, category_id, description)

        print(rows, "expense updated")

    elif choice == "15":
        id = input("Enter expense id: ")

        rows = deleteExpense(id)

        print(rows, "expense deleted")
        
    elif choice == "99":
        break
    else:
        print("Invalid choice")

mydb.close()
print("Disconnected from MySQL")