class UserDB:
    __db = None

    def __init__(self, db):
        self.__db = db

        cursor = self.db.cursor()
        cursor.execute("SHOW TABLES LIKE 'users'")
        result = cursor.fetchone()

        if not result:
            cursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, email VARCHAR(255), first_name VARCHAR(255), last_name VARCHAR(255), password VARCHAR(255), UNIQUE(email))")
            self.db.commit()

    @property
    def db(self):
        return self.__db

    @db.setter
    def db(self, db):
        self.__db = db

    def find_all(self):
        sql = "SELECT * FROM users"

        cursor = self.db.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()

        return result
    
    def find_by_id(self, id):
        sql = "SELECT * FROM users WHERE id = %s"
        val = (id,)

        cursor = self.db.cursor()
        cursor.execute(sql, val)
        result = cursor.fetchall()

        return result
    
    def find_by_email_and_password(self, email, password):
        sql = "SELECT * FROM users WHERE email = %s AND password = %s"
        val = (email, password)

        cursor = self.db.cursor()
        cursor.execute(sql, val)
        result = cursor.fetchone()

        return result

    def create(self, email, first_name, last_name, password):
        sql = "INSERT INTO users (email, first_name, last_name, password) VALUES (%s, %s, %s, %s)"
        val = (email, first_name, last_name, password)

        cursor = self.db.cursor()
        cursor.execute(sql, val)
        self.db.commit()

        if cursor.rowcount < 1:
            return False
        
        return True
    
    def update(self, id, email, first_name, last_name, password):
        sql = "UPDATE users SET email = %s, first_name = %s, last_name = %s, password = %s WHERE id = %s"
        val = (email, first_name, last_name, password, id)

        cursor = self.db.cursor()
        cursor.execute(sql, val)
        self.db.commit()

        if cursor.rowcount < 1:
            return False
        
        return True
    
    def delete(self, id):
        sql = "DELETE FROM users WHERE id = %s"
        val = (id,)

        cursor = self.db.cursor()
        cursor.execute(sql, val)
        self.db.commit()

        if cursor.rowcount < 1:
            return False
        
        return True
    
    def __del__(self):
        self.db.close()
        print("Connection closed.")
