from PyQt6.QtWidgets import (
    QMainWindow,
)


class AppSlider:
    def __init__(self) -> None:
        pass

    def update_quality(self, window: QMainWindow, value: int):
        window.slider_quality_label.setText(f"Качество: {value}")

    def update_subsampling(self, window: QMainWindow, value: int):
        window.slider_subsampling_label.setText(f"Цветовая субдискретизация: {value}")
