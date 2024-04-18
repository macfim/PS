class TransactionDB:
    __db = None

    def __init__(self, db):
        self.__db = db

        cursor = self.db.cursor()
        cursor.execute("SHOW TABLES LIKE 'transactions'")
        result = cursor.fetchone()

        if not result:
            cursor.execute("CREATE TABLE transactions (id INT AUTO_INCREMENT PRIMARY KEY, user_id INT, type ENUM('Income', 'Expense'), amount DECIMAL(10,2), date DATE, description VARCHAR(255), FOREIGN KEY (user_id) REFERENCES users(id))")
            self.db.commit()

    @property
    def db(self):
        return self.__db

    @db.setter
    def db(self, db):
        self.__db = db

    def find_all(self):
        sql = "SELECT * FROM transactions"

        cursor = self.db.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()

        return result
    
    def find_by_id(self, id):
        sql = "SELECT * FROM transactions WHERE id = %s"
        val = (id,)

        cursor = self.db.cursor()
        cursor.execute(sql, val)
        result = cursor.fetchall()

        return result

    def create(self, user_id, type, amount, date, description):
        sql = "INSERT INTO transactions (user_id, type, amount, date, description) VALUES (%s, %s, %s, %s, %s)"
        val = (user_id, type, amount, date, description)

        cursor = self.db.cursor()
        cursor.execute(sql, val)
        self.db.commit()

        if cursor.rowcount < 1:
            return False
        
        return True
    
    def update(self, id, user_id, type, amount, date, description):
        sql = "UPDATE transactions SET user_id = %s, type = %s, amount = %s, date = %s, description = %s WHERE id = %s"
        val = (user_id, type, amount, date, description, id)

        cursor = self.db.cursor()
        cursor.execute(sql, val)
        self.db.commit()

        if cursor.rowcount < 1:
            return False
        
        return True
    
    def delete(self, id):
        sql = "DELETE FROM transactions WHERE id = %s"
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
