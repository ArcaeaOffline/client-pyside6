import base64
import logging
import os
import re

from PySide6.QtCore import QObject, QProcess, QRunnable, QThreadPool, Signal

logger = logging.getLogger(__name__)


class AndrealExecuteRunnableSignals(QObject):
    error = Signal(str, str)
    completed = Signal(str, bytes)
    finished = Signal()


class AndrealExecuteRunnable(QRunnable):
    def __init__(self, executePath, jsonPath, arguments):
        super().__init__()
        self.signals = AndrealExecuteRunnableSignals()
        self.executePath = executePath
        self.jsonPath = jsonPath
        self.arguments = arguments

    def run(self):
        try:
            result = os.popen(f"{self.executePath} {' '.join(self.arguments)}").read()
            b64Result = [s for s in result.split("\n") if s]
            imageBytes = base64.b64decode(
                re.sub(r"data:image/.*;base64,", "", b64Result[-1])
            )
            self.signals.completed.emit(self.jsonPath, imageBytes)
        except Exception as e:
            imageBytes = None
            logger.exception(f"{self.__class__.__name__} error")
            self.signals.error.emit(self.jsonPath, str(e))
        finally:
            os.unlink(self.jsonPath)
            self.signals.finished.emit()


class AndrealHelper(QObject):
    error = Signal(str, str)
    ready = Signal(str, bytes)
    finished = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.andrealFolder = None
        self.__andrealExecutable = None

        self.andrealTestProcess = QProcess(self)
        self.__andrealTestResult: bool = False

    @property
    def andrealExecutable(self):
        return self.__andrealExecutable

    @andrealExecutable.setter
    def andrealExecutable(self, value: str):
        self.__andrealExecutable = value
        self.andrealTestProcess.start(self.__andrealExecutable, ["--help"])
        self.andrealTestProcess.waitForFinished()
        result = bytes(self.andrealTestProcess.readAll()).decode("utf-8")
        self.__andrealTestResult = "Andreal" in result and "--json-file" in result

    @property
    def andrealTestResult(self):
        return self.__andrealTestResult

    def andrealOutputToImage(self, output: str):
        b64result = output.split("\n")[-1]
        return base64.b64decode(b64result)

    def request(self, jsonPath: str, arguments: list[str]):
        runnable = AndrealExecuteRunnable(self.andrealExecutable, jsonPath, arguments)
        runnable.signals.error.connect(self.error)
        runnable.signals.completed.connect(self.ready)
        runnable.signals.finished.connect(self.finished)
        QThreadPool.globalInstance().start(runnable)
