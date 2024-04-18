import mysql.connector

from tkinter import *
from classes.App import App

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="joe",
    password="EfFaazcJv_l(3@]M",
    database="main"
)

if not mydb.is_connected():
    print("Failed to connect to MySQL")
    exit()

print("Successfully connected.")

root = Tk()
app = App(root, mydb)
root.mainloop()
