import sqlite3 as sl
from sqlite3 import Error


class DataBaseManager:
    """Класс для управления базой данных SQLite.

    Attributes:
        db_path (str): Путь к файлу базы данных SQLite.
        cursor (sqlite3.Cursor or None): Объект курсора для выполнения запросов.
        table_name (str): Имя таблицы в базе данных.
        connection (sqlite3.Connection or None): Объект соединения с базой данных SQLite.
    """

    def __init__(self, db_path):
        """Инициализирует объект класса DataBaseManager.

        Args:
            db_path (str): Путь к файлу базы данных SQLite.
        """
        self.cursor = None
        self.table_name = 'dict'
        self.db_path = db_path
        self.connection = None
        self.setConnection()
        self.createTable()

    def executeQuery(self, query, parameters=()):
        """Выполняет SQL-запрос к базе данных.

        Args:
            query (str): SQL-запрос.
            parameters (tuple, optional): Параметры запроса. По умолчанию пустой кортеж.
        """
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
        """Устанавливает соединение с базой данных SQLite."""
        try:
            self.connection = sl.connect(self.db_path)
            print("Успешное соединение с БД")
        except Error as e:
            print(f"Произошла ошибка '{e}'")

    def createTable(self):
        """Создает таблицу в базе данных SQLite."""
        createTable_query = f"""
        CREATE TABLE IF NOT EXISTS {self.table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word TEXT NOT NULL,
            meaning TEXT NOT NULL
        );
        """
        self.executeQuery(createTable_query)

    def insert(self, record):
        """Добавляет запись в базу данных SQLite.

        Args:
            record (tuple): Запись для добавления.
        """
        insert_query = f"INSERT INTO {self.table_name}(word, meaning) VALUES(?, ?)"
        self.executeQuery(insert_query, record)

    def delete(self, id):
        """Удаляет запись из базы данных SQLite по идентификатору.

        Args:
            id (int): Идентификатор записи для удаления.
        """
        delete_query = f"DELETE FROM {self.table_name} WHERE id = {id}"
        self.executeQuery(delete_query)

    def update(self, id, record):
        """Обновляет запись в базе данных SQLite по идентификатору.

        Args:
            id (int): Идентификатор записи для обновления.
            record (tuple): Новые данные записи.
        """
        update_query = f"UPDATE {self.table_name} SET word = ?, meaning = ? WHERE id = ?"
        data = list(record)
        data.append(id)
        data = tuple(data)
        self.executeQuery(update_query, data)

    def getData(self, order=""):
        """Получает данные из базы данных SQLite.

        Args:
            order (str, optional): Опциональный параметр сортировки данных. По умолчанию пустая строка.

        Returns:
            list: Данные из базы данных.
        """
        getAllRecords_query = f"SELECT * FROM {self.table_name} {order}"
        self.executeQuery(getAllRecords_query)
        data = self.cursor.fetchall()
        return data

    def close(self):
        """Закрывает соединение с базой данных SQLite."""
        if self.connection is not None:
            self.connection.close()

    def __str__(self):
        """Возвращает строковое представление данных из базы данных.

        Returns:
            str: Строковое представление данных из базы данных.
        """
        data = self.getData()
        return str(data)

    def __del__(self):
        """Деструктор класса, закрывает соединение с базой данных SQLite."""
        if self.connection is not None:
            self.connection.close()
            print("Соединение с БД закрыто")
