from enum import Enum

from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QSlider


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

    @staticmethod
    def setup_slider(slider: QSlider, default_value: int = 100):
        slider.setRange(0, 100)
        slider.setValue(default_value)
        slider.setSingleStep(5)
        slider.setPageStep(10)
        slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        return slider


class FileListSettings(Enum):
    width: int = 400
    height: int = 20
    xpadd: int = 20
    ypadd: int = 20


class SlidersSettings(Enum):
    slider_quality_dflt: int = 100
    slider_subsampling_dflt: int = 0
