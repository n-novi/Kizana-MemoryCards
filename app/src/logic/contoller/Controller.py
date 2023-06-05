from app.src.logic.contoller.DataBaseManager import DataBaseManager
import random
import os


class Controller:
    def __init__(self, db_path):
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
        self.table.sort(key=lambda x: x[1], reverse=False)

    def reopenDatabase(self):
        self.table = self.db_manager.getData()

    def geDictTitle(self):
        full_name = os.path.basename(self.db_path)
        name = os.path.splitext(full_name)[0]
        return name

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

    def next(self, cycle=False):
        if self.curRowIndex == len(self.table) - 1:
            if cycle:
                self.curRowIndex = 0
            else:
                self.end = True
        else:
            self.curRowIndex += 1

    def prev(self, cycle=False):
        if self.curRowIndex == 0:
            if cycle:
                self.curRowIndex = len(self.table) - 1
            else:
                self.end = True
        else:
            self.curRowIndex -= 1

    def getRow(self):
        if self.end is False:
            return self.table[self.curRowIndex]

    def getEnd(self):
        return self.end

    def match(self, word):
        if self.table[self.curRowIndex][2] != word:
            self.mistakesList.append(self.table[self.curRowIndex])
            self.user_answer_mistakes.append(word)
            self.result = False
        else:
            self.result = True

    def getResult(self):
        return self.result

    def shuffleCards(self):
        random.shuffle(self.table)

    def reset(self):
        self.result = None
        self.end = False
        self.curRowIndex = 0
        self.mistakesList = []
        self.user_answer_mistakes = []

    def getTable(self):
        return self.table

    def getTableSize(self):
        return len(self.table)

    def getCurIndex(self):
        return self.curRowIndex

    def getMistakesList(self):
        return self.mistakesList

    def getUserMistakesList(self):
        return self.user_answer_mistakes

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
