from enum import Enum

from PyQt6 import QtGui
from PyQt6.QtWidgets import (
    QMainWindow,
)


class MainWindowSettings:
    def __init__(self, window: QMainWindow) -> None:
        super().__init__()
        # Размеры окна
        self.width = 400
        self.height = 600
        self.xpadd = 80
        self.ypadd = 80

        # Заголовок
        window.setWindowTitle("Простой конвертер")
        # Иконка
        window.setWindowIcon(QtGui.QIcon("media/app_icon.png"))
        # Установка позиции и размеров окна
        window.setGeometry(self.xpadd, self.ypadd, self.width, self.height)

class FileListSettings(Enum):
    width: int = 400
    height: int = 20
    xpadd: int = 20
    ypadd: int = 20
