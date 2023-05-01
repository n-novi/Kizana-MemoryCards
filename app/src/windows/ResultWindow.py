from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ResultWindow(object):
    def setupUi(self, resultWindow):
        resultWindow.setObjectName("MainWindow")
        resultWindow.resize(300, 200)

        self.centralwidget = QtWidgets.QWidget(parent=resultWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.resultLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.resultLabel.setGeometry(QtCore.QRect(50, 60, 211, 31))
        self.resultLabel.setObjectName("titleLabel")

        self.mistakesButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.mistakesButton.setGeometry(QtCore.QRect(30, 140, 101, 41))
        self.mistakesButton.setObjectName("mistakesButton")

        self.reloadButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.reloadButton.setGeometry(QtCore.QRect(192, 140, 61, 41))
        self.reloadButton.setObjectName("reloadButton")

        resultWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(resultWindow)
        QtCore.QMetaObject.connectSlotsByName(resultWindow)

        resultWindow.show()

    def retranslateUi(self, resultWindow):
        _translate = QtCore.QCoreApplication.translate
        resultWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mistakesButton.setText(_translate("MainWindow", "Ошибки"))


class ResultWindow(QtWidgets.QMainWindow, Ui_ResultWindow):
    def __init__(self, app):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        self.app = app
        self.controller = self.app.getController()

        self.setInfo()

        # слушатели кнопок
        self.reloadButton.clicked.connect(self.reload)

    def setInfo(self):
        self.resultLabel.setText(
            "Всего ошибок: " + str(self.controller.getMistakesCounter()))

    def reload(self):
        self.app.getMainWindow().reload()
        self.close()

    def closeEvent(self, event):
        self.app.getMainWindow().reload()
