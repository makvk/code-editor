from PyQt6.QtWidgets import QMainWindow, QFileDialog, QStatusBar
from .editor_widget import EditorWidget
from core.file_manager import FileManager


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Python Code Editor")
        self.resize(900, 600)

        self.editor = EditorWidget()
        self.setCentralWidget(self.editor)

        self.file_manager = FileManager(self.editor)

        self._create_menu()
        self._create_status_bar()

    def _create_menu(self):
        menu = self.menuBar()

        file_menu = menu.addMenu("Файл")
        settings_menu = menu.addMenu("Настройки")

        open_action = file_menu.addAction("Открыть")
        save_action = file_menu.addAction("Сохранить")
        save_as_action = file_menu.addAction("Сохранить как")

        set_size = settings_menu.addAction("Изменить разрешение")

        open_action.triggered.connect(self.file_manager.open_file)
        save_action.triggered.connect(self.file_manager.save_file)
        save_as_action.triggered.connect(self.file_manager.save_file_as)

    def _create_status_bar(self):
        status = QStatusBar()
        self.setStatusBar(status)
        status.showMessage("Готово")
