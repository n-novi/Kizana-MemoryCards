from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_EditWindow(object):
    def setupUi(self, editWindow):
        editWindow.setObjectName("MainWindow")
        editWindow.setFixedSize(400, 600)

        self.centralwidget = QtWidgets.QWidget(parent=editWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.dictName = QtWidgets.QLabel(parent=self.centralwidget)
        self.dictName.setGeometry(QtCore.QRect(0, 0, 400, 50))
        self.dictName.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.dictName.setObjectName("dictName")

        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 50, 360, 110))
        self.groupBox.setObjectName("groupBox")

        self.textEditWord = QtWidgets.QLineEdit(parent=self.groupBox)
        self.textEditWord.setGeometry(QtCore.QRect(10, 10, 340, 40))
        self.textEditWord.setObjectName("textEditWord")

        self.textEditMeaning = QtWidgets.QLineEdit(parent=self.groupBox)
        self.textEditMeaning.setGeometry(QtCore.QRect(10, 60, 340, 40))
        self.textEditMeaning.setObjectName("textEditMeaning")

        self.addButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.addButton.move(160, 170)
        self.addButton.setObjectName("addButton")

        self.labelResult = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelResult.setGeometry(QtCore.QRect(0, 210, 400, 40))
        self.labelResult.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelResult.setObjectName("labelResult")

        self.labelLCol = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelLCol.setGeometry(QtCore.QRect(20, 250, 180, 30))
        self.labelLCol.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelLCol.setObjectName("labelLCol")

        self.labelRCol = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelRCol.setGeometry(QtCore.QRect(200, 250, 180, 30))
        self.labelRCol.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelRCol.setObjectName("labelRCol")

        self.listWord = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWord.setGeometry(QtCore.QRect(20, 280, 178, 265))
        self.listWord.setObjectName("listWord")

        self.listMeaning = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listMeaning.setGeometry(QtCore.QRect(202, 280, 180, 265))
        self.listMeaning.setObjectName("listMeaning")

        self.horizontalLayoutWidget = QtWidgets.QWidget(
            parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 545, 360, 55))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.deleteButton = QtWidgets.QPushButton(
            parent=self.horizontalLayoutWidget)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout.addWidget(self.deleteButton)

        self.changeButton = QtWidgets.QPushButton(
            parent=self.horizontalLayoutWidget)
        self.changeButton.setObjectName("changeButton")
        self.horizontalLayout.addWidget(self.changeButton)

        editWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(editWindow)
        QtCore.QMetaObject.connectSlotsByName(editWindow)

    def retranslateUi(self, editWindow):
        _translate = QtCore.QCoreApplication.translate
        editWindow.setWindowTitle(_translate("editWindow", "EditWindow"))
        self.addButton.setText(_translate("editWindow", "Добавить"))
        self.labelResult.setText(_translate(
            "editWindow", "Результат редактирования"))
        self.textEditWord.setPlaceholderText(_translate("editWindow", "Слово - en"))
        self.textEditMeaning.setPlaceholderText(
            _translate("editWindow", "Значение - ru"))
        self.labelLCol.setText(_translate("editWindow", "Слово"))
        self.labelRCol.setText(_translate("editWindow", "Значение"))
        self.deleteButton.setText(_translate("editWindow", "Удалить"))
        self.changeButton.setText(_translate("editWindow", "Изменить"))


class EditWindow(QtWidgets.QMainWindow, Ui_EditWindow):
    def __init__(self, app):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        self.app = app
        self.controller = self.app.getController()
        self.selectedDict = None

        self.setInfo()
        self.setDicts()

        # слушатели кнопок
        self.listWord.itemClicked.connect(self.selectDict)
        self.addButton.clicked.connect(self.addRow)
        self.deleteButton.clicked.connect(self.deleteRow)
        self.changeButton.clicked.connect(self.openChangeWindow)

    def setInfo(self):
        self.dictName.setText(self.app.getDictName())

    def setDicts(self):
        table = self.controller.getTable()
        for row in table:
            wordItem = QtWidgets.QListWidgetItem()
            wordItem.setText(row[1])
            meaningItem = QtWidgets.QListWidgetItem()
            meaningItem.setText(row[2])
            self.listWord.addItem(wordItem)
            self.listMeaning.addItem(meaningItem)

    def updateLists(self):
        self.listWord.clear()
        self.listMeaning.clear()

        self.setDicts()

    def addRow(self):
        word = self.textEditWord.text()
        meaning = self.textEditMeaning.text()
        record = (word, meaning)

        self.controller.add(record)

        self.textEditWord.clear()
        self.textEditMeaning.clear()
        self.updateLists()
        if self.app.getMainWindow() is not None:
            self.app.getMainWindow().reload()

    def selectDict(self):
        self.selectedDict = self.listWord.currentRow()

    def deleteRow(self):
        if self.selectedDict is not None:
            deletedIndex = self.selectedDict
            self.controller.delete(self.controller.getTable()[deletedIndex][0])

            self.updateLists()
            if self.app.getMainWindow() is not None:
                self.app.getMainWindow().reload()

    def openChangeWindow(self):
        if self.selectedDict is not None:
            changedIndex = self.selectedDict
            row = self.controller.getTable()[changedIndex]
            self.controller.setChangedRow(row)

            self.app.openChangeWindow()

    def closeEvent(self, event):
        if self.app.getMainWindow() is not None:
            self.app.getMainWindow().reload()
