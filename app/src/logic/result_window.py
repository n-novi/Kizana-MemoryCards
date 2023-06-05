from PyQt6 import QtWidgets, QtCore
from app.src.ui.result_interface_ui import Ui_Dialog


class ResultWindow(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, main_win):
        super().__init__()
        self.setupUi(self)
        self.main_win = main_win
        self.app = self.main_win.getApplication()

        self.openMistakesListStatus = True
        self.initResultWindow()

    def initResultWindow(self):
        self.setMistakeTable()
        self.mistakeCounter.setText(
            "Ошибок: " + str(self.app.getController().getMistakesCounter()))

        if self.openMistakesListStatus is True:
            self.moreInfoPanel.setMaximumHeight(300)
        else:
            self.moreInfoPanel.setMaximumHeight(0)

    def setMistakeTable(self):
        mistakes_list = self.app.getController().getMistakesList()
        user_answer_mistakes = self.app.getController().getUserMistakesList()

        self.mistakesTable.setColumnCount(3)
        self.mistakesTable.setRowCount(len(mistakes_list))

        self.mistakesTable.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.mistakesTable.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.mistakesTable.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.mistakesTable.setHorizontalHeaderLabels(["Слово", "Значение", "Ваш ответ"])

        for i in range(len(mistakes_list)):
            self.mistakesTable.setItem(i, 0, QtWidgets.QTableWidgetItem(mistakes_list[i][1]))
            self.mistakesTable.setItem(i, 1, QtWidgets.QTableWidgetItem(mistakes_list[i][2]))
            self.mistakesTable.setItem(i, 2, QtWidgets.QTableWidgetItem(user_answer_mistakes[i]))
