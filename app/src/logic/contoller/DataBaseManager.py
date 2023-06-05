import sqlite3 as sl
from sqlite3 import Error


class DataBaseManager:
    def __init__(self, db_path):
        self.cursor = None
        self.table_name = 'dict'
        self.db_path = db_path
        self.connection = None
        self.setConnection()
        self.createTable()

    def executeQuery(self, query, parameters=()):
        if self.connection is None:
            return

        self.cursor = self.connection.cursor()
        try:
            self.cursor.execute(query, parameters)
            self.connection.commit()
            print(f"Запрос выполнен успешно")
        except Error as e:
            print(f"Произошла ошибка '{e}'")

    def setConnection(self):
        try:
            self.connection = sl.connect(self.db_path)
            print("Успешное соединение с БД")
        except Error as e:
            print(f"Произошла ошибка '{e}'")

    def createTable(self):
        createTable_query = f"""
        CREATE TABLE IF NOT EXISTS {self.table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word TEXT NOT NULL,
            meaning TEXT NOT NULL
        );
        """
        self.executeQuery(createTable_query)

    def insert(self, record):
        insert_query = f"INSERT INTO {self.table_name}(word, meaning) VALUES(?, ?)"
        self.executeQuery(insert_query, record)

    def delete(self, id):
        delete_query = f"DELETE FROM {self.table_name} WHERE id = {id}"
        self.executeQuery(delete_query)

    def update(self, id, record):
        update_query = f"UPDATE {self.table_name} SET word = ?, meaning = ? WHERE id = ?"
        data = list(record)
        data.append(id)
        data = tuple(data)
        self.executeQuery(
            update_query, data)

    def getData(self, order=""):
        getAllRecords_query = f"SELECT * FROM {self.table_name} {order}"
        self.executeQuery(getAllRecords_query)
        data = self.cursor.fetchall()
        return data

    def close(self):
        if self.connection is not None:
            self.connection.close()

    def __str__(self):
        data = self.getData()
        return str(data)

    def __del__(self):
        if self.connection is not None:
            self.connection.close()
            print("Соединение с БД закрыто")
