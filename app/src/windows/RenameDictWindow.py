from PyQt6 import QtCore, QtGui, QtWidgets
import os


class Ui_renameDictWindow(object):
    def setupUi(self, renameDictWindow):
        renameDictWindow.setObjectName("renameDictWindow")
        renameDictWindow.setFixedSize(300, 190)

        self.centralwidget = QtWidgets.QWidget(parent=renameDictWindow)
        self.centralwidget.setObjectName('centralwidget')

        self.titleLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(0, 0, 300, 70))
        self.titleLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.titleLabel.setObjectName('titleLabel')

        self.editName = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.editName.setGeometry(QtCore.QRect(25, 70, 250, 30))
        self.editName.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        self.editName.setObjectName('editName')

        self.renameButton = QtWidgets.QPushButton(
            parent=self.centralwidget)
        self.renameButton.setGeometry(QtCore.QRect(85, 120, 130, 50))

        renameDictWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(renameDictWindow)
        QtCore.QMetaObject.connectSlotsByName(renameDictWindow)

    def retranslateUi(self, renameDictWindow):
        _translate = QtCore.QCoreApplication.translate

        renameDictWindow.setWindowTitle(_translate(
            "renameDictWindow", "MemoryCards"))

        self.titleLabel.setText(_translate(
            "renameDictWindow", "Переименование словаря"))
        self.editName.setPlaceholderText(
            _translate("renameDictWindow", "Название"))
        self.renameButton.setText(_translate(
            "renameDictWindow", "Переименовать"))


class RenameDictWindow(QtWidgets.QMainWindow, Ui_renameDictWindow):
    def __init__(self, app):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        self.app = app

        self.selectedFile = None

        # слушатели кнопок
        self.renameButton.clicked.connect(self.renameDict)

    def renameDict(self):
        name = self.editName.text()

        file = self.app.getDirectory() + self.app.getSelectedFile() + '.db'
        new_file = self.app.getDirectory() + name + '.db'

        nameOpenDict = self.app.getDictName()
        controller = self.app.getController()

        if controller is not None:
            self.app.getController().close()

        try:
            os.rename(file, new_file)
        except OSError as e:
            self.app.errorMessage("Не удалось переименовать словарь")

        if controller is not None and self.app.getSelectedFile() == nameOpenDict:
            self.app.setController(name)
        elif controller is not None and self.app.getSelectedFile() != nameOpenDict:
            self.app.setController(nameOpenDict)

        self.app.getDictsWindow().updateList()
        if self.app.getController() is not None and self.app.getMainWindow() is not None:
            self.app.getMainWindow().setTitle()

        self.close()
