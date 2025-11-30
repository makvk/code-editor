from PyQt6.QtWidgets import QFileDialog
import os

class FileManager:
    # Конструктор с инициализацией двух полей
    def __init__(self, editor):
        self.editor = editor
        self.current_path = None

    # Логика открытия файла
    def open_file(self):
        path, _ = QFileDialog.getOpenFileName(
            None, 
            "Открыть файл",
            "", 
            "Python Files (*.py);;All Files (*)"
        )
        if not path:
            return

        with open(path, "r", encoding="utf-8") as f:
            self.editor.setPlainText(f.read())

        self.current_path = path

    # Логика сохранения файла
    def save_file(self):
        if self.current_path is None:
            return self.save_file_as()

        with open(self.current_path, "w", encoding="utf-8") as f:
            f.write(self.editor.toPlainText())

    # Логика сохранения файла по указанному пути
    def save_file_as(self):
        path, _ = QFileDialog.getSaveFileName(
            None,
            "Сохранить файл как",
            "",
            "Python Files (*.py);;All Files (*)"
        )
        if not path:
            return

        with open(path, "w", encoding="utf-8") as f:
            f.write(self.editor.toPlainText())

        self.current_path = path
