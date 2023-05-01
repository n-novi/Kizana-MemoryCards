from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ChangeWindow(object):
    def setupUi(self, changeWindow):
        changeWindow.setObjectName("changeWindow")
        changeWindow.setFixedSize(400, 160)

        self.centralwidget = QtWidgets.QWidget(parent=changeWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.prevWord = QtWidgets.QLabel(parent=self.centralwidget)
        self.prevWord.setGeometry(QtCore.QRect(15, 20, 180, 30))
        self.prevWord.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.prevWord.setObjectName("prevWord")

        self.prevMeaning = QtWidgets.QLabel(parent=self.centralwidget)
        self.prevMeaning.setGeometry(QtCore.QRect(205, 20, 180, 30))
        self.prevMeaning.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.prevMeaning.setObjectName("prevMeaning")

        self.textEditNewWord = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.textEditNewWord.setGeometry(QtCore.QRect(15, 70, 180, 30))
        self.textEditNewWord.setObjectName("textEditNewWord")

        self.textEditNewMeaning = QtWidgets.QLineEdit(
            parent=self.centralwidget)
        self.textEditNewMeaning.setGeometry(QtCore.QRect(205, 70, 180, 30))
        self.textEditNewMeaning.setObjectName("textEditNewMeaning")

        self.changeButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.changeButton.setGeometry(QtCore.QRect(145, 120, 110, 30))
        self.changeButton.setObjectName("changeButton")

        changeWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(changeWindow)
        QtCore.QMetaObject.connectSlotsByName(changeWindow)

    def retranslateUi(self, changeWindow):
        _translate = QtCore.QCoreApplication.translate
        changeWindow.setWindowTitle(_translate("changeWindow", "MemoryCards"))
        self.changeButton.setText(_translate("changeWindow", "Изменить"))

        self.textEditNewWord.setPlaceholderText(
            _translate("changeWindow", "Новое слово"))
        self.textEditNewMeaning.setPlaceholderText(
            _translate("changeWindow", "Новое значение"))

        self.prevMeaning.setText(
            _translate("changeWindow", "Прежнее значение"))
        self.prevWord.setText(
            _translate("changeWindow", "Прежнее слово"))


class ChangeWindow(QtWidgets.QMainWindow, Ui_ChangeWindow):
    def __init__(self, app):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        self.app = app
        self.controller = self.app.getController()

        self.setInfo()

        # слушатели кнопок
        self.changeButton.clicked.connect(self.changeRow)

    def setInfo(self):
        word = self.controller.getChangedRow()[1]
        meaning = self.controller.getChangedRow()[2]

        self.prevWord.setText(word)
        self.prevMeaning.setText(meaning)

    def changeRow(self):
        id = self.controller.getChangedRow()[0]
        new_word = self.textEditNewWord.text()
        new_meaning = self.textEditNewMeaning.text()
        self.controller.update(id, (new_word, new_meaning))

        self.app.getEditWindow().updateLists()
        if self.app.getMainWindow() is not None:
            self.app.getMainWindow().reload()
        self.close()
