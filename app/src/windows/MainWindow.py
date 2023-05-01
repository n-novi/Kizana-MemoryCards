from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWin(object):
    def setupUi(self, mainWin):
        mainWin.setObjectName('MainWindow')
        mainWin.setEnabled(True)
        mainWin.setFixedSize(800, 680)

        self.centralwidget = QtWidgets.QWidget(parent=mainWin)
        self.centralwidget.setObjectName('centralwidget')

        self.wordCard = QtWidgets.QLabel(parent=self.centralwidget)
        self.wordCard.setEnabled(True)
        self.wordCard.setGeometry(QtCore.QRect(100, 160, 600, 400))
        self.wordCard.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.wordCard.setWordWrap(True)
        self.wordCard.setObjectName('wordCard')

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

        self.nextButton = QtWidgets.QPushButton(parent=self.controlButtonGroup)
        self.nextButton.setGeometry(QtCore.QRect(100, 2, 80, 80))
        self.nextButton.setObjectName('nextButton')

        self.answerFieldEdit = QtWidgets.QLineEdit(parent=self.mainToolsGroup)
        self.answerFieldEdit.setGeometry(QtCore.QRect(10, 0, 320, 84))
        self.answerFieldEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.answerFieldEdit.setObjectName('answerFieldEdit')

        self.topPanel = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.topPanel.setGeometry(QtCore.QRect(0, 0, 800, 90))
        self.topPanel.setObjectName('topPanel')

        self.topLeftPanel = QtWidgets.QWidget(
            parent=self.topPanel)
        self.topLeftPanel.setGeometry(QtCore.QRect(0, 0, 500, 90))
        self.topLeftPanel.setObjectName("topLeftPanel")

        self.topLeftHorizontalLayout = QtWidgets.QHBoxLayout(
            self.topLeftPanel)
        self.topLeftHorizontalLayout.setContentsMargins(20, 20, 20, 20)
        self.topLeftHorizontalLayout.setObjectName("topLeftHorizontalLayout")

        self.dictButton = QtWidgets.QPushButton(parent=self.topLeftPanel)
        self.dictButton.setObjectName("dictButton")
        self.topLeftHorizontalLayout.addWidget(
            self.dictButton, alignment=QtCore.Qt.AlignmentFlag.AlignLeft)

        self.langButton = QtWidgets.QPushButton(parent=self.topLeftPanel)
        self.langButton.setObjectName("langButton")
        self.topLeftHorizontalLayout.addWidget(
            self.langButton, alignment=QtCore.Qt.AlignmentFlag.AlignLeft)

        self.shuffleButton = QtWidgets.QPushButton(
            parent=self.topLeftPanel)
        self.shuffleButton.setObjectName("shuffleButton")
        self.topLeftHorizontalLayout.addWidget(
            self.shuffleButton, alignment=QtCore.Qt.AlignmentFlag.AlignLeft)

        self.themeButton = QtWidgets.QPushButton(
            parent=self.topLeftPanel)
        self.themeButton.setObjectName("themeButton")
        self.topLeftHorizontalLayout.addWidget(
            self.themeButton, alignment=QtCore.Qt.AlignmentFlag.AlignLeft)

        self.infoButton = QtWidgets.QPushButton(
            parent=self.topLeftPanel)
        self.infoButton.setObjectName("infoButton")
        self.topLeftHorizontalLayout.addWidget(
            self.infoButton, alignment=QtCore.Qt.AlignmentFlag.AlignLeft)

        self.topLeftHorizontalLayout.addStretch(1)

        self.topRightPanel = QtWidgets.QWidget(
            parent=self.topPanel)
        self.topRightPanel.setGeometry(QtCore.QRect(500, 0, 300, 90))
        self.topRightPanel.setObjectName("top")

        self.topRightHorizontalLayout = QtWidgets.QHBoxLayout(
            self.topRightPanel)
        self.topRightHorizontalLayout.addStretch(1)
        self.topRightHorizontalLayout.setContentsMargins(20, 20, 20, 20)
        self.topRightHorizontalLayout.setObjectName("topRightHorizontalLayout")

        self.editButton = QtWidgets.QPushButton(parent=self.topRightPanel)
        self.editButton.setObjectName("editButton")
        self.topRightHorizontalLayout.addWidget(
            self.editButton, alignment=QtCore.Qt.AlignmentFlag.AlignRight)

        self.infoPanel = QtWidgets.QWidget(parent=self.centralwidget)
        self.infoPanel.setGeometry(QtCore.QRect(100, 100, 200, 50))
        self.infoPanel.setObjectName("infoPanel")

        self.gridLayout = QtWidgets.QGridLayout(self.infoPanel)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.progressLabel = QtWidgets.QLabel(parent=self.infoPanel)
        self.progressLabel.setObjectName("progressLabel")
        self.gridLayout.addWidget(self.progressLabel, 0, 0, 1, 1)

        self.mistakeLabel = QtWidgets.QLabel(parent=self.infoPanel)
        self.mistakeLabel.setObjectName("mistakeLabel")
        self.gridLayout.addWidget(self.mistakeLabel, 0, 1, 1, 1)

        self.resultLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.resultLabel.setGeometry(QtCore.QRect(350, 100, 300, 50))
        self.resultLabel.setObjectName("resultLabel")

        self.retranslateUi(mainWin)
        mainWin.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(mainWin)

    def retranslateUi(self, mainWin):
        _translate = QtCore.QCoreApplication.translate
        self.answerFieldEdit.setPlaceholderText(
            _translate("mainWin", "Ответ"))
        self.mistakeLabel.setText(_translate(
            "mainWin", "Ошибки: 0"))
        self.dictButton.setText(_translate("mainWin", "Словари"))
        self.langButton.setText(_translate("mainWin", "EN - RU"))
        self.shuffleButton.setText(_translate("mainWin", "Перемешать"))
        self.editButton.setText(_translate("mainWin", "Изменить"))


