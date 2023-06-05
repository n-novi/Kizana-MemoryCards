import json
from PyQt6 import QtCore, QtWidgets


class ParametersSideMenu:
    def __init__(self, main_win):
        self.main_win = main_win
        self.app = main_win.getApplication()

        # слушатели кнопок
        self.main_win.modeComboBox.currentIndexChanged.connect(self.changedMode)
        self.main_win.saveParBtn.clicked.connect(self.saveParameters)

    def changedMode(self):
        mode = self.main_win.modeComboBox.currentIndex()
        if mode < len(self.app.MODE):
            self.app.setMode(self.app.MODE(mode))
            self.main_win.getPlayPanel().openPage()

    def saveParameters(self):
        with open(self.app.getConfigPath()) as f:
            data = json.load(f)

        for i in range(len(self.app.MODE)):
            if self.app.getMode() == self.app.MODE(i):
                data["app_play_parameters"]["mode"] = i

        with open(self.app.getConfigPath(), 'w') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
