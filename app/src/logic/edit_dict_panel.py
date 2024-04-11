from PyQt6 import QtCore, QtWidgets

def validation(src_string):
    """
    Проверяет строку на наличие символов.

    Args:
        src_string (str): Исходная строка.

    Returns:
        bool: True, если строка не пустая, False в противном случае.
    """
    if len(src_string) > 0:
        return True
    else:
        return False

class EditDictPanel:
    """
    Класс для управления панелью редактирования словаря.

    Args:
        main_win: Основное окно приложения.

    Attributes:
        main_win: Основное окно приложения.
        app: Объект приложения.
        openEditDictPanelStatus: Статус открытия панели редактирования словаря.
    """
    def __init__(self, main_win):
        """
        Инициализация объекта класса EditDictPanel.

        Args:
            main_win: Основное окно приложения.
        """
        self.main_win = main_win
        self.app = self.main_win.getApplication()
        self.openEditDictPanelStatus = False
        self.initEditDictPanel()

        # Слушатели кнопок
        self.main_win.editBtn.clicked.connect(self.animationEditDictPanel)
        self.main_win.dictTable.cellClicked.connect(self.clickedCell)
        self.main_win.addEditBtn.clicked.connect(self.addRow)
        self.main_win.deleteEditBtn.clicked.connect(self.deleteRow)
        self.main_win.editEditBtn.clicked.connect(self.updateRow)
        self.main_win.sortEditBtn.clicked.connect(self.sortWord)

    def getOpenEditDictPanelStatus(self):
        """
        Возвращает текущий статус открытия панели редактирования словаря.

        Returns:
            bool: Статус открытия панели.
        """
        return self.openEditDictPanelStatus

    def initEditDictPanel(self):
        """
        Инициализирует панель редактирования словаря.
        """
        if self.openEditDictPanelStatus is False:
            self.main_win.frameEditPanel.setMaximumWidth(0)
            self.main_win.editBtn.setChecked(False)
        else:
            self.main_win.frameEditPanel.setMaximumWidth(400)
            self.main_win.editBtn.setChecked(True)

    def addRow(self):
        """
        Добавляет запись в словарь.
        """
        word = self.main_win.leftEdit.text()
        meaning = self.main_win.rightEdit.text()
        if validation(word) and validation(meaning):
            record = (word, meaning)
            self.app.getController().add(record)

            row = self.main_win.dictTable.rowCount()

            self.main_win.dictTable.insertRow(row)
            self.main_win.dictTable.setItem(row, 0, QtWidgets.QTableWidgetItem(word))
            self.main_win.dictTable.setItem(row, 1, QtWidgets.QTableWidgetItem(meaning))

            self.main_win.leftEdit.clear()
            self.main_win.rightEdit.clear()
            self.main_win.getPlayPanel().openPage()

    def sortWord(self):
        """
        Сортирует слова в словаре.
        """
        if self.main_win.sortEditBtn.isChecked():
            self.app.getController().sortTable()
            self.updateDictTable()
        else:
            self.app.getController().reopenDatabase()
            self.updateDictTable()

    def deleteRow(self):
        """
        Удаляет выбранную запись из словаря.
        """
        curRow = self.main_win.dictTable.currentRow()
        if curRow is not None and curRow >= 0:
            self.app.getController().delete(self.app.getController().getTable()[curRow][0])
            self.main_win.dictTable.removeRow(curRow)
            self.main_win.getPlayPanel().openPage()

    def updateRow(self):
        """
        Обновляет выбранную запись в словаре.
        """
        curRow = self.main_win.dictTable.currentRow()
        if curRow is not None and curRow >= 0:
            new_word = self.main_win.leftEdit.text()
            new_meaning = self.main_win.rightEdit.text()

            if validation(new_word) and validation(new_meaning):
                record = (new_word, new_meaning)
                self.app.getController().update(self.app.getController().getTable()[curRow][0], record)

                self.main_win.dictTable.item(curRow, 0).setText(new_word)
                self.main_win.dictTable.item(curRow, 1).setText(new_meaning)

                self.main_win.leftEdit.clear()
                self.main_win.rightEdit.clear()
                self.main_win.getPlayPanel().openPage()

    def clickedCell(self):
        """
        Обрабатывает клик по ячейке таблицы словаря.
        """
        self.main_win.dictTable.clearSelection()
        self.main_win.dictTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.main_win.dictTable.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)

        row_num = self.main_win.dictTable.currentRow()
        self.main_win.dictTable.selectRow(row_num)

    def setDictTable(self):
        """
        Устанавливает таблицу словаря.
        """
        dict_table = self.app.getController().getTable()
        self.main_win.dictTable.setColumnCount(2)
        self.main_win.dictTable.setRowCount(len(dict_table))
        self.main_win.dictTable.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.main_win.dictTable.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.Stretch)

        self.main_win.dictTable.setHorizontalHeaderLabels(["Слово", "Значение"])

        for i in range(len(dict_table)):
            self.main_win.dictTable.setItem(i, 0, QtWidgets.QTableWidgetItem(dict_table[i][1]))
            self.main_win.dictTable.setItem(i, 1, QtWidgets.QTableWidgetItem(dict_table[i][2]))

    def updateDictTable(self):
        """
        Обновляет таблицу словаря.
        """
        self.main_win.dictTable.clear()
        self.main_win.dictTable.clearSelection()
        self.setDictTable()

    def animationEditDictPanel(self):
        """
        Запускает анимацию открытия/закрытия панели редактирования словаря.
        """
        if not self.openEditDictPanelStatus:
            self.animation_1 = QtCore.QPropertyAnimation(self.main_win.frameEditPanel, b"maximumWidth")
            self.animation_1.setDuration(500)
            self.animation_1.setStartValue(0)
            self.animation_1.setEndValue(400)
            self.animation_1.setEasingCurve(QtCore.QEasingCurve.Type.InOutQuart)
            self.animation_1.start()

            self.openEditDictPanelStatus = True
        else:
            self.animation_1 = QtCore.QPropertyAnimation(self.main_win.frameEditPanel, b"maximumWidth")
            self.animation_1.setDuration(500)
            self.animation_1.setStartValue(self.main_win.frameEditPanel.width())
            self.animation_1.setEndValue(0)
            self.animation_1.setEasingCurve(QtCore.QEasingCurve.Type.InOutQuart)
            self.animation_1.start()

            self.openEditDictPanelStatus = False
