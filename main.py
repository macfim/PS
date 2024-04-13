import mysql.connector

##############################
# Users Table
##############################

def getAllUsers():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM users")
    myresult = mycursor.fetchall()
    return myresult

def getUserById(id):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM users WHERE id = %s", (id,))
    myresult = mycursor.fetchall()
    return myresult

def createUser(email, username, password):
    mycursor = mydb.cursor()
    sql = "INSERT INTO users (email, username, password) VALUES (%s, %s, %s)"
    val = (email, username, password)
    mycursor.execute(sql, val)
    mydb.commit()
    return mycursor.lastrowid

def updateUser(id, email, username, password):
    mycursor = mydb.cursor()
    sql = "UPDATE users SET email = %s, username = %s, password = %s WHERE id = %s"
    val = (email, username, password, id)
    mycursor.execute(sql, val)
    mydb.commit()
    return mycursor.rowcount

def deleteUser(id):
    mycursor = mydb.cursor()
    sql = "DELETE FROM users WHERE id = %s"
    val = (id,)
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
print("1. Get all users")
print("2. Get user by id")
print("3. Create user")
print("4. Update user")
print("5. Delete user")
print("99. Exit")

while True:
    choice = input("Enter your choice: ")
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
    elif choice == "99":
        break
    else:
        print("Invalid choice")

mydb.close()
print("Disconnected from MySQL")