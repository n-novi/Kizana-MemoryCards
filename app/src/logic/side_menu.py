from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import QPropertyAnimation, QEasingCurve, QAbstractAnimation
from PyQt6.QtWidgets import QPushButton, QWidget

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
        self.__mw_view = main_win  # представление главного окна, в котором расположены элементы панели

        # max_width >= start_width >= min_width > closed_width >= 0
        self.__max_width = 480  # максимальная ширина панели
        self.__start_width = 250  # начальная ширина панели
        self.__min_width = 250  # минимальная ширина панели
        self.__closed_width = 0  # ширина панели при закрытии
        self.__previous_width = self.__start_width  # предыдущая ширина панели

        self.__animation = None  # QPropertyAnimation
        self.__open_animation_duration = 400  # продолжительность анимации

        self.dictSideMenu = DictsSideMenu(self.__mw_view)
        self.parametersSideMenu = ParametersSideMenu(self.__mw_view)
        self.settingsSideMenu = SettingsSideMenu(self.__mw_view)

        # соответствие кнопок меню и страниц панели
        self.__button_to_page_mapping = {self.__mw_view.dictsBtn: self.__mw_view.dictsPage,
                                         self.__mw_view.parBtn: self.__mw_view.parPage,
                                         self.__mw_view.infoBtn: self.__mw_view.infoPage,
                                         self.__mw_view.settingsBtn: self.__mw_view.settingsPage,
                                         self.__mw_view.helpBtn: self.__mw_view.helpPage}

        self.__cur_button = self.__mw_view.dictsBtn
        self.__is_opened = True  # панель открыта \ закрыта
        self.__initState(self.__cur_button)
        self.__initButtonsSignals()
        self.__mw_view.splitter.splitterMoved.connect(self.__changePanelBySplitter)

    # Логика закрытия \ открытия панели заключается в установлении максимальной ширины панели
    def __initState(self, active_button: QPushButton):  # установка стартового состояния панели
        self.__mw_view.stackedWidgetMenu.setCurrentWidget(
            self.__button_to_page_mapping[active_button])  # установка стартовой страницы
        self.__mw_view.frameSubMenu.setMaximumWidth(self.__max_width if self.__is_opened else self.__closed_width)
        self.__mw_view.frameSubMenu.setMinimumWidth(self.__start_width if self.__is_opened else self.__closed_width)

        self.__mw_view.splitter.setCollapsible(0, True)  # левая область сплиттера может закрываться
        self.__mw_view.splitter.setCollapsible(1, False)  # правая область сплиттера не может закрываться
        self.__mw_view.splitter.setCollapsible(2, True)  # правая область сплиттера не может закрываться
        self.__mw_view.splitter.setSizes([self.__start_width if self.__is_opened else self.__closed_width])

        active_button.setChecked(self.__is_opened)

    def __initButtonsSignals(self):  # установка сигналов кнопок меню
        for button, page in self.__button_to_page_mapping.items():
            button.clicked.connect(self.__createHandler(button, page))

    def __createHandler(self, button, page):
        return lambda: self.__changePanelByButtons(button, page)

    def __changePanelByButtons(self, button: QPushButton, page: QWidget):  # смена страниц при нажатии кнопок
        if self.__animation is not None and self.__animation.state() == QAbstractAnimation.State.Running:  # кнопки не активны пока идет анимация
            for button in self.__button_to_page_mapping.keys():
                button.setChecked((button == self.__cur_button) * self.__is_opened)
            return

        print(type(button))
        print(button)
        print(self.__button_to_page_mapping)

        if button.isChecked():
            self.__mw_view.stackedWidgetMenu.setCurrentWidget(page)
            self.__cur_button.setChecked(False)
            self.__cur_button = button
            self.__cur_button.setChecked(True)
            if not self.__is_opened:  # открыть панель
                self.__changeWidthByButton()

        elif self.__is_opened:  # закрыть панель
            self.__previous_width = self.__mw_view.frameSubMenu.width()  # сохранение щирины панели
            self.__changeWidthByButton()

    def __changePanelBySplitter(self, pos):  # изменение ширины панели через сплиттер
        self.__mw_view.frameSubMenu.setMaximumWidth(self.__max_width)
        self.__mw_view.frameSubMenu.setMinimumWidth(self.__min_width)

        if pos == self.__closed_width and self.__is_opened:
            self.__is_opened = False
            self.__cur_button.setChecked(False)

        elif pos > self.__closed_width + 1 and not self.__is_opened:
            self.__is_opened = True
            self.__cur_button.setChecked(True)

    def __toggleMenuButtons(self, checked_button: QPushButton):  # отключение кнопок
        for button in self.__button_to_page_mapping.keys():
            button.setChecked(button == checked_button)

    def __changeWidthByButton(self):  # изменение ширины панели через кнопки
        start_value = self.__mw_view.frameSubMenu.width() if self.__is_opened else self.__closed_width
        end_value = self.__closed_width if self.__is_opened else self.__previous_width

        self.__mw_view.frameSubMenu.setMinimumWidth(self.__closed_width)

        self.__animation = QPropertyAnimation(self.__mw_view.frameSubMenu, b"maximumWidth")
        self.__animation.setDuration(self.__open_animation_duration)
        self.__animation.setStartValue(start_value)
        self.__animation.setEndValue(end_value)
        self.__animation.setEasingCurve(QEasingCurve.Type.InOutCubic)
        self.__animation.valueChanged.connect(self.__onValueChanged)
        self.__animation.finished.connect(self.__restoreMinimumWidth)
        self.__animation.start()

        self.__is_opened = not self.__is_opened

    def __onValueChanged(self, value):  # при изменении значений анимации (ширины панели)
        self.__mw_view.splitter.setSizes([value])

    def __restoreMinimumWidth(self):  # Восстановление минимальной ширины
        if self.__is_opened:
            self.__mw_view.frameSubMenu.setMinimumWidth(self.__min_width)
