class ViewMode:
    def __init__(self, main_win):
        self.main_win = main_win
        self.app = self.main_win.getApplication()
        self.translated = False
        self.initViewMode()

        # слушатели кнопок
        self.main_win.nextViewModeBtn.clicked.connect(self.nextWord)
        self.main_win.backViewModeBtn.clicked.connect(self.prevWord)
        self.main_win.answerViewModeBtn.clicked.connect(self.translate)

    def initViewMode(self):
        self.translated = False
        self.setInfo()
        self.setWord()

    def setInfo(self):
        curIndex = self.app.getController().getCurIndex() + 1
        totalWords = self.app.getController().getTableSize()
        self.main_win.labelWordCounterViewMode.setText(str(curIndex) + "/" + str(totalWords))

    def setWord(self):
        row = self.app.getController().getRow()
        self.main_win.wordViewMode.setText(row[1])

    def nextWord(self):
        self.app.getController().next(cycle=True)
        self.setWord()
        self.setInfo()

    def prevWord(self):
        self.app.getController().prev(cycle=True)
        self.setWord()
        self.setInfo()

    def translate(self):
        row = self.app.getController().getRow()
        if self.translated:
            self.main_win.wordViewMode.setText(row[1])
            self.translated = False
        else:
            self.main_win.wordViewMode.setText(row[2])
            self.translated = True

    def reload(self):
        self.app.getController().reset()
        self.initViewMode()

    def shuffleCards(self):
        self.app.getController().shuffleCards()
        self.reload()
