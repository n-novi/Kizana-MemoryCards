import json
from PyQt6 import QtCore, QtWidgets


class SettingsSideMenu:
    """
    Класс для управления боковым меню настроек.

    Args:
        main_win: Основное окно приложения.
    """

    def __init__(self, main_win):
        """
        Инициализация объекта класса SettingsSideMenu.

        Args:
            main_win: Основное окно приложения.
        """
        self.main_win = main_win
        self.app = main_win.getApplication()

        self.main_win.themeComboBox.currentIndexChanged.connect(self.changedTheme)
        self.main_win.saveSettingsBtn.clicked.connect(self.saveSettings)

    def changedTheme(self):
        """
        Обрабатывает изменение темы приложения.
        """
        theme = self.main_win.themeComboBox.currentIndex()
        self.app.setTheme(self.app.THEME(theme))
        self.main_win.setUiTheme()

    def saveSettings(self):
        """
        Сохраняет настройки приложения в конфигурационный файл.
        """
        with open(self.app.getConfigPath()) as f:
            data = json.load(f)

        theme = self.app.getTheme()
        if theme == self.app.THEME.LIGHT:
            data["app_settings"]["theme"] = 'light'
        if theme == self.app.THEME.DARK:
            data["app_settings"]["theme"] = 'dark'

        with open(self.app.getConfigPath(), 'w') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
