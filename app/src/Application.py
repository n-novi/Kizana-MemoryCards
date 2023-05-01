from PyQt6 import QtCore, QtGui, QtWidgets
from src.windows.MainWindow import MainWin
from src.windows.DictsWindow import DictsWindow
from src.windows.EditDictWindow import EditWindow
from src.windows.CreateDictWindow import CreateDictWindow
from src.windows.ResultWindow import ResultWindow
from src.windows.ChangeWindow import ChangeWindow
from src.windows.RenameDictWindow import RenameDictWindow
from src.control.DataBaseManager import DataBaseManager
from src.control.Controller import Controller
from enum import Enum


class Application(QtWidgets.QApplication):
    THEME = Enum('THEME', 'LIGHT DARK', start=0)
    LANG = Enum('LANG', 'EN RU', start=0)

    def __init__(self, argv, lang, theme, database_dir, styles_dir, img_dir):
        QtWidgets.QApplication.__init__(self, argv)
        self.light_styles_file = styles_dir + 'light_styles.qss'
        self.dark_styles_file = styles_dir + 'dark_styles.qss'
        self.db_directory = database_dir
        self.img_dir = img_dir

        self.theme = theme
        self.lang = lang
        self.mainWindow = None
        self.controller = None
        self.selectedFile = None
        self.curDictName = None

        self.setTheme(self.theme)
        self.openDictsWindow()

    def errorMessage(self, text):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Внимание")
        msgBox.setText("Ошибка!")
        msgBox.setInformativeText(text)
        msgBox.setIconPixmap(QtGui.QPixmap(
            self.getImgDirectory() + 'warning.png').scaled(50, 50))
        msgBox.setStandardButtons(
            QtWidgets.QMessageBox.StandardButton.Cancel)
        ret = msgBox.exec()

        if ret == QtWidgets.QMessageBox.StandardButton.Cancel:
            msgBox.close()

    def getDictName(self):
        return self.curDictName

    def setController(self, name):
        self.curDictName = name
        self.controller = Controller(
            self.getDirectory() + self.curDictName + '.db')

    def getController(self):
        return self.controller

    def setSelectedFile(self, name):
        self.selectedFile = name

    def getSelectedFile(self):
        return self.selectedFile

    def getDirectory(self):
        return self.db_directory

    def getImgDirectory(self):
        return self.img_dir

    def getDictsWindow(self):
        return self.dictsWindow

    def getMainWindow(self):
        return self.mainWindow

    def getEditWindow(self):
        return self.editWindow

    def openDictsWindow(self):
        self.dictsWindow = DictsWindow(self)
        self.dictsWindow.show()

    def openMainWindow(self):
        self.mainWindow = MainWin(self)
        self.mainWindow.show()

    def openEditWindow(self):
        self.editWindow = EditWindow(self)
        self.editWindow.show()

    def openCreateDictWindow(self):
        self.createDictWindow = CreateDictWindow(self)
        self.createDictWindow.show()

    def openResultWindow(self):
        self.resultWindow = ResultWindow(self)
        self.resultWindow.show()

    def openChangeWindow(self):
        self.changeWindow = ChangeWindow(self)
        self.changeWindow.show()

    def openRenameDictWindow(self):
        self.renameDictWindow = RenameDictWindow(self)
        self.renameDictWindow.show()

    def loadLightTheme(self):
        f = open(self.light_styles_file, 'r')
        styles = f.read()
        self.setStyleSheet(styles)
        f.close()

    def loadDarkTheme(self):
        f = open(self.dark_styles_file, 'r')
        styles = f.read()
        self.setStyleSheet(styles)
        f.close()

    def getTheme(self):
        return self.theme

    def setTheme(self, theme):
        self.theme = theme
        if self.theme == self.THEME.LIGHT:
            self.loadLightTheme()
        elif self.theme == self.THEME.DARK:
            self.loadDarkTheme()

    def getLang(self):
        return self.lang

    def setLang(self, lang):
        self.lang = lang


if __name__ == "__main__":
    import sys

    application = Application(sys.argv)
    sys.exit(application.exec())
