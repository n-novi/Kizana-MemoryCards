from app.src.logic.controller.DataBaseManager import DataBaseManager
import random
import os


class Controller:
    """
    Класс Controller управляет взаимодействием между пользовательским интерфейсом и базой данных.

    Attributes:
        db_path (str): Путь к файлу базы данных.
        db_manager (DataBaseManager): Экземпляр класса DataBaseManager.
        table (list): Список кортежей, представляющих записи базы данных.
        changedRow (tuple): Измененная запись.
        end (bool): Указывает на достижение конца таблицы во время навигации.
        result (bool): Результат сопоставления введенного пользователем слова с ожидаемым.
        curRowIndex (int): Индекс текущей строки, отображаемой пользователю.
        mistakesList (list): Список кортежей, представляющих ошибки, допущенные пользователем.
        user_answer_mistakes (list): Список неправильных ответов пользователя.
    """

    def __init__(self, db_path):
        """
        Инициализация Controller с указанным путем к базе данных.

        Args:
            db_path (str): Путь к файлу базы данных.
        """
        self.db_path = db_path
        self.db_manager = DataBaseManager(self.db_path)
        self.table = self.db_manager.getData()

        self.changedRow = None

        self.end = False
        self.result = None
        self.curRowIndex = 0
        self.mistakesList = []
        self.user_answer_mistakes = []

    def sortTable(self):
        """
        Сортировка таблицы по второму столбцу (индекс 1).
        """
        self.table.sort(key=lambda x: x[1], reverse=False)

    def reopenDatabase(self):
        """Переоткрыть базу данных и обновить таблицу."""
        self.table = self.db_manager.getData()

    def geDictTitle(self):
        """
        Извлечь и вернуть название базы данных из ее пути.

        Returns:
            str: Название базы данных.
        """
        full_name = os.path.basename(self.db_path)
        name = os.path.splitext(full_name)[0]
        return name

    def replace(self):
        """
        Заменить столбцы 1 и 2 местами для каждой записи в таблице.
        """
        replaced_table = []
        for row in self.table:
            row = list(row)
            row[1], row[2] = row[2], row[1]
            row = tuple(row)
            replaced_table.append(row)
        self.table = replaced_table

    def setChangedRow(self, changedRow):
        """
        Установить измененную запись.

        Args:
            changedRow (tuple): Измененная запись.
        """
        self.changedRow = changedRow

    def getChangedRow(self):
        """
        Получить измененную запись.

        Returns:
            tuple: Измененная запись.
        """
        return self.changedRow

    def next(self, cycle=False):
        """
        Перейти к следующей записи в таблице.

        Args:
            cycle (bool): Если True, то при достижении конца таблицы переходит к началу.
        """
        if self.curRowIndex == len(self.table) - 1:
            if cycle:
                self.curRowIndex = 0
            else:
                self.end = True
        else:
            self.curRowIndex += 1

    def prev(self, cycle=False):
        """
        Перейти к предыдущей записи в таблице.

        Args:
            cycle (bool): Если True, то при достижении начала таблицы переходит к концу.
        """
        if self.curRowIndex == 0:
            if cycle:
                self.curRowIndex = len(self.table) - 1
            else:
                self.end = True
        else:
            self.curRowIndex -= 1

    def getRow(self):
        """
        Получить текущую запись из таблицы.

        Returns:
            tuple: Текущая запись.
        """
        if self.end is False:
            return self.table[self.curRowIndex]

    def getEnd(self):
        """
        Получить значение, указывающее на достижение конца таблицы.

        Returns:
            bool: Значение, указывающее на достижение конца таблицы.
        """
        return self.end

    def match(self, word):
        """
        Проверить совпадение введенного пользователем слова с ожидаемым.

        Args:
            word (str): Введенное пользователем слово.
        """
        if self.table[self.curRowIndex][2] != word:
            self.mistakesList.append(self.table[self.curRowIndex])
            self.user_answer_mistakes.append(word)
            self.result = False
        else:
            self.result = True

    def getResult(self):
        """
        Получить результат проверки совпадения слов.

        Returns:
            bool: Результат проверки совпадения слов.
        """
        return self.result

    def shuffleCards(self):
        """Перемешать записи в таблице."""
        random.shuffle(self.table)

    def reset(self):
        """Сбросить состояние контроллера."""
        self.result = None
        self.end = False
        self.curRowIndex = 0
        self.mistakesList = []
        self.user_answer_mistakes = []

    def getTable(self):
        """
        Получить таблицу записей.

        Returns:
            list: Таблица записей.
        """
        return self.table

    def getTableSize(self):
        """
        Получить размер таблицы записей.

        Returns:
            int: Размер таблицы записей.
        """
        return len(self.table)

    def getCurIndex(self):
        """
        Получить индекс текущей записи.

        Returns:
            int: Индекс текущей записи.
        """
        return self.curRowIndex

    def getMistakesList(self):
        """
        Получить список ошибок.

        Returns:
            list: Список ошибок.
        """
        return self.mistakesList

    def getUserMistakesList(self):
        """
        Получить список неправильных ответов пользователя.

        Returns:
            list: Список неправильных ответов пользователя.
        """
        return self.user_answer_mistakes

    def getMistakesCounter(self):
        """
        Получить количество ошибок.

        Returns:
            int: Количество ошибок.
        """
        return len(self.mistakesList)

    def add(self, record):
        """
        Добавить запись в базу данных.

        Args:
            record (tuple): Добавляемая запись.
        """
        self.db_manager.insert(record)
        self.table = self.db_manager.getData()

    def delete(self, record):
        """
        Удалить запись из базы данных.

        Args:
            record (tuple): Удаляемая запись.
        """
        self.db_manager.delete(record)
        self.table = self.db_manager.getData()

    def update(self, id, record):
        """
        Обновить запись в базе данных.

        Args:
            id (int): Идентификатор записи для обновления.
            record (tuple): Обновленная запись.
        """
        self.db_manager.update(id, record)
        self.table = self.db_manager.getData()

    def close(self):
        """Закрыть соединение с базой данных."""
        self.db_manager.close()
