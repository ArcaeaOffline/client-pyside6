from arcaea_offline.calculate import calculate_play_rating
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QWidget,
)

from ui.extends.shared.language import LanguageChangeEventFilter

from .arcaeaScoreLineEdit import ArcaeaScoreLineEdit


class PlayRatingCalculator(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.languageChangeEventFilter = LanguageChangeEventFilter(self)
        self.installEventFilter(self.languageChangeEventFilter)

        self.setupUi()

        self.arcaeaScoreLineEdit.textChanged.connect(self.updateResultLabel)
        self.copyButton.clicked.connect(self.on_copyButton_clicked)

        self.constant: int | None = None

    def setConstant(self, constant: int | None):
        self.constant = constant
        self.updateResultLabel()

    @property
    def result(self):
        if self.constant is None:
            return None

        score = self.arcaeaScoreLineEdit.score()
        return None if score is None else calculate_play_rating(self.constant, score)

    def updateResultLabel(self):
        result = self.result
        self.resultLabel.setText(str(round(result, 3)) if result is not None else "...")
        self.resultLabel.setToolTip(str(result))

    def on_copyButton_clicked(self):
        result = self.result
        if result is not None:
            QGuiApplication.clipboard().setText(str(result))

    def setupUi(self, *args):
        self.horizontalLayout = QHBoxLayout(self)

        self.arcaeaScoreLineEdit = ArcaeaScoreLineEdit(self)
        self.horizontalLayout.addWidget(self.arcaeaScoreLineEdit)

        self.label = QLabel(self)
        self.label.setText(" > ")
        self.horizontalLayout.addWidget(self.label)

        self.resultLabel = QLabel(self)
        self.resultLabel.setText("...")
        self.resultLabel.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred
        )
        self.resultLabel.setMinimumWidth(100)
        self.horizontalLayout.addWidget(self.resultLabel)

        self.horizontalSpacer = QSpacerItem(
            20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred
        )
        self.horizontalLayout.addSpacerItem(self.horizontalSpacer)

        self.copyButton = QPushButton(self)
        self.horizontalLayout.addWidget(self.copyButton)

        self.retranslateUi()

    def retranslateUi(self, *args):
        self.copyButton.setText(
            QCoreApplication.translate("PotentialCalculator", "copyButton")
        )
