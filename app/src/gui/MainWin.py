from PyQt6 import QtCore, QtGui, QtWidgets

# TODO: добавить логику для кнопок


class MainWin(object):  # Окно главного окна приложения
    def __init__(self):
        self.MainWindow = QtWidgets.QMainWindow()

    def setupUi(self):
        self.MainWindow.setObjectName('MainWindow')
        self.MainWindow.setEnabled(True)
        self.MainWindow.setFixedSize(800, 680)

        self.centralwidget = QtWidgets.QWidget(parent=self.MainWindow)
        self.centralwidget.setObjectName('centralwidget')

        self.wordCard = QtWidgets.QLabel(parent=self.centralwidget)
        self.wordCard.setEnabled(True)
        self.wordCard.setGeometry(QtCore.QRect(100, 160, 600, 400))
        self.wordCard.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.wordCard.setObjectName('wordCard')
        self.wordCard.setText("Hello")

        self.mainToolsGroup = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.mainToolsGroup.setGeometry(QtCore.QRect(140, 580, 530, 84))
        self.mainToolsGroup.setObjectName('mainToolsGroup')

        self.controlButtonGroup = QtWidgets.QGroupBox(
            parent=self.mainToolsGroup)
        self.controlButtonGroup.setGeometry(QtCore.QRect(340, 0, 190, 84))
        self.controlButtonGroup.setObjectName('controlButtonGroup')

        self.reloadButton = QtWidgets.QPushButton(
            parent=self.controlButtonGroup)
        self.reloadButton.setGeometry(QtCore.QRect(10, 2, 80, 80))
        self.reloadButton.setObjectName('reloadButton')
        self.reloadButton.setText("R")

        self.nextButton = QtWidgets.QPushButton(parent=self.controlButtonGroup)
        self.nextButton.setGeometry(QtCore.QRect(100, 2, 80, 80))
        self.nextButton.setObjectName('nextButton')
        self.nextButton.setText("N")

        self.answerFieldEdit = QtWidgets.QLineEdit(parent=self.mainToolsGroup)
        self.answerFieldEdit.setGeometry(QtCore.QRect(10, 0, 320, 84))
        self.answerFieldEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.answerFieldEdit.setObjectName('answerFieldEdit')
        self.answerFieldEdit.setPlaceholderText("Ответ")

        self.MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

        self.MainWindow.show()


def load_styles(app, file_styles):  # Функция загрузки стилей
    f = open(file_styles, 'r')
    styles = f.read()
    app.setStyleSheet(styles)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    load_styles(app, 'app/res/styles/styles.qss')
    mainWindow = MainWin()
    mainWindow.setupUi()

    app.exec()
