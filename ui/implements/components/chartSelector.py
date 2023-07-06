from typing import Literal

from arcaea_offline.database import Database
from arcaea_offline.models import Chart, Package
from arcaea_offline.utils import rating_class_to_text
from PySide6.QtCore import QModelIndex, Qt, Signal, Slot
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QCompleter, QWidget

from ui.designer.components.chartSelector_ui import Ui_ChartSelector
from ui.extends.components.chartSelector import FuzzySearchCompleterModel
from ui.extends.shared.delegates.descriptionDelegate import DescriptionDelegate
from ui.implements.components.ratingClassRadioButton import RatingClassRadioButton


class ChartSelector(Ui_ChartSelector, QWidget):
    valueChanged = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.db = Database()
        self.db.register_update_hook(self.fillPackageComboBox)
        self.setupUi(self)

        self.pstButton.setColors(QColor("#399bb2"), QColor("#f0f8fa"))
        self.prsButton.setColors(QColor("#809955"), QColor("#f7f9f4"))
        self.ftrButton.setColors(QColor("#702d60"), QColor("#f7ebf4"))
        self.bydButton.setColors(QColor("#710f25"), QColor("#f9ced8"))
        self.__RATING_CLASS_BUTTONS = [
            self.pstButton,
            self.prsButton,
            self.ftrButton,
            self.bydButton,
        ]
        self.pstButton.clicked.connect(self.selectRatingClass)
        self.prsButton.clicked.connect(self.selectRatingClass)
        self.ftrButton.clicked.connect(self.selectRatingClass)
        self.bydButton.clicked.connect(self.selectRatingClass)
        self.deselectAllRatingClassButtons()
        self.updateRatingClassButtonsEnabled([])

        self.previousPackageButton.clicked.connect(
            lambda: self.quickSwitchSelection("previous", "package")
        )
        self.previousSongIdButton.clicked.connect(
            lambda: self.quickSwitchSelection("previous", "songId")
        )
        self.nextSongIdButton.clicked.connect(
            lambda: self.quickSwitchSelection("next", "songId")
        )
        self.nextPackageButton.clicked.connect(
            lambda: self.quickSwitchSelection("next", "package")
        )

        self.valueChanged.connect(self.updateResultLabel)

        self.fillPackageComboBox()
        self.packageComboBox.setCurrentIndex(-1)
        self.songIdComboBox.setCurrentIndex(-1)

        self.fuzzySearchCompleterModel = FuzzySearchCompleterModel()
        self.fuzzySearchCompleter = QCompleter(self.fuzzySearchCompleterModel)
        self.fuzzySearchCompleter.popup().setItemDelegate(
            DescriptionDelegate(self.fuzzySearchCompleter.popup())
        )
        self.fuzzySearchCompleter.activated[QModelIndex].connect(
            self.fuzzySearchCompleterSetSelection
        )
        self.fuzzySearchLineEdit.setCompleter(self.fuzzySearchCompleter)

        self.packageComboBox.setItemDelegate(DescriptionDelegate(self.packageComboBox))
        self.songIdComboBox.setItemDelegate(DescriptionDelegate(self.songIdComboBox))

        self.pstButton.toggled.connect(self.valueChanged)
        self.prsButton.toggled.connect(self.valueChanged)
        self.ftrButton.toggled.connect(self.valueChanged)
        self.bydButton.toggled.connect(self.valueChanged)
        self.packageComboBox.currentIndexChanged.connect(self.valueChanged)
        self.songIdComboBox.currentIndexChanged.connect(self.valueChanged)

    def quickSwitchSelection(
        self,
        direction: Literal["previous", "next"],
        model: Literal["package", "songId"],
    ):
        minIndex = 0
        if model == "package":
            maxIndex = self.packageComboBox.count() - 1
            currentIndex = self.packageComboBox.currentIndex() + (
                1 if direction == "next" else -1
            )
            currentIndex = max(min(maxIndex, currentIndex), minIndex)
            self.packageComboBox.setCurrentIndex(currentIndex)
        elif model == "songId":
            maxIndex = self.songIdComboBox.count() - 1
            currentIndex = self.songIdComboBox.currentIndex() + (
                1 if direction == "next" else -1
            )
            currentIndex = max(min(maxIndex, currentIndex), minIndex)
            self.songIdComboBox.setCurrentIndex(currentIndex)
        else:
            return

    def value(self):
        packageId = self.packageComboBox.currentData()
        songId = self.songIdComboBox.currentData()
        ratingClass = self.selectedRatingClass()

        if packageId and songId and isinstance(ratingClass, int):
            return Chart.from_db_row(self.db.get_chart(songId, ratingClass))
        return None

    @Slot()
    def updateResultLabel(self):
        chart = self.value()
        if isinstance(chart, Chart):
            package = Package.from_db_row(
                self.db.get_package_by_package_id(chart.package_id)
            )
            texts = [
                [package.name, chart.name_en, rating_class_to_text(chart.rating_class)],
                [package.id, chart.song_id, str(chart.rating_class)],
            ]
            texts = [" | ".join(t) for t in texts]
            text = f'{texts[0]}<br><font color="gray">{texts[1]}</font>'
            self.resultLabel.setText(text)
        else:
            self.resultLabel.setText("...")

    def fillPackageComboBox(self):
        self.packageComboBox.clear()
        packages = [Package.from_db_row(dbRow) for dbRow in self.db.get_packages()]
        for package in packages:
            self.packageComboBox.addItem(f"{package.name} ({package.id})", package.id)
            row = self.packageComboBox.count() - 1
            self.packageComboBox.setItemData(
                row, package.name, DescriptionDelegate.MainTextRole
            )
            self.packageComboBox.setItemData(
                row, package.id, DescriptionDelegate.DescriptionTextRole
            )

        self.packageComboBox.setCurrentIndex(-1)

    def fillSongIdComboBox(self):
        self.songIdComboBox.clear()
        packageId = self.packageComboBox.currentData()
        if packageId:
            charts = [
                Chart.from_db_row(dbRow)
                for dbRow in self.db.get_charts_by_package_id(packageId)
            ]
            inserted_song_ids = []
            for chart in charts:
                if chart.song_id not in inserted_song_ids:
                    self.songIdComboBox.addItem(
                        f"{chart.name_en} ({chart.song_id})", chart.song_id
                    )
                    inserted_song_ids.append(chart.song_id)
                    row = self.songIdComboBox.count() - 1
                    self.songIdComboBox.setItemData(
                        row, chart.name_en, DescriptionDelegate.MainTextRole
                    )
                    self.songIdComboBox.setItemData(
                        row, chart.song_id, DescriptionDelegate.DescriptionTextRole
                    )
        self.songIdComboBox.setCurrentIndex(-1)

    @Slot()
    def on_packageComboBox_activated(self):
        self.fillSongIdComboBox()

    @Slot(int)
    def on_songIdComboBox_currentIndexChanged(self, index: int):
        rating_classes = []
        if index > -1:
            charts = [
                Chart.from_db_row(dbRow)
                for dbRow in self.db.get_charts_by_song_id(
                    self.songIdComboBox.currentData()
                )
            ]
            rating_classes = [chart.rating_class for chart in charts]
        self.updateRatingClassButtonsEnabled(rating_classes)

    @Slot()
    def on_resetButton_clicked(self):
        self.packageComboBox.setCurrentIndex(-1)
        self.songIdComboBox.setCurrentIndex(-1)

    @Slot(str)
    def on_fuzzySearchLineEdit_textChanged(self, text: str):
        if text:
            self.fuzzySearchCompleterModel.fillDbFuzzySearchResults(self.db, text)
        else:
            self.fuzzySearchCompleterModel.clear()

    def selectChart(self, chart: Chart):
        packageIdIndex = self.packageComboBox.findData(chart.package_id)
        if packageIdIndex > -1:
            self.packageComboBox.setCurrentIndex(packageIdIndex)
        else:
            # QMessageBox
            return

        self.fillSongIdComboBox()
        songIdIndex = self.songIdComboBox.findData(chart.song_id)
        if songIdIndex > -1:
            self.songIdComboBox.setCurrentIndex(songIdIndex)
        else:
            # QMessageBox
            return

        self.selectRatingClass(chart.rating_class)

    @Slot(QModelIndex)
    def fuzzySearchCompleterSetSelection(self, index: QModelIndex):
        chart = index.data(Qt.ItemDataRole.UserRole + 10)  # type: Chart
        self.selectChart(chart)

        self.fuzzySearchLineEdit.clear()
        self.fuzzySearchLineEdit.clearFocus()

    def ratingClassButtons(self):
        return self.__RATING_CLASS_BUTTONS

    def selectedRatingClass(self):
        for i, button in enumerate(self.__RATING_CLASS_BUTTONS):
            if button.isChecked():
                return i

    def updateRatingClassButtonsEnabled(self, rating_classes: list[int]):
        for i, button in enumerate(self.__RATING_CLASS_BUTTONS):
            if i in rating_classes:
                button.setEnabled(True)
            else:
                button.setChecked(False)
                button.setEnabled(False)

    def deselectAllRatingClassButtons(self):
        [button.setChecked(False) for button in self.__RATING_CLASS_BUTTONS]

    @Slot()
    def selectRatingClass(self, rating_class: int | None = None):
        if type(rating_class) == int and rating_class in range(4):
            self.deselectAllRatingClassButtons()
            button = self.__RATING_CLASS_BUTTONS[rating_class]
            if button.isEnabled():
                button.setChecked(True)
        else:
            button = self.sender()
            if isinstance(button, RatingClassRadioButton) and button.isEnabled():
                self.deselectAllRatingClassButtons()
                button.setChecked(True)
