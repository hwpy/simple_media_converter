from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QLabel,
    QListWidget,
    QMessageBox,
    QPushButton,
    QSlider,
    QVBoxLayout,
    QWidget,
)

from model.settings import FileListSettings, SlidersSettings


class MainWindowElements:
    def __init__(self) -> None:
        self.file_list = QListWidget()
        self.file_list.setGeometry(
            FileListSettings.xpadd.value,
            FileListSettings.ypadd.value,
            FileListSettings.width.value,
            FileListSettings.height.value,
        )

        self.msg_converted = QMessageBox()

        self.main_label = QLabel("HEIC -> JPG")

        self.button_convert = QPushButton("Конвертировать")
        self.button_open = QPushButton("Открыть файл")

        self.slider_quality_label = QLabel(f"Качество: {SlidersSettings.slider_quality_dflt.value}", self)
        self.slider_quality = QSlider(Qt.Orientation.Horizontal, self)

        self.slider_subsampling_label = QLabel(f"Цветовая субдискретизация: {SlidersSettings.slider_quality_dflt.value}", self)
        self.slider_subsampling = QSlider(Qt.Orientation.Horizontal, self)

        self.layout = QVBoxLayout()
        self.container = QWidget()
        self.container.setLayout(self.layout)
