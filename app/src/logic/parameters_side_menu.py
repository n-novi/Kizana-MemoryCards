import json
from PyQt6 import QtCore, QtWidgets


class ParametersSideMenu:
    """
    Класс для управления боковым меню с параметрами приложения.

    Args:
        main_win: Основное окно приложения.
    """

    def __init__(self, main_win):
        """
        Инициализация объекта класса ParametersSideMenu.

        Args:
            main_win: Основное окно приложения.
        """
        self.main_win = main_win
        self.app = main_win.getApplication()

        # Слушатели кнопок
        self.main_win.modeComboBox.currentIndexChanged.connect(self.changedMode)
        self.main_win.saveParBtn.clicked.connect(self.saveParameters)

    def changedMode(self):
        """
        Обработчик изменения режима приложения.
        """
        mode = self.main_win.modeComboBox.currentIndex()
        if mode < len(self.app.MODE):
            self.app.setMode(self.app.MODE(mode))
            self.main_win.getPlayPanel().openPage()

    def saveParameters(self):
        """
        Сохраняет параметры приложения в конфигурационный файл.
        """
        with open(self.app.getConfigPath()) as f:
            data = json.load(f)

        for i in range(len(self.app.MODE)):
            if self.app.getMode() == self.app.MODE(i):
                data["app_play_parameters"]["mode"] = i

        with open(self.app.getConfigPath(), 'w') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
