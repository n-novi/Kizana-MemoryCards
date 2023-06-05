from PyQt6 import QtCore, QtWidgets
from app.src.logic.answer_mode import AnswerMode
from app.src.logic.view_mode import ViewMode


class PlayPanel:
    def __init__(self, main_win):
        self.main_win = main_win
        self.app = self.main_win.getApplication()

        self.answerMode = None
        self.view_mode = None

        self.openPage()
        self.main_win.closeBtn.clicked.connect(self.dictClose)

    def openPage(self):
        if self.app.getPlaySession() is True:
            #  выбор режима игры
            self.main_win.getEditDictPanel().updateDictTable()
            self.main_win.dictTitle.setText(self.app.getController().geDictTitle())
            self.main_win.playMode.setText(self.main_win.modeComboBox.currentText())
            self.main_win.statusBar.setHidden(False)

            if self.app.getController().getTableSize() == 0:
                self.main_win.stackedWidgetMode.setCurrentIndex(3)
            else:
                mode = self.app.getMode()
                if mode == self.app.MODE.View:
                    self.main_win.stackedWidgetMode.setCurrentIndex(4)
                    self.view_mode = ViewMode(self.main_win)
                    self.main_win.reloadBtn.clicked.connect(self.view_mode.reload)
                    self.main_win.shuffleBtn.clicked.connect(self.view_mode.shuffleCards)
                elif mode == self.app.MODE.Answer:
                    self.main_win.stackedWidgetMode.setCurrentIndex(0)
                    self.answerMode = AnswerMode(self.main_win)
                    self.main_win.reloadBtn.clicked.connect(self.answerMode.reload)
                    self.main_win.shuffleBtn.clicked.connect(self.answerMode.shuffleCards)
                elif mode == self.app.MODE.Test:
                    pass
        else:
            #  выбор предыгровой страницы
            self.main_win.statusBar.setHidden(True)
            if self.main_win.listDicts.count() == 0:
                self.main_win.stackedWidgetMode.setCurrentIndex(1)
            else:
                self.main_win.stackedWidgetMode.setCurrentIndex(2)

    def dictClose(self):
        self.app.setPlaySession(False)
        if self.main_win.getEditDictPanel().getOpenEditDictPanelStatus():
            self.main_win.getEditDictPanel().animationEditDictPanel()
        self.openPage()
