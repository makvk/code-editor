from PyQt6.QtWidgets import QWidget, QTextEdit, QVBoxLayout
from PyQt6.QtGui import QColor
from ui.input_widget import InputWidget


class OutputWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

        # окно вывода
        self.text = QTextEdit()
        self.text.setReadOnly(True)
        self.text.setStyleSheet("""
            background-color: #1e1e1e;
            color: #cccccc;
            font-family: Consolas;
            font-size: 14px;
        """)
        layout.addWidget(self.text)

        # окно ввода
        self.input = InputWidget()
        layout.addWidget(self.input)

    def append_stdout(self, text: str):
        self.text.setTextColor(QColor("#cccccc"))
        self.text.append(text)

    def append_stderr(self, text: str):
        self.text.setTextColor(QColor("#ff5555"))
        self.text.append(text)

    def clear_output(self):
        self.text.clear()
