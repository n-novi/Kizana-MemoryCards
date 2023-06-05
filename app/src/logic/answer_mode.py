from app.src.logic.result_window import ResultWindow


class AnswerMode:
    def __init__(self, main_win):
        self.main_win = main_win
        self.app = self.main_win.getApplication()
        self.initAnswerMode()

        # слушатели кнопок
        self.main_win.nextAnswerModeBtn.clicked.connect(self.nextWord)

    def initAnswerMode(self):
        self.setInfo()
        self.setWord()

    def setWord(self):
        row = self.app.getController().getRow()
        self.main_win.word.setText(row[1])

    def nextWord(self):
        if self.app.getController().getEnd() is False:
            self.checkAnswer()
        self.app.getController().next()
        if self.app.getController().getEnd() is False:
            self.setWord()

        self.setInfo()
        self.main_win.answerEdit.clear()

        if self.app.getController().getEnd() is True:
            dialog = ResultWindow(self.main_win)
            result = dialog.exec()
            self.reload()

    def checkAnswer(self):
        answer = self.main_win.answerEdit.text()
        self.app.getController().match(answer)

    def setInfo(self):
        curIndex = self.app.getController().getCurIndex() + 1
        totalWords = self.app.getController().getTableSize()
        self.main_win.labelWordCounter.setText(str(curIndex) + "/" + str(totalWords))

        text = "Результат"
        result = self.app.getController().getResult()
        if result is not None:
            if result is True:
                text = "Верно!"
            elif result is False:
                text = "Ошибка!"
            self.main_win.resultAnswerMode.setText(text)
        else:
            self.main_win.resultAnswerMode.setText(text)

        mistakesCounter = self.app.getController().getMistakesCounter()
        self.main_win.mistakeAnswerMode.setText("Ошибки: " + str(mistakesCounter))

    def reload(self):
        self.app.getController().reset()
        self.initAnswerMode()

    def shuffleCards(self):
        self.app.getController().shuffleCards()
        self.reload()
