from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_createDictWindow(object):
    def setupUi(self, createDictWindow):
        createDictWindow.setObjectName("createDictWindow")
        createDictWindow.setFixedSize(300, 190)

        self.centralwidget = QtWidgets.QWidget(parent=createDictWindow)
        self.centralwidget.setObjectName('centralwidget')

        self.titleLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(0, 0, 300, 70))
        self.titleLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.titleLabel.setObjectName('titleLabel')

        self.editName = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.editName.setGeometry(QtCore.QRect(25, 70, 250, 30))
        self.editName.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        self.editName.setObjectName('editName')

        self.createDictButton = QtWidgets.QPushButton(
            parent=self.centralwidget)
        self.createDictButton.setGeometry(QtCore.QRect(95, 120, 100, 50))

        createDictWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(createDictWindow)
        QtCore.QMetaObject.connectSlotsByName(createDictWindow)

    def retranslateUi(self, createDictWidow):
        _translate = QtCore.QCoreApplication.translate

        createDictWidow.setWindowTitle(_translate(
            "createDictWidow", "MemoryCards"))

        self.titleLabel.setText(_translate(
            "createDictWidow", "Создание словаря"))
        self.editName.setPlaceholderText(
            _translate("createDictWidow", "Название"))
        self.createDictButton.setText(_translate("createDictWidow", "Создать"))


class CreateDictWindow(QtWidgets.QMainWindow, Ui_createDictWindow):
    def __init__(self, app):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        self.app = app

        # слушатели кнопок
        self.createDictButton.clicked.connect(self.createDict)

    def createDict(self):
        name = self.editName.text()
        try:
            f = open(self.app.getDirectory() + name + '.db', 'w')
            f.close()
        except IOError as e:
            self.app.errorMessage("Не удалось создать словарь")

        self.app.getDictsWindow().updateList()
        self.close()


def load_styles(app, file_styles):
    f = open(file_styles, 'r')
    styles = f.read()
    app.setStyleSheet(styles)
