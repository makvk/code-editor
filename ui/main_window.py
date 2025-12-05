from PyQt6.QtWidgets import QMainWindow, QFileDialog, QStatusBar, QSplitter
from PyQt6.QtCore import Qt
from .editor_widget import EditorWidget
from core.file_manager import FileManager
from core.executor import PythonRunner
from ui.output_widget import OutputWidget



class MainWindow(QMainWindow):
    # Конструктор главного окна, с установкой необходимых параметров
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Python Code Editor")
        self.resize(900, 600)

        self.editor = EditorWidget()
        self.setCentralWidget(self.editor)

        self.file_manager = FileManager(self.editor)

        self.output = OutputWidget()
        splitter = QSplitter(Qt.Orientation.Vertical)
        splitter.addWidget(self.editor)
        splitter.addWidget(self.output)
        splitter.setSizes([500, 200])  # верхняя и нижняя часть

        self.setCentralWidget(splitter)

        self.executor = PythonRunner()
        self.executor.outputReady.connect(self.output.append_stdout)
        self.executor.errorReady.connect(self.output.append_stderr)
        self.executor.finished.connect(self.on_finished)
        self.output.input.submitted.connect(self.executor.send_input)


        self._create_menu()
        self._create_status_bar()

    # Создание виджета меню
    def _create_menu(self):
        menu = self.menuBar()
        file_menu = menu.addMenu("Настройки")

        run_aciton = file_menu.addAction("Run")

        open_action = file_menu.addAction("Открыть")
        save_action = file_menu.addAction("Сохранить")
        save_as_action = file_menu.addAction("Сохранить как")

        #
        run_aciton.triggered.connect(self.run_code)

        #
        open_action.triggered.connect(self.file_manager.open_file)
        save_action.triggered.connect(self.file_manager.save_file)
        save_as_action.triggered.connect(self.file_manager.save_file_as)

    # Создание строки статуса
    def _create_status_bar(self):
        status = QStatusBar()
        self.setStatusBar(status)
        status.showMessage("Готово")

    def on_finished(self, code):
        self.output.append_stdout(f"\n[Process finished with code {code}]")

    def run_code(self):
        code = self.editor.toPlainText()
        self.output.clear_output()
        self.executor.run(code)