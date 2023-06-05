import sys
import typing
import json
from PyQt6 import QtWidgets, QtGui
from enum import Enum
from app.src.logic.main_window import MainWindow
from app.src.logic.contoller.Controller import Controller
import ctypes
myappid = u'Kizana.Flash_v2.1' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


class Application(QtWidgets.QApplication):
    class MODE(Enum):
        View = 0
        Answer = 1
        Test = 2

    class THEME(Enum):
        LIGHT = 0
        DARK = 1

    def __init__(self, argv: typing.List[str]):
        super().__init__(argv)

        self.config_path = "app/res/config/app_config.json"

        # полученные данные из файла конфигурации
        self.app_settings = None
        self.app_info = None
        self.app_play_parameters = None
        self.img_folder_path = None
        self.icon_folder_path = None
        self.dicts_folder_path = None
        self.theme_file_path = None

        self.mode = self.MODE.View
        self.theme = self.THEME.LIGHT

        # объекты приложения
        self.mainWindow = None
        self.controller = None

        # состояние игровой сессии
        self.playSession = False

        self.configApplication()
        self.setWindowIcon(QtGui.QIcon(str(self.icon_folder_path) + "/app_icon/app_icon.svg"))
        self.openMainWindow()

    def configApplication(self):  # получение данных из файла конфигурации, установка производится в main_window
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
        return self.app_settings

    def getAppInfo(self):
        return self.app_info

    def getAppPlayParameters(self):
        return self.app_play_parameters

    def getConfigPath(self):
        return self.config_path

    def getDictsFolder(self):
        return self.dicts_folder_path

    def getIconFolder(self):
        return self.icon_folder_path

    def getThemeFiles(self):
        return self.theme_file_path

    def openMainWindow(self):
        self.mainWindow = MainWindow(self)
        self.mainWindow.show()

    def getTheme(self):
        return self.theme

    def setTheme(self, theme):
        if isinstance(theme, Application.THEME):
            self.theme = theme

    def setPlaySession(self, playSession):
        if isinstance(playSession, bool):
            self.playSession = playSession

    def getPlaySession(self):
        return self.playSession

    def setMode(self, mode):
        if isinstance(mode, Application.MODE):
            self.mode = mode

    def getMode(self):
        return self.mode

    def setController(self, controller):
        if isinstance(controller, Controller):
            self.controller = controller
        else:
            controller = None

    def getController(self):
        return self.controller


if __name__ == "__main__":
    app = Application(sys.argv)
    sys.exit(app.exec())
