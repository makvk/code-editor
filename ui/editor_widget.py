from PyQt6.QtWidgets import QPlainTextEdit
from PyQt6.QtGui import QFont
from core.syntax import PythonHighlighter

class EditorWidget(QPlainTextEdit):
    def __init__(self):
        super().__init__()

        # Настройки редактора
        self.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap)
        self.setFont(QFont('Courier New', 14))
        self.setTabStopDistance(4 * self.fontMetrics().horizontalAdvance(' '))
        # Подсветка синтаксиса
        self.highlighter = PythonHighlighter(self.document())