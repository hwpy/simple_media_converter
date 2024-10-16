from functools import partial

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QMainWindow,
)

from controller.buttons import AppButton
from controller.sliders import AppSlider
from model.settings import MainWindowSettings, SlidersSettings
from view.window_elements import MainWindowElements


class MainWindow(QMainWindow, MainWindowElements):
    def __init__(self):
        super().__init__()
        settings = MainWindowSettings(self)

        self.main_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Действия
        app_buttons = AppButton()
        app_sliders = AppSlider()

        # Слайдеры
        self.slider_quality = settings.setup_slider(
            self.slider_quality, SlidersSettings.slider_quality_dflt.value
        )
        self.slider_quality.valueChanged.connect(
            partial(app_sliders.update_quality, self)
        )

        self.slider_subsampling = settings.setup_slider(
            self.slider_subsampling, SlidersSettings.slider_subsampling_dflt.value
        )
        self.slider_subsampling.valueChanged.connect(
            partial(app_sliders.update_subsampling, self)
        )

        # Обработка нажатий кнопок
        self.button_convert.clicked.connect(partial(app_buttons.convert_img, self))
        self.button_open.clicked.connect(partial(app_buttons.open_file_dialog, self))

        # Добавление на лейаут
        self.layout.addWidget(self.main_label)

        self.layout.addWidget(self.button_open)

        self.layout.addWidget(self.slider_quality_label)
        self.layout.addWidget(self.slider_quality)
        self.layout.addWidget(self.slider_subsampling_label)
        self.layout.addWidget(self.slider_subsampling)

        self.layout.addWidget(self.file_list)
        self.layout.addWidget(self.button_convert)

        # Устанавливаем центральный виджет Window.
        self.setCentralWidget(self.container)
