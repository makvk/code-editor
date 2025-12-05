from PyQt6.QtCore import QProcess, QObject, pyqtSignal

class PythonRunner(QObject):
    outputReady = pyqtSignal(str)
    errorReady = pyqtSignal(str)
    finished = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.process = QProcess()
        
        self.process.readyReadStandardOutput.connect(self._read_stdout)
        self.process.readyReadStandardError.connect(self._read_stderr)
        self.process.finished.connect(self._finished)

    def run(self, code: str):
        # Создаем временный файл
        import tempfile, os
        
        self.temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".py")
        self.temp_file.write(code.encode())
        self.temp_file.close()

        # Запускаем python temp.py
        self.process.start("python", [self.temp_file.name])
        self.process.setProcessChannelMode(QProcess.ProcessChannelMode.MergedChannels)


    def send_input(self, text: str):
        self.process.write((text + "\n").encode())

    
    def _read_stdout(self):
        text = self.process.readAllStandardOutput().data().decode()
        self.outputReady.emit(text)

    def _read_stderr(self):
        text = self.process.readAllStandardError().data().decode()
        self.errorReady.emit(text)

    def _finished(self, exit_code):
        self.finished.emit(exit_code)
