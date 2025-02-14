import os, shutil
from PyQt6 import QtCore, QtWidgets
from app.src.logic.play_panel import PlayPanel
from app.src.logic.controller.Controller import Controller
from app.src.logic.message_window import MessageWindow

class DictsSideMenu:
    """
    Класс для управления боковым меню со списком словарей.

    Args:
        main_win: Основное окно приложения.

    Attributes:
        main_win: Основное окно приложения.
        selectedDict: Имя выбранного словаря.
        dicts: Список имен файлов словарей.
        dicts_folder_path: Путь к папке с файлами словарей.
    """

    def __init__(self, main_win):
        """
        Инициализация объекта класса DictsSideMenu.

        Args:
            main_win: Основное окно приложения.
        """
        self.main_win = main_win
        self.selectedDict = None
        self.dicts = None
        self.dicts_folder_path = self.main_win.getApplication().getDictsFolder()

        self.updateListDicts()

        # Слушатели кнопок
        self.main_win.listDicts.itemClicked.connect(self.selectDict)
        self.main_win.addDictBtn.clicked.connect(self.createDict)
        self.main_win.deleteDictBtn.clicked.connect(self.deleteDict)
        self.main_win.renameDictBtn.clicked.connect(self.renameDict)
        self.main_win.copyDictBtn.clicked.connect(self.copyDict)
        self.main_win.openDictBtn.clicked.connect(self.openDict)
        self.main_win.listDicts.itemDoubleClicked.connect(self.openDict)
        self.main_win.searchDictBtn.clicked.connect(self.searchDict)

    def updateListDicts(self):
        """
        Обновляет список словарей в боковом меню.
        """
        self.dicts = self.getDicts()
        self.setDictsList()

    def getDicts(self):
        """
        Получает список словарей из папки.

        Returns:
            list: Список имен файлов словарей.
        """
        result = []
        content = os.listdir(self.dicts_folder_path)
        for file in content:
            if os.path.isfile(os.path.join(self.dicts_folder_path, file)) and file.endswith('.db'):
                result.append(file)
        return result

    def addElement(self, text):
        """
        Добавляет элемент в список словарей.

        Args:
            text (str): Текст элемента.
        """
        item = QtWidgets.QListWidgetItem()
        item.setText(text)
        self.main_win.listDicts.addItem(item)

    def setDictsList(self):
        """
        Устанавливает список словарей в боковом меню.
        """
        self.main_win.listDicts.clear()
        for d in self.dicts:
            file = str(d)
            self.addElement(file[:len(file) - 3])

    def selectDict(self, item):
        """
        Выбирает словарь из списка.

        Args:
            item (QtWidgets.QListWidgetItem): Элемент списка словарей.
        """
        self.selectedDict = item.text()

    def dict_name_uniq(self, name):
        """
        Генерирует уникальное имя для нового словаря.

        Args:
            name (str): Имя словаря.

        Returns:
            str: Уникальное имя словаря.
        """
        found = self.main_win.listDicts.findItems(name, QtCore.Qt.MatchFlag.MatchExactly)
        if len(found) > 0:
            return self.name_selection(name, name)
        else:
            return name

    def name_selection(self, name, new_name, counter=0):
        """
        Генерирует уникальное имя для словаря с учетом уже существующих имен.

        Args:
            name (str): Имя словаря.
            new_name (str): Новое имя словаря.
            counter (int, optional): Счетчик для генерации нового имени. По умолчанию 0.

        Returns:
            str: Уникальное имя словаря.
        """
        found = self.main_win.listDicts.findItems(new_name, QtCore.Qt.MatchFlag.MatchExactly)
        if len(found) == 0:
            return new_name
        else:
            counter += 1
            new_name = f"{name} ({counter})"
            return self.name_selection(name, new_name, counter)

    def createDict(self):
        """
        Создает новый словарь.
        """
        name = self.main_win.dictEdit.text()
        if self.validation(name):
            name = self.dict_name_uniq(name)
            try:
                f = open(self.dicts_folder_path + name + '.db', 'w')
                f.close()
            except IOError as e:
                print("Не удалось создать словарь")
                dialog = MessageWindow("Не удалось создать словарь")
                dialog.setWindowTitle('Ошибка')
                result = dialog.exec()

            self.updateListDicts()
            self.main_win.dictEdit.clear()
            self.main_win.getPlayPanel().openPage()

    def deleteDict(self):
        """
        Удаляет выбранный словарь.
        """
        if self.selectedDict is not None:
            try:
                os.remove(self.dicts_folder_path + self.selectedDict + '.db')
            except OSError as e:
                print("Не удалось удалить словарь")
                dialog = MessageWindow("Не удалось удалить словарь")
                dialog.setWindowTitle('Ошибка')
                result = dialog.exec()

            self.updateListDicts()
            self.main_win.dictEdit.clear()
            self.main_win.getPlayPanel().openPage()

    def renameDict(self):
        """
        Переименовывает выбранный словарь.
        """
        if self.selectedDict is not None:
            new_name = self.main_win.dictEdit.text()
            if self.validation(new_name):
                file = self.dicts_folder_path + self.selectedDict + '.db'
                new_file = self.dicts_folder_path + new_name + '.db'

                try:
                    os.rename(file, new_file)
                except OSError as e:
                    print("Не удалось переименовать словарь")
                    dialog = MessageWindow("Не удалось переименовать словарь")
                    dialog.setWindowTitle('Ошибка')
                    result = dialog.exec()

                self.updateListDicts()
                self.main_win.dictEdit.clear()

    def copyDict(self):
        """
        Копирует выбранный словарь.
        """
        if self.selectedDict is not None:
            folder = self.main_win.getApplication().getDictsFolder()
            try:
                shutil.copy2(folder + self.selectedDict + '.db', folder + self.selectedDict + '_copy.db')
            except IOError as e:
                print("Не удалось скопировать файл")
                dialog = MessageWindow("Не удалось скопировать файл")
                dialog.setWindowTitle('Ошибка')
                result = dialog.exec()

            self.updateListDicts()

    def openDict(self):
        """
        Открывает выбранный словарь для игры.
        """
        if self.selectedDict is not None:
            self.main_win.getApplication().setPlaySession(True)
            self.main_win.getApplication().setController(
                Controller(self.main_win.getApplication().getDictsFolder() + self.selectedDict + '.db'))
            self.main_win.getPlayPanel().openPage()

    def searchDict(self):
        """
        Ищет словарь в списке по введенному запросу.
        """
        search_string = self.main_win.dictEdit.text()
        if len(search_string) > 0:
            found = self.main_win.listDicts.findItems(search_string, QtCore.Qt.MatchFlag.MatchContains)

            for item in found:
                if search_string:
                    row = self.main_win.listDicts.row(item)
                    el = self.main_win.listDicts.takeItem(row)
                    self.main_win.listDicts.insertItem(0, el)

            self.main_win.listDicts.item(0).setSelected(True)
            self.selectDict(self.main_win.listDicts.item(0))

    def validation(self, src_string):
        """
        Проверяет строку на наличие содержимого.

        Args:
            src_string (str): Входная строка для проверки.

        Returns:
            bool: True, если строка не пустая, иначе False.
        """
        if len(src_string) > 0:
            return True
        else:
            return False
