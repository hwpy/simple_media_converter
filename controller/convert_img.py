import os

import pillow_heif
from PIL import Image


class HEIC_2_JPG:
    def __init__(self) -> None:
        pass

    def convert_file(
        self, heic_path: str, jpeg_path: str | None = None, **kwargs
    ) -> str:
        # Зарегистрировать Pillow для формата HEIF
        pillow_heif.register_heif_opener()

        # Сформировать имя файла
        if not jpeg_path:
            heic_dir_and_file = os.path.split(heic_path)
            jpg_dir = os.path.join(heic_dir_and_file[0], "jpg")
            jpeg_path = os.path.join(
                jpg_dir, heic_dir_and_file[1].lower().replace(".heic", ".jpg")
            )

            # Создать директорию для сохранения, если она не существует
            if not os.path.exists(jpg_dir):
                os.makedirs(jpg_dir)

        img = Image.open(heic_path)
        img.save(jpeg_path, format="JPEG", **kwargs)
        return jpeg_path


if __name__ == "__main__":
    input_folder = "heif"
    output_folder = "jpg"
    heic_2_jpg = HEIC_2_JPG()
    heic_2_jpg.convert_from_dir(input_folder, output_folder)
