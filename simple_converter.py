import sys
from functools import partial

from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
)

from controller.buttons import AppButton
from controller.sliders import AppSlider
from model.main_window import MainWindowSettings
from view.windows import MainWindowElements


class MainWindow(QMainWindow, MainWindowElements):
    def __init__(self):
        super().__init__()
        settings = MainWindowSettings(self)

        # Действия
        app_buttons = AppButton()
        app_sliders = AppSlider()

        # Слайдеры
        self.slider_quality_label = QLabel("Качество: ", self)
        self.slider_quality = settings.setup_slider(self.slider_quality, 100)
        self.slider_quality.valueChanged.connect(partial(app_sliders.update_quality, self))

        self.slider_subsampling_label = QLabel("Цветовая субдискретизация: ", self)
        self.slider_subsampling = settings.setup_slider(self.slider_subsampling, 0)
        self.slider_subsampling.valueChanged.connect(partial(app_sliders.update_subsampling, self))

        # Обработка нажатий кнопок
        self.button_convert.clicked.connect(partial(app_buttons.convert_img, self))
        self.button_open.clicked.connect(partial(app_buttons.open_file_dialog, self))

        # Добавление на лейаут
        self.layout.addWidget(self.button_open)

        self.layout.addWidget(self.slider_quality_label)
        self.layout.addWidget(self.slider_quality)
        self.layout.addWidget(self.slider_subsampling_label)
        self.layout.addWidget(self.slider_subsampling)

        self.layout.addWidget(self.file_list)
        self.layout.addWidget(self.button_convert)

        # Устанавливаем центральный виджет Window.
        self.setCentralWidget(self.container)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
