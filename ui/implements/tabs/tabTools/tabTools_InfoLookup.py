import re

from arcaea_offline.database import Database
from PySide6.QtCore import QDateTime
from PySide6.QtWidgets import QVBoxLayout, QWidget

from ui.designer.tabs.tabTools.tabTools_InfoLookup_ui import Ui_TabTools_InfoLookup
from ui.extends.shared.language import LanguageChangeEventFilter


class TabTools_InfoLookup(Ui_TabTools_InfoLookup, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.languageChangeEventFilter = LanguageChangeEventFilter(self)
        self.installEventFilter(self.languageChangeEventFilter)

        self.ratingClassSelector.setLayout(QVBoxLayout)

        self.db = Database()

        self.songIdSelector.valueChanged.connect(self.updatePackLabels)
        self.songIdSelector.valueChanged.connect(self.updateSongLabels)
        self.songIdSelector.valueChanged.connect(self.updateRatingClassEnabled)
        self.ratingClassSelector.valueChanged.connect(self.updateDifficultyLabels)
        self.ratingClassSelector.valueChanged.connect(self.updateChartInfoLabels)

        self.songIdSelector.valueChanged.connect(self.updatePlayRatingCalculator)
        self.ratingClassSelector.valueChanged.connect(self.updatePlayRatingCalculator)

        self.langSelectComboBox.addItem("En - English [en]", "en")
        self.langSelectComboBox.addItem("あ - Japanese [ja]", "ja")
        self.langSelectComboBox.addItem("한 - Korean [ko]", "ko")
        self.langSelectComboBox.addItem("简 - Simplified Chinese [zh_hans]", "zh_hans")
        self.langSelectComboBox.addItem("繁 - Traditional Chinese [zh_hant]", "zh_hant")
        self.langSelectComboBox.setCurrentIndex(0)

        self.langSelectComboBox.currentIndexChanged.connect(self.updatePackLabels)
        self.langSelectComboBox.currentIndexChanged.connect(self.updateSongLabels)
        self.langSelectComboBox.currentIndexChanged.connect(self.updateDifficultyLabels)

        self.packLabels = [
            attr
            for attrName, attr in self.__dict__.items()
            if re.match(r"^pack.*Label$", attrName)
        ]
        self.songLabels = [
            attr
            for attrName, attr in self.__dict__.items()
            if re.match(r"^song.*Label$", attrName)
        ]
        self.difficultyLabels = [
            attr
            for attrName, attr in self.__dict__.items()
            if re.match(r"^difficulty.*Label$", attrName)
        ]
        self.chartInfoLabels = [
            attr
            for attrName, attr in self.__dict__.items()
            if re.match(r"^chart.*Label$", attrName)
        ]

    def getLocalizedItem(self, obj, objLocalized, attrName):
        if not objLocalized:
            return getattr(obj, attrName)

        currentLang = self.langSelectComboBox.currentData()
        if currentLang == "en":
            return getattr(obj, attrName)

        localized = getattr(objLocalized, f"{attrName}_{currentLang}")
        return localized or getattr(obj, attrName)

    def resetLabels(self, labelList):
        [label.setText("...") for label in labelList]

    def resetPackLabels(self):
        self.resetLabels(self.packLabels)

    def updatePackLabels(self):
        packId = self.songIdSelector.packId()
        if not packId:
            self.resetPackLabels()
            return

        pack = self.db.get_pack(packId)
        packLocalized = self.db.get_pack_localized(packId)

        name = self.getLocalizedItem(pack, packLocalized, "name")
        description = self.getLocalizedItem(pack, packLocalized, "description")

        self.packIdLabel.setText(pack.id)
        self.packNameLabel.setText(name)
        self.packDescriptionLabel.setText(
            description.replace("\n", " ") if description else "-"
        )

    def resetSongLabels(self):
        self.resetLabels(self.songLabels)

    def updateSongLabels(self):
        songId = self.songIdSelector.songId()
        if not songId:
            self.resetSongLabels()
            return

        song = self.db.get_song(songId)
        songLocalized = self.db.get_song_localized(songId)

        title = self.getLocalizedItem(song, songLocalized, "title")
        bgSideTexts = []
        if song.side is not None:
            bgSideTexts.append(["Light", "Conflict", "Achromatic"][song.side])
        if song.bg:
            text = song.bg
            if song.bg_inverse:
                text += f" ⇄ {song.bg_inverse}"
            bgSideTexts.append(text)
        bgSideText = ", ".join(bgSideTexts) if bgSideTexts else "-"
        source = self.getLocalizedItem(song, songLocalized, "source")
        dateTimeStr = QDateTime.fromSecsSinceEpoch(song.date).toString(
            "yyyy-MM-dd HH:mm:ss"
        )

        self.songIdLabel.setText(f"({song.idx or '-'}) {song.id}")
        self.songTitleLabel.setText(title)
        self.songArtistLabel.setText(song.artist)
        self.songBpmLabel.setText(f"{song.bpm_base} ({song.bpm})")
        self.songAddedInLabel.setText(f"v{song.version}, {dateTimeStr}")
        self.songBgSideLabel.setText(bgSideText)
        self.songBgDayNightLabel.setText(f"{song.bg_day or '-'}/{song.bg_night or '-'}")
        self.songSourceLabel.setText(source)
        self.songAudioPreviewLabel.setText(
            f"{song.audio_preview / 1000:.2f}s~{song.audio_preview_end / 1000:.2f}s"
        )

    def updateRatingClassEnabled(self):
        songId = self.songIdSelector.songId()
        if songId:
            ratingClasses = [
                c.rating_class for c in self.db.get_charts_by_song_id(songId)
            ]
            self.ratingClassSelector.setButtonsEnabled(ratingClasses)

    def resetDifficultyLabels(self):
        self.resetLabels(self.difficultyLabels)

    def updateDifficultyLabels(self):
        songId = self.songIdSelector.songId()
        ratingClass = self.ratingClassSelector.value()

        if not songId or ratingClass is None:
            self.resetDifficultyLabels()
            return

        difficulty = self.db.get_difficulty(songId, ratingClass)
        difficultyLocalized = self.db.get_difficulty_localized(songId, ratingClass)

        title = self.getLocalizedItem(difficulty, difficultyLocalized, "title")
        if difficulty.date:
            dateTimeStr = QDateTime.fromSecsSinceEpoch(difficulty.date).toString(
                "yyyy-MM-dd HH:mm:ss"
            )
            versionDateStr = f"v{difficulty.version}, {dateTimeStr}"
        else:
            versionDateStr = "-"

        self.difficultyRatingLabel.setText(
            f"{difficulty.rating}{'+' if difficulty.rating_plus else ''}"
        )
        self.difficultyAddedInLabel.setText(versionDateStr)
        self.difficultyChartDesignerLabel.setText(difficulty.chart_designer or "-")
        self.difficultyJacketDesignerLabel.setText(difficulty.jacket_desginer or "-")
        self.difficultyTitleLabel.setText(title or "-")
        self.difficultyArtistLabel.setText(difficulty.artist or "-")
        self.difficultyBgLabel.setText(difficulty.bg or "-")
        self.difficultyBgInverseLabel.setText(difficulty.bg_inverse or "-")
        self.difficultyBpmLabel.setText(
            f"{difficulty.bpm_base} ({difficulty.bpm})" if difficulty.bpm else "-"
        )
        self.difficultyJacketNightLabel.setText(difficulty.jacket_night or "-")
        self.difficultyAudioOverrideLabel.setText(str(difficulty.audio_override))
        self.difficultyJacketOverrideLabel.setText(str(difficulty.jacket_override))

    def resetChartInfoLabels(self):
        self.resetLabels(self.chartInfoLabels)

    def updateChartInfoLabels(self):
        songId = self.songIdSelector.songId()
        ratingClass = self.ratingClassSelector.value()

        if not songId or ratingClass is None:
            self.resetChartInfoLabels()
            return

        chartInfo = self.db.get_chart_info(songId, ratingClass)

        if not chartInfo:
            self.resetChartInfoLabels()
            return

        self.chartConstantLabel.setText(str(chartInfo.constant / 10))
        self.chartNotesLabel.setText(
            str(chartInfo.notes) if chartInfo.notes is not None else "-"
        )

    def updatePlayRatingCalculator(self):
        songId = self.songIdSelector.songId()
        ratingClass = self.ratingClassSelector.value()
        chartInfo = self.db.get_chart_info(songId, ratingClass)

        if not chartInfo:
            self.playRatingCalculator.setConstant(None)
        else:
            self.playRatingCalculator.setConstant(chartInfo.constant)
