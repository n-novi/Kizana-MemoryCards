from PyQt6 import QtWidgets
from app.src.ui.message_interface_ui import Ui_Dialog


class MessageWindow(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, msg):
        super().__init__()
        self.setupUi(self)
        self.msg_text.setText(msg)
