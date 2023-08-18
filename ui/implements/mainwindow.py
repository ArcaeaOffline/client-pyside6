from traceback import format_exception

from PySide6.QtWidgets import QMainWindow

from ui.designer.mainwindow_ui import Ui_MainWindow
from ui.implements.tabs.tabOcrEntry import TabOcrEntry

# try:
#     import arcaea_offline_ocr

#     from ui.implements.tabs.tabOcr import TabOcr

#     OCR_ENABLED_FLAG = True
# except Exception as e:
#     from ui.implements.tabs.tabOcrDisabled import TabOcrDisabled

#     OCR_ENABLED_FLAG = False
#     OCR_ERROR_TEXT = "\n".join(format_exception(e))


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        currentIndex = self.tabWidget.currentIndex()
        ocrTabIndex = self.tabWidget.indexOf(self.tab_ocr)
        self.tabWidget.removeTab(ocrTabIndex)
        self.tab_ocr.deleteLater()
        # if OCR_ENABLED_FLAG:
        #     self.tab_ocr = TabOcr(self.tabWidget)
        # else:
        #     self.tab_ocr = TabOcrDisabled(self.tabWidget)
        #     self.tab_ocr.contentLabel.setText(OCR_ERROR_TEXT)
        self.tab_ocr = TabOcrEntry(self.tabWidget)
        self.tabWidget.insertTab(ocrTabIndex, self.tab_ocr, "")
        self.tabWidget.setCurrentIndex(currentIndex)
        self.retranslateUi(self)
