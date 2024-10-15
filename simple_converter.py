import sys
from functools import partial

from PyQt6.QtWidgets import QApplication, QFormLayout, QMainWindow, QTabWidget

from controller.buttons import AppButton
from model.main_window import MainWindowSettings
from view.windows import MainWindowElements


class MainWindow(QMainWindow, MainWindowElements):
    def __init__(self):
        super().__init__()
        MainWindowSettings(self)

        app_buttons = AppButton()

        self.button_convert.clicked.connect(partial(app_buttons.convert_img, self))
        self.button_open.clicked.connect(partial(app_buttons.open_file_dialog, self))

        self.layout.addWidget(self.button_open)
        self.layout.addWidget(self.file_list)
        self.layout.addWidget(self.button_convert)

        # Устанавливаем центральный виджет Window.
        self.setCentralWidget(self.container)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
