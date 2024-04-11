class ViewMode:
    """
    Класс для представления режима просмотра карточек.

    Args:
        main_win: Основное окно приложения.
    """

    def __init__(self, main_win):
        """
        Инициализация объекта класса ViewMode.

        Args:
            main_win: Основное окно приложения.
        """
        self.main_win = main_win
        self.app = self.main_win.getApplication()
        self.translated = False
        self.initViewMode()

        self.main_win.nextViewModeBtn.clicked.connect(self.nextWord)
        self.main_win.backViewModeBtn.clicked.connect(self.prevWord)
        self.main_win.answerViewModeBtn.clicked.connect(self.translate)

    def initViewMode(self):
        """
        Инициализация режима просмотра.
        """
        self.translated = False
        self.setInfo()
        self.setWord()

    def setInfo(self):
        """
        Установка информации о текущем слове и общем количестве слов.
        """
        curIndex = self.app.getController().getCurIndex() + 1
        totalWords = self.app.getController().getTableSize()
        self.main_win.labelWordCounterViewMode.setText(str(curIndex) + "/" + str(totalWords))

    def setWord(self):
        """
        Установка слова для отображения.
        """
        row = self.app.getController().getRow()
        self.main_win.wordViewMode.setText(row[1])

    def nextWord(self):
        """
        Переход к следующему слову.
        """
        self.app.getController().next(cycle=True)
        self.setWord()
        self.setInfo()

    def prevWord(self):
        """
        Переход к предыдущему слову.
        """
        self.app.getController().prev(cycle=True)
        self.setWord()
        self.setInfo()

    def translate(self):
        """
        Перевод слова.
        """
        row = self.app.getController().getRow()
        if self.translated:
            self.main_win.wordViewMode.setText(row[1])
            self.translated = False
        else:
            self.main_win.wordViewMode.setText(row[2])
            self.translated = True

    def reload(self):
        """
        Перезагрузка режима просмотра.
        """
        self.app.getController().reset()
        self.initViewMode()

    def shuffleCards(self):
        """
        Перемешивание карточек.
        """
        self.app.getController().shuffleCards()
        self.reload()
