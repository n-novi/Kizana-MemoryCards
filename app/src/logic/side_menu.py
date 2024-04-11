from PyQt6 import QtCore, QtWidgets
from app.src.logic.dicts_side_menu import DictsSideMenu
from app.src.logic.parameters_side_menu import ParametersSideMenu
from app.src.logic.settings_side_menu import SettingsSideMenu


class SideMenu:
    """
    Класс для управления боковым меню приложения.

    Args:
        main_win: Основное окно приложения.
    """

    def __init__(self, main_win):
        """
        Инициализация объекта класса SideMenu.

        Args:
            main_win: Основное окно приложения.
        """
        self.main_win = main_win

        self.dictSideMenu = None
        self.parametersSideMenu = None
        self.settingsSideMenu = None

        self.listMenuItem = []  # список всех элементов (кнопок) меню
        self.openSideMenuStatus = True  # боковое меню открыто/закрыто

        self.initSideMenu()
        self.fillListMenuItem()

        # слушатели кнопок
        self.main_win.dictsBtn.clicked.connect(lambda: self.menu_item(self.main_win.dictsBtn, 0))
        self.main_win.parBtn.clicked.connect(lambda: self.menu_item(self.main_win.parBtn, 1))
        self.main_win.settingsBtn.clicked.connect(lambda: self.menu_item(self.main_win.settingsBtn, 2))
        self.main_win.infoBtn.clicked.connect(lambda: self.menu_item(self.main_win.infoBtn, 3))
        self.main_win.helpBtn.clicked.connect(lambda: self.menu_item(self.main_win.helpBtn, 4))

    def initSideMenu(self):
        """
        Инициализация бокового меню.
        """
        if not self.openSideMenuStatus:
            self.main_win.frameSubMenu.setMaximumWidth(0)
            self.main_win.dictsBtn.setChecked(False)
        else:
            self.main_win.frameSubMenu.setMaximumWidth(270)
            self.main_win.dictsBtn.setChecked(True)
            self.main_win.stackedWidgetMenu.setCurrentIndex(0)
            self.dictSideMenu = DictsSideMenu(self.main_win)

    def fillListMenuItem(self):
        """
        Заполнение списка элементов (кнопок) меню.
        """
        self.listMenuItem.append(self.main_win.dictsBtn)
        self.listMenuItem.append(self.main_win.parBtn)
        self.listMenuItem.append(self.main_win.settingsBtn)
        self.listMenuItem.append(self.main_win.infoBtn)
        self.listMenuItem.append(self.main_win.helpBtn)

    def offMenuItems(self, itemOn):
        """
        Выключение всех элементов меню кроме одного.

        Args:
            itemOn: Элемент меню, который нужно оставить включенным.
        """
        for item in self.listMenuItem:
            if isinstance(item, QtWidgets.QPushButton):
                if item != itemOn:
                    item.setChecked(False)
                else:
                    item.setChecked(True)

    def actionMenuItem(self, button):
        """
        Выполнение действия для выбранного элемента меню.

        Args:
            button: Выбранный элемент меню.
        """
        if button == self.main_win.dictsBtn:
            self.dictSideMenu = DictsSideMenu(self.main_win)
        if button == self.main_win.parBtn:
            self.parametersSideMenu = ParametersSideMenu(self.main_win)
        if button == self.main_win.settingsBtn:
            self.settingsSideMenu = SettingsSideMenu(self.main_win)

    def menu_item(self, button, page):
        """
        Переключение пунктов меню.

        Args:
            button: Выбранный элемент меню.
            page: Номер страницы для переключения.
        """
        if not isinstance(button, QtWidgets.QPushButton):
            return

        if button.isChecked():
            self.main_win.stackedWidgetMenu.setCurrentIndex(page)
            self.actionMenuItem(button)
            self.offMenuItems(button)
            if not self.openSideMenuStatus:
                self.animationSideMenu()
        else:
            button.setChecked(True)
            if self.openSideMenuStatus:
                self.animationSideMenu()
                button.setChecked(False)

    def animationSideMenu(self):
        """
        Анимация открытия и закрытия бокового меню.
        """
        if not self.openSideMenuStatus:
            self.animation_1 = QtCore.QPropertyAnimation(self.main_win.frameSubMenu, b"maximumWidth")
            self.animation_1.setDuration(500)
            self.animation_1.setStartValue(0)
            self.animation_1.setEndValue(270)
            self.animation_1.setEasingCurve(QtCore.QEasingCurve.Type.InOutQuart)
            self.animation_1.start()

            self.openSideMenuStatus = True
        else:
            self.animation_1 = QtCore.QPropertyAnimation(self.main_win.frameSubMenu, b"maximumWidth")
            self.animation_1.setDuration(500)
            self.animation_1.setStartValue(self.main_win.frameSubMenu.width())
            self.animation_1.setEndValue(0)
            self.animation_1.setEasingCurve(QtCore.QEasingCurve.Type.InOutQuart)
            self.animation_1.start()

            self.openSideMenuStatus = False
