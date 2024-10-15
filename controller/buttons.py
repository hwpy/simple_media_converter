from pathlib import Path

from PyQt6.QtWidgets import (
    QFileDialog,
    QMainWindow,
)

from .convert_img import HEIC_2_JPG


class AppButton:
    def __init__(self) -> None:
        pass

    def open_file_dialog(self, window: QMainWindow):
        dialog = QFileDialog(window)
        dialog.setDirectory(r"~/")
        dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        dialog.setNameFilter("Изображения (*.heic *.jpg);;Все (*)")
        dialog.setViewMode(QFileDialog.ViewMode.List)
        if dialog.exec():
            filenames = dialog.selectedFiles()
            if filenames:
                if window.file_list.count() > 0:
                    items = [
                        window.file_list.item(file).text()
                        for file in range(window.file_list.count())
                    ]
                    window.file_list.addItems(
                        [
                            str(Path(filename))
                            for filename in filenames
                            if filename not in items
                        ]
                    )
                else:
                    window.file_list.addItems(
                        [str(Path(filename)) for filename in filenames]
                    )

    def convert_img(self, window: QMainWindow):
        converted_files = []
        heic_2_jpg = HEIC_2_JPG()
        for file in range(window.file_list.count()):
            cur_file = window.file_list.item(file).text()
            heic_2_jpg.convert_file(
                cur_file,
                quality=window.slider_quality.value(),
                subsampling=window.slider_subsampling.value(),
            )
            converted_files.append(cur_file)
        window.msg_converted.setText(
            f"Конвертация {window.file_list.count()} файлов завершена"
        )
        _ = window.msg_converted.exec()
