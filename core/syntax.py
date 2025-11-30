from PyQt6.QtGui import QSyntaxHighlighter, QColor, QTextCharFormat, QFont
import re

class PythonHighlighter(QSyntaxHighlighter):
    def __init__(self, document):
        super().__init__(document)
        self.rules = []
        self._init_formats()
        self._init_rules()        

    def _init_formats(self):
        # Установка формата для ключевых слов
        self.keyword_format = QTextCharFormat()
        self.keyword_format.setForeground(QColor("#DB8300"))

        # Установка формата встроенных функций
        self.func_format = QTextCharFormat()
        self.func_format.setForeground(QColor("#6D118C"))
        self.func_format.setFontWeight(QFont.Weight.Medium)

        # Установка формата для комментариев
        self.comment_format = QTextCharFormat()
        self.comment_format.setForeground(QColor("#B93A24"))

        # Установка формата для строк
        self.string_format = QTextCharFormat()
        self.string_format.setForeground(QColor("#56C516"))

        # Установка формата для чисел
        self.number_format = QTextCharFormat()
        self.number_format.setForeground(QColor("#4EC9B0"))

    # Добавление правил подсветки с помощью regex'ов и заготовленных форматов
    def _init_rules(self):
        KEYWORDS = [
            "False", "None", "True", "and", "as", "assert", "async", "await",
            "break", "class", "continue", "def", "del", "elif", "else", "except",
            "finally", "for", "from", "global", "if", "import", "in", "is",
            "lambda", "nonlocal", "not", "or", "pass", "raise", "return",
            "try", "while", "with", "yield"
        ]

        FUNCTIONS = [
            "abs", "all", "any", "ascii", "bin", "bool", "breakpoint", "bytearray",
            "bytes", "callable", "chr", "classmethod", "compile", "complex",
            "delattr", "dict", "dir", "divmod", "enumerate", "eval", "exec",
            "filter", "float", "format", "frozenset", "getattr", "globals",
            "hasattr", "hash", "help", "hex", "id", "input", "int", "isinstance",
            "issubclass", "iter", "len", "list", "locals", "map", "max", "memoryview",
            "min", "next", "object", "oct", "open", "ord", "pow", "print", "property",
            "range", "repr", "reversed", "round", "set", "setattr", "slice", "sorted",
            "staticmethod", "str", "sum", "super", "tuple", "type", "vars", "zip",
            "__import__"
        ]

        self.rules.append( 
            (rf"\b({'|'.join(KEYWORDS)})\b", self.keyword_format)
            )
        self.rules.append(
            (rf"\b({'|'.join(FUNCTIONS)})\b", self.func_format)
        )

        self.rules.append(
            (r"#.*$", self.comment_format)
        )

        self.rules.append((r'"[^"\\]*(\\.[^"\\]*)*"', self.string_format))

        self.rules.append((r"\b[0-9]+\b", self.number_format))
    
    # Абстрактный метод класса QSyntaxHighlighter для подсветки синтаксиса 
    def highlightBlock(self, text):
        for pattern, fmt in self.rules:
            for match in re.finditer(pattern, text):
                start = match.start()
                length = match.end() - match.start()
                self.setFormat(start, length, fmt)