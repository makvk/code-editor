from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLineEdit, QLabel
from PyQt6.QtCore import pyqtSignal


class InputWidget(QWidget):
    submitted = pyqtSignal(str)   # сигнал отправки текст в stdin процесса

    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()
        layout.setContentsMargins(4, 2, 4, 2)
        self.setLayout(layout)

        self.prompt = QLabel(">>>")
        layout.addWidget(self.prompt)

        self.edit = QLineEdit()
        layout.addWidget(self.edit)

        self.edit.returnPressed.connect(self._on_enter)

    def _on_enter(self):
        text = self.edit.text()
        self.edit.clear()
        self.submitted.emit(text)
