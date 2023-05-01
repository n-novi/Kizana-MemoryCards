from src.control.DataBaseManager import DataBaseManager
import random


class Controller:
    def __init__(self, db_path):
        self.db_path = db_path
        self.db_manager = DataBaseManager(self.db_path)
        self.table = self.db_manager.getData()

        self.changedRow = None

        self.end = False
        self.curRowIndex = 0
        self.mistakesList = []

    def replace(self):
        replaced_table = []
        for row in self.table:
            row = list(row)
            row[1], row[2] = row[2], row[1]
            row = tuple(row)
            replaced_table.append(row)
        self.table = replaced_table

    def setChangedRow(self, changedRow):
        self.changedRow = changedRow

    def getChangedRow(self):
        return self.changedRow

    def next(self):
        if self.curRowIndex == len(self.table) - 1:
            self.end = True
        else:
            self.curRowIndex += 1

    def getRow(self):
        if self.end is False:
            return self.table[self.curRowIndex]

    def getEnd(self):
        return self.end

    def match(self, word):
        if self.table[self.curRowIndex][2] != word:
            self.mistakesList.append(self.table[self.curRowIndex])
            return False
        return True

    def shuffleCards(self):
        random.shuffle(self.table)

    def reset(self):
        self.end = False
        self.curRowIndex = 0
        self.mistakesList = []

    def getTable(self):
        return self.table

    def getTableSize(self):
        return len(self.table)

    def getCurIndex(self):
        return self.curRowIndex

    def getMistakesList(self):
        return self.mistakesList

    def getMistakesCounter(self):
        return len(self.mistakesList)

    def add(self, record):
        self.db_manager.insert(record)
        self.table = self.db_manager.getData()

    def delete(self, record):
        self.db_manager.delete(record)
        self.table = self.db_manager.getData()

    def update(self, id, record):
        self.db_manager.update(id, record)
        self.table = self.db_manager.getData()

    def close(self):
        self.db_manager.close()
