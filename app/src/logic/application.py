import sys
import typing
import json
from PyQt6 import QtWidgets, QtGui
from enum import Enum
from app.src.logic.main_window import MainWindow
from app.src.logic.controller.Controller import Controller
import ctypes

myappid = u'Kizana.MemoryCards_v2.2'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


class Application(QtWidgets.QApplication):
    """
    Класс приложения, управляющий графическим интерфейсом и логикой приложения.

    Attributes:
        config_path (str): Путь к файлу конфигурации приложения.
        app_settings (dict or None): Настройки приложения.
        app_info (dict or None): Информация о приложении.
        app_play_parameters (dict or None): Параметры игровой сессии.
        img_folder_path (str or None): Путь к папке с изображениями.
        icon_folder_path (str or None): Путь к папке с иконками.
        dicts_folder_path (str or None): Путь к папке с базами данных.
        theme_file_path (dict or None): Пути к файлам тем оформления.
        mode (Application.MODE): Режим работы приложения.
        theme (Application.THEME): Тема оформления приложения.
        mainWindow: Основное окно приложения.
        controller: Контроллер приложения.
        playSession (bool): Флаг игровой сессии.
    """

    class MODE(Enum):
        """Перечисление режимов работы приложения."""
        View = 0
        Answer = 1
        Test = 2

    class THEME(Enum):
        """Перечисление тем оформления приложения."""
        LIGHT = 0
        DARK = 1

    def __init__(self, argv: typing.List[str]):
        """
        Инициализация объекта класса Application.

        Args:
            argv (list): Список аргументов командной строки.
        """
        super().__init__(argv)

        self.config_path = "app/res/config/app_config.json"
        self.app_settings = None
        self.app_info = None
        self.app_play_parameters = None
        self.img_folder_path = None
        self.icon_folder_path = None
        self.dicts_folder_path = None
        self.theme_file_path = None
        self.mode = self.MODE.View
        self.theme = self.THEME.LIGHT
        self.mainWindow = None
        self.controller = None
        self.playSession = False

        self.configApplication()
        self.setWindowIcon(QtGui.QIcon(str(self.icon_folder_path) + "/app_icon/app_icon_2.svg"))
        self.openMainWindow()

    def configApplication(self):
        """Конфигурация приложения."""
        with open(self.config_path) as f:
            config = json.load(f)

        app_company = config["app_info"]["app_company"]
        app_title = config["app_info"]["app_title"]
        app_version = config["app_info"]["app_version"]
        app_author = config["app_info"]["author"]
        app_developer = config["app_info"]["developer"]
        self.app_info = {"app_company": app_company, "app_title": app_title, "app_version": app_version,
                         "author": app_author, "developer": app_developer}

        theme = config["app_settings"]["theme"]
        self.app_settings = {"theme": theme}

        mode = config["app_play_parameters"]["mode"]
        self.app_play_parameters = {"mode": mode}

        self.dicts_folder_path = config["app_path"]["database"]
        self.icon_folder_path = config["app_path"]["icon"]
        self.img_folder_path = config["app_path"]["img"]

        light_theme = config["app_path"]["style"]["light"]
        dark_theme = config["app_path"]["style"]["dark"]
        self.theme_file_path = {"light": light_theme, "dark": dark_theme}

    def getAppSettings(self):
        """Получить настройки приложения."""
        return self.app_settings

    def getAppInfo(self):
        """Получить информацию о приложении."""
        return self.app_info

    def getAppPlayParameters(self):
        """Получить параметры игровой сессии."""
        return self.app_play_parameters

    def getConfigPath(self):
        """Получить путь к файлу конфигурации приложения."""
        return self.config_path

    def getDictsFolder(self):
        """Получить путь к папке с базами данных."""
        return self.dicts_folder_path

    def getIconFolder(self):
        """Получить путь к папке с иконками."""
        return self.icon_folder_path

    def getThemeFiles(self):
        """Получить пути к файлам тем оформления."""
        return self.theme_file_path

    def openMainWindow(self):
        """Открыть основное окно приложения."""
        self.mainWindow = MainWindow(self)
        self.mainWindow.show()

    def getTheme(self):
        """Получить тему оформления приложения."""
        return self.theme

    def setTheme(self, theme):
        """
        Установить тему оформления приложения.

        Args:
            theme (Application.THEME): Тема оформления.
        """
        if isinstance(theme, Application.THEME):
            self.theme = theme

    def setPlaySession(self, playSession):
        """
        Установить флаг игровой сессии.

        Args:
            playSession (bool): Флаг игровой сессии.
        """
        if isinstance(playSession, bool):
            self.playSession = playSession

    def getPlaySession(self):
        """Получить флаг игровой сессии."""
        return self.playSession

    def setMode(self, mode):
        """
        Установить режим работы приложения.

        Args:
            mode (Application.MODE): Режим работы приложения.
        """
        if isinstance(mode, Application.MODE):
            self.mode = mode

    def getMode(self):
        """Получить режим работы приложения."""
        return self.mode

    def setController(self, controller):
        """
        Установить контроллер приложения.

        Args:
            controller (Controller): Контроллер приложения.
        """
        if isinstance(controller, Controller):
            self.controller = controller
        else:
            controller = None

    def getController(self):
        """Получить контроллер приложения."""
        return self.controller


if __name__ == "__main__":
    app = Application(sys.argv)
    sys.exit(app.exec())
