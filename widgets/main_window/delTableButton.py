import os, sys

from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import QSize

sys.path.append( os.path.dirname( __file__ ).replace("widgets\main_window", ""))
from widgets.func_get_path_icon import get_path_icon

class DelTableButton(QPushButton):
    def delTable(self):
        self.tableListWidget.del_table()

    def __init__(self, *args):
        super().__init__()
        self.tableListWidget = args[0]
        self.setFixedWidth(100)
        self.setText("DEL")
        self.setIcon(get_path_icon("file-minus.svg"))
        self.setIconSize(QSize(30,30))

        self.clicked.connect(self.delTable)