class MainWin(QtWidgets.QMainWindow, Ui_MainWin):
    def __init__(self, app):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        self.app = app
        self.controller = self.app.getController()
        self.setTitle()
        self.loadPic()
        self.setTheme()
        self.setLang()

        self.reload()

        # слушатели кнопок
        self.nextButton.clicked.connect(self.nextWord)
        self.reloadButton.clicked.connect(self.reload)
        self.shuffleButton.clicked.connect(self.shuffleCards)
        self.dictButton.clicked.connect(self.openDictsWindow)
        self.editButton.clicked.connect(self.openEditWindow)
        self.themeButton.clicked.connect(self.changeTheme)
        self.langButton.clicked.connect(self.changeLang)

    def setTitle(self):
        self.setWindowTitle("Kizana MemoryCards - " + self.app.getDictName())

    def setInfo(self):
        self.progressLabel.setText(str(self.controller.getCurIndex(
        ) + 1) + " / " + str(self.controller.getTableSize()))

        self.mistakeLabel.setText(
            "Ошибки: " + str(self.controller.getMistakesCounter()))

    def setWord(self):
        row = self.controller.getRow()
        self.wordCard.setText(row[1])

    def nextWord(self):
        if self.controller.getEnd() is False:
            self.checkAnswer()
        self.controller.next()
        if self.controller.getEnd() is False:
            self.setWord()
        self.setInfo()
        self.answerFieldEdit.clear()

        if self.controller.getEnd() is True:
            self.app.openResultWindow()

    def checkAnswer(self):
        answer = self.answerFieldEdit.text()
        result = self.controller.match(answer)
        if result is True:
            self.resultLabel.setText("Верно!")
        else:
            self.resultLabel.setText(
                "Ошибка. Ответ: " + self.controller.getTable()[self.controller.getCurIndex()][2])

    def loadPic(self):
        self.iconLightTheme = QtGui.QIcon()
        self.iconLightTheme.addPixmap(QtGui.QPixmap(self.app.getImgDirectory() + 'light_theme.png'),
                                      QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)

        self.iconDarkTheme = QtGui.QIcon()
        self.iconDarkTheme.addPixmap(QtGui.QPixmap(self.app.getImgDirectory() + 'dark_theme.png'),
                                     QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)

    def setTheme(self):
        if self.app.getTheme() == self.app.THEME.LIGHT:
            self.themeButton.setIcon(self.iconLightTheme)
        elif self.app.getTheme() == self.app.THEME.DARK:
            self.themeButton.setIcon(self.iconDarkTheme)
        self.themeButton.setIconSize(QtCore.QSize(35, 35))

    def setLang(self):
        if self.app.getLang() == self.app.LANG.RU:
            self.app.setLang(self.app.LANG.RU)
            self.controller.replace()
        elif self.app.getLang() == self.app.LANG.EN:
            self.app.setLang(self.app.LANG.EN)

    def changeTheme(self):
        if self.app.getTheme() == self.app.THEME.LIGHT:
            self.app.setTheme(self.app.THEME.DARK)
            self.themeButton.setIcon(self.iconDarkTheme)
        elif self.app.getTheme() == self.app.THEME.DARK:
            self.app.setTheme(self.app.THEME.LIGHT)
            self.themeButton.setIcon(self.iconLightTheme)

    def changeLang(self):
        if self.app.getLang() == self.app.LANG.RU:
            self.app.setLang(self.app.LANG.EN)
        elif self.app.getLang() == self.app.LANG.EN:
            self.app.setLang(self.app.LANG.RU)
        self.controller.replace()
        self.reload()

    def reload(self):
        self.controller.reset()
        self.setWord()
        self.setInfo()
        self.resultLabel.clear()

    def shuffleCards(self):
        self.controller.shuffleCards()
        self.reload()

    def openDictsWindow(self):
        self.app.openDictsWindow()

    def openEditWindow(self):
        self.app.openEditWindow()
