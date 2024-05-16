import os
import re
from PyQt6 import QtCore, QtWidgets, QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QSplitter

from app.src.ui.main_interface_ui import Ui_MainWindow
from app.src.logic.side_menu import SideMenu
from app.src.logic.play_panel import PlayPanel
from app.src.logic.edit_dict_panel import EditDictPanel


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """
    Главное окно приложения.

    Attributes:
        app: Объект приложения.
        sideMenu: Панель бокового меню.
        playPanel: Панель воспроизведения словаря.
        editDictPanel: Панель редактирования словаря.
    """

    def __init__(self, app):
        """
        Инициализация главного окна приложения.

        Args:
            app: Объект приложения.
        """
        QtWidgets.QMainWindow.__init__(self)
        self.app = app
        self.setupUi(self)

        self.splitter = QSplitter(Qt.Orientation.Horizontal)
        self.splitter.addWidget(self.frameSubMenu)
        self.splitter.addWidget(self.frameMain)
        self.bodylayout.addWidget(self.splitter)

        self.setSettings()
        self.setUiTheme()

        self.setAppInfo()
        self.setPlayParameters()

        self.sideMenu = None
        self.playPanel = None
        self.editDictPanel = None

        self.buildSideMenu()
        self.buildPlayPanel()
        self.buildEditDictPanel()

    def setAppInfo(self):
        """
        Устанавливает информацию о приложении в главном окне.
        """
        app_info = self.app.getAppInfo()
        self.setWindowTitle(app_info["app_title"])
        self.labelCompany.setText(app_info["app_company"])
        self.labelVersion.setText(app_info["app_version"])
        self.labelAppTitle.setText(app_info["app_title"])
        self.labelInfoCompany.setText(app_info["app_company"])
        self.labelInfoVersion.setText(app_info["app_version"])

        authors = [author for author in app_info["author"]]
        model_1 = QtCore.QStringListModel(self)
        model_1.setStringList(authors)
        self.listViewAuthors.setModel(model_1)
        self.listViewAuthors.setSelectionMode(QtWidgets.QListView.SelectionMode.NoSelection)

    def setPlayParameters(self):
        """
        Устанавливает параметры воспроизведения приложения.
        """
        parameter = self.app.getAppPlayParameters()
        for i in range(len(self.app.MODE)):
            if parameter["mode"] == i:
                self.app.setMode(self.app.MODE(i))
                self.modeComboBox.setCurrentIndex(i)

    def buildSideMenu(self):
        """
        Создает панель бокового меню.
        """
        self.sideMenu = SideMenu(self)

    def buildPlayPanel(self):
        """
        Создает панель воспроизведения словаря.
        """
        self.playPanel = PlayPanel(self)

    def buildEditDictPanel(self):
        """
        Создает панель редактирования словаря.
        """
        self.editDictPanel = EditDictPanel(self)

    def setPlayPanel(self, playPanel):
        """
        Устанавливает панель воспроизведения словаря.

        Args:
            playPanel: Панель воспроизведения словаря.
        """
        if isinstance(playPanel, PlayPanel):
            self.playPanel = playPanel

    def getPlayPanel(self):
        """
        Получает панель воспроизведения словаря.

        Returns:
            PlayPanel: Панель воспроизведения словаря.
        """
        return self.playPanel

    def getEditDictPanel(self):
        """
        Получает панель редактирования словаря.

        Returns:
            EditDictPanel: Панель редактирования словаря.
        """
        return self.editDictPanel

    def getApplication(self):
        """
        Получает объект приложения.

        Returns:
            Application: Объект приложения.
        """
        return self.app

    def setSettings(self):
        """
        Устанавливает настройки приложения.
        """
        app_settings = self.app.getAppSettings()
        if app_settings["theme"] == "light":
            self.app.setTheme(self.app.THEME.LIGHT)
            self.themeComboBox.setCurrentIndex(0)
        elif app_settings["theme"] == "dark":
            self.app.setTheme(self.app.THEME.DARK)
            self.themeComboBox.setCurrentIndex(1)

    def load_icon(self):
        """
        Загружает иконки для элементов интерфейса из файлов.
        """
        icon_path = self.app.getIconFolder()
        QtCore.QDir.addSearchPath("icons", icon_path)

        menu_dict_icon = QtGui.QIcon("icons:cards_1.svg")
        self.dictsBtn.setIcon(menu_dict_icon)
        self.dictsBtn.setIconSize(QtCore.QSize(24, 24))

        menu_parameters_icon = QtGui.QIcon("icons:parameters.svg")
        self.parBtn.setIcon(menu_parameters_icon)
        self.parBtn.setIconSize(QtCore.QSize(24, 24))

        menu_settings_icon = QtGui.QIcon("icons:settings.svg")
        self.settingsBtn.setIcon(menu_settings_icon)
        self.settingsBtn.setIconSize(QtCore.QSize(24, 24))

        menu_info_icon = QtGui.QIcon("icons:info.svg")
        self.infoBtn.setIcon(menu_info_icon)
        self.infoBtn.setIconSize(QtCore.QSize(24, 24))

        menu_help_icon = QtGui.QIcon("icons:help.svg")
        self.helpBtn.setIcon(menu_help_icon)
        self.helpBtn.setIconSize(QtCore.QSize(24, 24))

        dict_open_icon = QtGui.QIcon("icons:apply_1.svg")
        self.openDictBtn.setIcon(dict_open_icon)
        self.openDictBtn.setIconSize(QtCore.QSize(24, 24))

        dict_add_icon = QtGui.QIcon("icons:add.svg")
        self.addDictBtn.setIcon(dict_add_icon)
        self.addDictBtn.setIconSize(QtCore.QSize(24, 24))

        dict_delete_icon = QtGui.QIcon("icons:delete_1.svg")
        self.deleteDictBtn.setIcon(dict_delete_icon)
        self.deleteDictBtn.setIconSize(QtCore.QSize(24, 24))

        dict_copy_icon = QtGui.QIcon("icons:copy.svg")
        self.copyDictBtn.setIcon(dict_copy_icon)
        self.copyDictBtn.setIconSize(QtCore.QSize(24, 24))

        dict_rename_icon = QtGui.QIcon("icons:edit_2.svg")
        self.renameDictBtn.setIcon(dict_rename_icon)
        self.renameDictBtn.setIconSize(QtCore.QSize(24, 24))

        dict_search_icon = QtGui.QIcon("icons:search.svg")
        self.searchDictBtn.setIcon(dict_search_icon)
        self.searchDictBtn.setIconSize(QtCore.QSize(24, 24))

        par_save_icon = QtGui.QIcon("icons:apply_1.svg")
        self.saveParBtn.setIcon(par_save_icon)
        self.saveParBtn.setIconSize(QtCore.QSize(24, 24))

        settings_save_icon = QtGui.QIcon("icons:apply_1.svg")
        self.saveSettingsBtn.setIcon(settings_save_icon)
        self.saveSettingsBtn.setIconSize(QtCore.QSize(24, 24))

        reload_icon = QtGui.QIcon("icons:reload_2.svg")
        self.reloadBtn.setIcon(reload_icon)
        self.reloadBtn.setIconSize(QtCore.QSize(24, 24))

        shuffle_icon = QtGui.QIcon("icons:shuffle.svg")
        self.shuffleBtn.setIcon(shuffle_icon)
        self.shuffleBtn.setIconSize(QtCore.QSize(24, 24))

        edit_icon = QtGui.QIcon("icons:edit.svg")
        self.editBtn.setIcon(edit_icon)
        self.editBtn.setIconSize(QtCore.QSize(24, 24))

        edit_add_icon = QtGui.QIcon("icons:add_card.svg")
        self.addEditBtn.setIcon(edit_add_icon)
        self.addEditBtn.setIconSize(QtCore.QSize(24, 24))

        edit_delete_icon = QtGui.QIcon("icons:delete_2.svg")
        self.deleteEditBtn.setIcon(edit_delete_icon)
        self.deleteEditBtn.setIconSize(QtCore.QSize(24, 24))

        edit_update_icon = QtGui.QIcon("icons:edit_2.svg")
        self.editEditBtn.setIcon(edit_update_icon)
        self.editEditBtn.setIconSize(QtCore.QSize(24, 24))

        edit_sort__icon = QtGui.QIcon("icons:sort.svg")
        self.sortEditBtn.setIcon(edit_sort__icon)
        self.sortEditBtn.setIconSize(QtCore.QSize(24, 24))

        dict_close__icon = QtGui.QIcon("icons:close.svg")
        self.closeBtn.setIcon(dict_close__icon)
        self.closeBtn.setIconSize(QtCore.QSize(24, 24))

        reverse__icon = QtGui.QIcon("icons:reverse_card.svg")
        self.answerViewModeBtn.setIcon(reverse__icon)
        self.answerViewModeBtn.setIconSize(QtCore.QSize(64, 64))

        back__icon = QtGui.QIcon("icons:back.svg")
        self.backViewModeBtn.setIcon(back__icon)
        self.backViewModeBtn.setIconSize(QtCore.QSize(64, 64))

        next__icon = QtGui.QIcon("icons:next.svg")
        self.nextViewModeBtn.setIcon(next__icon)
        self.nextViewModeBtn.setIconSize(QtCore.QSize(64, 64))

        self.nextAnswerModeBtn.setIcon(next__icon)
        self.nextAnswerModeBtn.setIconSize(QtCore.QSize(64, 64))

    def load_style(self, style_file):
        """
        Загружает стили интерфейса из файла.

        Args:
            style_file (str): Путь к файлу стилей.
        """
        f = open(style_file, 'r')
        styles = f.read()
        self.app.setStyleSheet(styles)
        f.close()

    def svg_change_color(self, color):
        """
        Меняет цвет SVG-иконок.

        Args:
            color (str): Цвет в формате RGB.
        """
        folder = self.app.getIconFolder()
        for file in os.listdir(folder):
            if os.path.isfile(os.path.join(folder, file)) and file.endswith('.svg'):
                with open(os.path.join(folder, file), 'r') as svg_icon:
                    svg_text = svg_icon.read()

                svg_text = re.sub(r'#[0-9A-Fa-f]{6}', color, svg_text)

                with open(os.path.join(folder, file), 'w') as svg_icon:
                    svg_icon.write(svg_text)

    def setUiTheme(self):
        """
        Устанавливает тему интерфейса приложения.
        """
        theme = self.app.getTheme()
        theme_files = self.app.getThemeFiles()
        if theme == self.app.THEME.LIGHT:
            self.svg_change_color("#314b5b")
            self.load_icon()
            self.load_style(theme_files["light"])
        elif theme == self.app.THEME.DARK:
            self.svg_change_color("#d5d5d5")
            self.load_icon()
            self.load_style(theme_files["dark"])
