from app.src.logic.result_window import ResultWindow


class AnswerMode:
    """
    Класс для управления режимом ответа в приложении.

    Attributes:
        main_win: Основное окно приложения.
        app: Экземпляр приложения.
    """

    def __init__(self, main_win):
        """
        Инициализация объекта класса AnswerMode.

        Args:
            main_win: Основное окно приложения.
        """
        self.main_win = main_win
        self.app = self.main_win.getApplication()
        self.initAnswerMode()

        # Слушатели кнопок
        self.main_win.nextAnswerModeBtn.clicked.connect(self.nextWord)

    def initAnswerMode(self):
        """Инициализация режима ответа."""
        self.setInfo()
        self.setWord()

    def setWord(self):
        """Установка слова для отображения."""
        row = self.app.getController().getRow()
        self.main_win.word.setText(row[1])

    def nextWord(self):
        """Переход к следующему слову."""
        if self.app.getController().getEnd() is False:
            self.checkAnswer()
        self.app.getController().next()
        if self.app.getController().getEnd() is False:
            self.setWord()

        self.setInfo()
        self.main_win.answerEdit.clear()

        if self.app.getController().getEnd() is True:
            dialog = ResultWindow(self.main_win)
            dialog.setWindowTitle('Результат')
            result = dialog.exec()
            self.reload()

    def checkAnswer(self):
        """Проверка ответа пользователя."""
        answer = self.main_win.answerEdit.text()
        self.app.getController().match(answer)

    def setInfo(self):
        """Установка информации о текущем состоянии режима ответа."""
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
        """Перезагрузка режима ответа."""
        self.app.getController().reset()
        self.initAnswerMode()

    def shuffleCards(self):
        """Перемешивание карточек."""
        self.app.getController().shuffleCards()
        self.reload()
