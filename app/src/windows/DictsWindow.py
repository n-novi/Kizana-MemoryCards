from PyQt6 import QtCore, QtGui, QtWidgets
import os


class Ui_DictsWin(object):
    def setupUi(self, dictsWin):
        dictsWin.setObjectName("MainWindow")
        dictsWin.setFixedSize(500, 705)

        self.centralwidget = QtWidgets.QWidget(parent=dictsWin)
        self.centralwidget.setObjectName("centralwidget")

        self.titleLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(0, 0, 500, 70))
        self.titleLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")

        self.dictsList = QtWidgets.QListWidget(parent=self.centralwidget)
        self.dictsList.setGeometry(QtCore.QRect(25, 70, 450, 530))
        self.dictsList.setObjectName("dictsList")

        self.horizontalLayoutWidget = QtWidgets.QWidget(
            parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(25, 610, 450, 40))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.openButton = QtWidgets.QPushButton(
            parent=self.horizontalLayoutWidget)
        self.openButton.setObjectName("openButton")
        self.horizontalLayout.addWidget(self.openButton)

        self.createButton = QtWidgets.QPushButton(
            parent=self.horizontalLayoutWidget)
        self.createButton.setObjectName("createButton")
        self.horizontalLayout.addWidget(self.createButton)

        self.renameButton = QtWidgets.QPushButton(
            parent=self.horizontalLayoutWidget)
        self.renameButton.setObjectName("renameButton")
        self.horizontalLayout.addWidget(self.renameButton)

        self.horizontalLayoutWidget2 = QtWidgets.QWidget(
            parent=self.centralwidget)
        self.horizontalLayoutWidget2.setGeometry(
            QtCore.QRect(25, 655, 450, 40))
        self.horizontalLayoutWidget2.setObjectName("horizontalLayoutWidget2")

        self.horizontalLayout2 = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget2)
        self.horizontalLayout2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout2.setObjectName("horizontalLayout2")

        self.editButton = QtWidgets.QPushButton(
            parent=self.horizontalLayoutWidget2)
        self.editButton.setObjectName("editButton")
        self.horizontalLayout2.addWidget(self.editButton)

        self.deleteButton = QtWidgets.QPushButton(
            parent=self.horizontalLayoutWidget2)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout2.addWidget(self.deleteButton)

        dictsWin.setCentralWidget(self.centralwidget)
        self.retranslateUi(dictsWin)
        QtCore.QMetaObject.connectSlotsByName(dictsWin)

    def retranslateUi(self, dictsWin):
        _translate = QtCore.QCoreApplication.translate
        dictsWin.setWindowTitle(_translate("Dictionaries", "Словари"))
        self.titleLabel.setText(_translate("MainWindow", "Ваши словари"))
        self.deleteButton.setText(_translate("MainWindow", "Удалить"))
        self.openButton.setText(_translate("MainWindow", "Открыть"))
        self.createButton.setText(_translate("MainWindow", "Создать"))
        self.renameButton.setText(_translate("MainWindow", "Переименовать"))
        self.editButton.setText(_translate("MainWindow", "Редактировать"))


class DictsWindow(QtWidgets.QMainWindow, Ui_DictsWin):
    def __init__(self, app):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        self.app = app

        self.updateList()
        self.selectedDict = None

        # слушатели кнопок
        self.dictsList.itemClicked.connect(self.selectDict)
        self.openButton.clicked.connect(self.openDict)
        self.deleteButton.clicked.connect(self.deleteDict)
        self.createButton.clicked.connect(self.openCreateDictWindow)
        self.renameButton.clicked.connect(self.openRenameDictWindow)
        self.editButton.clicked.connect(self.openEditWindow)

    def updateList(self):
        self.dicts = self.getDicts()
        self.setDictsList()

    def getDicts(self):
        result = []
        content = os.listdir(self.app.getDirectory())
        for file in content:
            if os.path.isfile(os.path.join(self.app.getDirectory(), file)) and file.endswith('.db'):
                result.append(file)

        return result

    def addElement(self, text):
        item = QtWidgets.QListWidgetItem()
        item.setText(text)
        self.dictsList.addItem(item)

    def setDictsList(self):
        self.dictsList.clear()
        for d in self.dicts:
            file = str(d)
            self.addElement(file[:len(file)-3])

    def selectDict(self, item):
        self.selectedDict = item.text()

    def emptyDictMessage(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Внимание")
        msgBox.setText("Выбранный словарь пуст!")
        msgBox.setInformativeText(
            "Добавьте в словарь слова для изучения")
        msgBox.setIconPixmap(QtGui.QPixmap(
            self.app.getImgDirectory() + 'info.png').scaled(50, 50))
        msgBox.setStandardButtons(
            QtWidgets.QMessageBox.StandardButton.Cancel | QtWidgets.QMessageBox.StandardButton.Ok)
        ret = msgBox.exec()

        if ret == QtWidgets.QMessageBox.StandardButton.Ok:
            self.app.openEditWindow()
        elif ret == QtWidgets.QMessageBox.StandardButton.Cancel:
            msgBox.close()

    def openDict(self):
        if self.selectedDict is not None:
            self.app.setController(self.selectedDict)
            if self.app.getController().getTableSize() == 0:
                self.emptyDictMessage()
            else:
                self.app.openMainWindow()
                self.close()

    def deleteDict(self):
        if self.selectedDict is not None and self.selectedDict != self.app.getDictName():
            try:
                os.remove(self.app.getDirectory() + self.selectedDict + '.db')
            except OSError as e:
                self.app.errorMessage("Не удалось удалить словарь")
            self.updateList()

    def openCreateDictWindow(self):
        self.app.openCreateDictWindow()

    def openRenameDictWindow(self):
        if self.selectedDict is not None:
            self.app.setSelectedFile(self.selectedDict)
            self.app.openRenameDictWindow()

    def openEditWindow(self):
        if self.selectedDict is not None:
            self.app.setController(self.selectedDict)
            self.app.openEditWindow()
