from pathlib import Path

from config import OUTPUT_FOLDER


class FileHandler:

    @staticmethod
    def create_output_folder():
        OUTPUT_FOLDER.mkdir(exist_ok=True)

    @staticmethod
    def save_text(filename: str, content: str):
        FileHandler.create_output_folder()

        file_path = OUTPUT_FOLDER / filename

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)

        return file_path