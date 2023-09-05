# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tabTools_InfoLookup.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

from ui.implements.components.ratingClassSelector import RatingClassSelector
from ui.implements.components.songIdSelector import SongIdSelector

class Ui_TabTools_InfoLookup(object):
    def setupUi(self, TabTools_InfoLookup):
        if not TabTools_InfoLookup.objectName():
            TabTools_InfoLookup.setObjectName(u"TabTools_InfoLookup")
        TabTools_InfoLookup.resize(665, 570)
        TabTools_InfoLookup.setWindowTitle(u"TabTools_InfoLookup")
        self.verticalLayout = QVBoxLayout(TabTools_InfoLookup)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_9 = QLabel(TabTools_InfoLookup)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_3.addWidget(self.label_9)

        self.langSelectComboBox = QComboBox(TabTools_InfoLookup)
        self.langSelectComboBox.setObjectName(u"langSelectComboBox")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.langSelectComboBox.sizePolicy().hasHeightForWidth())
        self.langSelectComboBox.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.langSelectComboBox)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.groupBox = QGroupBox(TabTools_InfoLookup)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.songIdSelector = SongIdSelector(self.groupBox)
        self.songIdSelector.setObjectName(u"songIdSelector")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.songIdSelector.sizePolicy().hasHeightForWidth())
        self.songIdSelector.setSizePolicy(sizePolicy2)

        self.verticalLayout_4.addWidget(self.songIdSelector)

        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_2 = QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"QLabel { color: gray; }")
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_10, 3, 0, 1, 1)

        self.packIdLabel = QLabel(self.groupBox_3)
        self.packIdLabel.setObjectName(u"packIdLabel")
        self.packIdLabel.setText(u"...")

        self.gridLayout_2.addWidget(self.packIdLabel, 0, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"QLabel { color: gray; }")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)

        self.packDescriptionLabel = QLabel(self.groupBox_3)
        self.packDescriptionLabel.setObjectName(u"packDescriptionLabel")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.packDescriptionLabel.sizePolicy().hasHeightForWidth())
        self.packDescriptionLabel.setSizePolicy(sizePolicy3)
        self.packDescriptionLabel.setMinimumSize(QSize(0, 100))
        self.packDescriptionLabel.setText(u"...")
        self.packDescriptionLabel.setWordWrap(True)

        self.gridLayout_2.addWidget(self.packDescriptionLabel, 3, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"QLabel { color: gray; }")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)

        self.packNameLabel = QLabel(self.groupBox_3)
        self.packNameLabel.setObjectName(u"packNameLabel")
        self.packNameLabel.setText(u"...")

        self.gridLayout_2.addWidget(self.packNameLabel, 1, 1, 1, 1)

        self.gridLayout_2.setColumnStretch(1, 1)
        self.gridLayout_2.setColumnMinimumWidth(1, 100)

        self.verticalLayout_4.addWidget(self.groupBox_3)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.songInfoGroupBox = QGroupBox(self.groupBox)
        self.songInfoGroupBox.setObjectName(u"songInfoGroupBox")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.songInfoGroupBox.sizePolicy().hasHeightForWidth())
        self.songInfoGroupBox.setSizePolicy(sizePolicy4)
        self.gridLayout = QGridLayout(self.songInfoGroupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_23 = QLabel(self.songInfoGroupBox)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"QLabel { color: gray; }")
        self.label_23.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_23, 6, 0, 1, 1)

        self.label_27 = QLabel(self.songInfoGroupBox)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setStyleSheet(u"QLabel { color: gray; }")
        self.label_27.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_27, 8, 0, 1, 1)

        self.songAudioPreviewLabel = QLabel(self.songInfoGroupBox)
        self.songAudioPreviewLabel.setObjectName(u"songAudioPreviewLabel")
        self.songAudioPreviewLabel.setText(u"...")

        self.gridLayout.addWidget(self.songAudioPreviewLabel, 8, 1, 1, 1)

        self.songArtistLabel = QLabel(self.songInfoGroupBox)
        self.songArtistLabel.setObjectName(u"songArtistLabel")
        self.songArtistLabel.setText(u"...")

        self.gridLayout.addWidget(self.songArtistLabel, 3, 1, 1, 1)

        self.label_11 = QLabel(self.songInfoGroupBox)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"QLabel { color: gray; }")
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_11, 3, 0, 1, 1)

        self.songSourceLabel = QLabel(self.songInfoGroupBox)
        self.songSourceLabel.setObjectName(u"songSourceLabel")
        self.songSourceLabel.setText(u"...")

        self.gridLayout.addWidget(self.songSourceLabel, 7, 1, 1, 1)

        self.songTitleLabel = QLabel(self.songInfoGroupBox)
        self.songTitleLabel.setObjectName(u"songTitleLabel")
        self.songTitleLabel.setText(u"...")

        self.gridLayout.addWidget(self.songTitleLabel, 2, 1, 1, 1)

        self.label_19 = QLabel(self.songInfoGroupBox)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"QLabel { color: gray; }")
        self.label_19.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_19, 5, 0, 1, 1)

        self.label_3 = QLabel(self.songInfoGroupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QLabel { color: gray; }")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_15 = QLabel(self.songInfoGroupBox)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"QLabel { color: gray; }")
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_15, 1, 0, 1, 1)

        self.songBgSideLabel = QLabel(self.songInfoGroupBox)
        self.songBgSideLabel.setObjectName(u"songBgSideLabel")
        self.songBgSideLabel.setText(u"...")

        self.gridLayout.addWidget(self.songBgSideLabel, 5, 1, 1, 1)

        self.songIdLabel = QLabel(self.songInfoGroupBox)
        self.songIdLabel.setObjectName(u"songIdLabel")
        self.songIdLabel.setText(u"...")

        self.gridLayout.addWidget(self.songIdLabel, 0, 1, 1, 1)

        self.songDateVersionLabel = QLabel(self.songInfoGroupBox)
        self.songDateVersionLabel.setObjectName(u"songDateVersionLabel")
        self.songDateVersionLabel.setText(u"...")

        self.gridLayout.addWidget(self.songDateVersionLabel, 1, 1, 1, 1)

        self.songBgDayNightLabel = QLabel(self.songInfoGroupBox)
        self.songBgDayNightLabel.setObjectName(u"songBgDayNightLabel")
        self.songBgDayNightLabel.setText(u"...")

        self.gridLayout.addWidget(self.songBgDayNightLabel, 6, 1, 1, 1)

        self.label_6 = QLabel(self.songInfoGroupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"QLabel { color: gray; }")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)

        self.label_14 = QLabel(self.songInfoGroupBox)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"QLabel { color: gray; }")
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_14, 4, 0, 1, 1)

        self.label_25 = QLabel(self.songInfoGroupBox)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"QLabel { color: gray; }")
        self.label_25.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_25, 7, 0, 1, 1)

        self.songBpmLabel = QLabel(self.songInfoGroupBox)
        self.songBpmLabel.setObjectName(u"songBpmLabel")
        self.songBpmLabel.setText(u"...")

        self.gridLayout.addWidget(self.songBpmLabel, 4, 1, 1, 1)

        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnMinimumWidth(1, 150)

        self.horizontalLayout.addWidget(self.songInfoGroupBox)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(TabTools_InfoLookup)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy5)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.ratingClassSelector = RatingClassSelector(self.groupBox_2)
        self.ratingClassSelector.setObjectName(u"ratingClassSelector")
        sizePolicy2.setHeightForWidth(self.ratingClassSelector.sizePolicy().hasHeightForWidth())
        self.ratingClassSelector.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.ratingClassSelector)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.groupBox_5 = QGroupBox(self.groupBox_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy2.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy2)
        self.gridLayout_3 = QGridLayout(self.groupBox_5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.chartConstantLabel = QLabel(self.groupBox_5)
        self.chartConstantLabel.setObjectName(u"chartConstantLabel")
        self.chartConstantLabel.setText(u"...")

        self.gridLayout_3.addWidget(self.chartConstantLabel, 0, 1, 1, 1)

        self.chartNotesLabel = QLabel(self.groupBox_5)
        self.chartNotesLabel.setObjectName(u"chartNotesLabel")
        self.chartNotesLabel.setText(u"...")

        self.gridLayout_3.addWidget(self.chartNotesLabel, 1, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel { color: gray; }")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"QLabel { color: gray; }")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_8, 1, 0, 1, 1)

        self.gridLayout_3.setColumnStretch(1, 1)
        self.gridLayout_3.setColumnMinimumWidth(1, 50)

        self.horizontalLayout_4.addWidget(self.groupBox_5)

        self.groupBox_4 = QGroupBox(self.groupBox_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy4.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy4)
        self.gridLayout_4 = QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_18 = QLabel(self.groupBox_4)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"QLabel { color: gray; }")
        self.label_18.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_18, 0, 3, 1, 1)

        self.difficultyRatingLabel = QLabel(self.groupBox_4)
        self.difficultyRatingLabel.setObjectName(u"difficultyRatingLabel")
        self.difficultyRatingLabel.setText(u"...")

        self.gridLayout_4.addWidget(self.difficultyRatingLabel, 0, 1, 1, 1)

        self.difficultyJacketNightLabel = QLabel(self.groupBox_4)
        self.difficultyJacketNightLabel.setObjectName(u"difficultyJacketNightLabel")
        self.difficultyJacketNightLabel.setText(u"...")

        self.gridLayout_4.addWidget(self.difficultyJacketNightLabel, 4, 4, 1, 1)

        self.difficultyBgLabel = QLabel(self.groupBox_4)
        self.difficultyBgLabel.setObjectName(u"difficultyBgLabel")
        self.difficultyBgLabel.setText(u"...")

        self.gridLayout_4.addWidget(self.difficultyBgLabel, 3, 1, 1, 1)

        self.difficultyBgInverseLabel = QLabel(self.groupBox_4)
        self.difficultyBgInverseLabel.setObjectName(u"difficultyBgInverseLabel")
        self.difficultyBgInverseLabel.setText(u"...")

        self.gridLayout_4.addWidget(self.difficultyBgInverseLabel, 3, 4, 1, 1)

        self.label_31 = QLabel(self.groupBox_4)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setStyleSheet(u"QLabel { color: gray; }")
        self.label_31.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_31, 2, 3, 1, 1)

        self.label_13 = QLabel(self.groupBox_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"QLabel { color: gray; }")
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_13, 0, 0, 1, 1)

        self.label_33 = QLabel(self.groupBox_4)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setStyleSheet(u"QLabel { color: gray; }")
        self.label_33.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_33, 3, 0, 1, 1)

        self.difficultyChartDesignerLabel = QLabel(self.groupBox_4)
        self.difficultyChartDesignerLabel.setObjectName(u"difficultyChartDesignerLabel")
        self.difficultyChartDesignerLabel.setText(u"...")

        self.gridLayout_4.addWidget(self.difficultyChartDesignerLabel, 1, 1, 1, 1)

        self.difficultyAudioOverrideLabel = QLabel(self.groupBox_4)
        self.difficultyAudioOverrideLabel.setObjectName(u"difficultyAudioOverrideLabel")
        self.difficultyAudioOverrideLabel.setText(u"...")

        self.gridLayout_4.addWidget(self.difficultyAudioOverrideLabel, 5, 1, 1, 1)

        self.difficultyBpmLabel = QLabel(self.groupBox_4)
        self.difficultyBpmLabel.setObjectName(u"difficultyBpmLabel")
        self.difficultyBpmLabel.setText(u"...")

        self.gridLayout_4.addWidget(self.difficultyBpmLabel, 4, 1, 1, 1)

        self.label_43 = QLabel(self.groupBox_4)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setStyleSheet(u"QLabel { color: gray; }")
        self.label_43.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_43, 5, 3, 1, 1)

        self.label_22 = QLabel(self.groupBox_4)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"QLabel { color: gray; }")
        self.label_22.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_22, 1, 0, 1, 1)

        self.difficultyJacketOverrideLabel = QLabel(self.groupBox_4)
        self.difficultyJacketOverrideLabel.setObjectName(u"difficultyJacketOverrideLabel")
        self.difficultyJacketOverrideLabel.setText(u"...")

        self.gridLayout_4.addWidget(self.difficultyJacketOverrideLabel, 5, 4, 1, 1)

        self.label_35 = QLabel(self.groupBox_4)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setStyleSheet(u"QLabel { color: gray; }")
        self.label_35.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_35, 5, 0, 1, 1)

        self.label_34 = QLabel(self.groupBox_4)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setStyleSheet(u"QLabel { color: gray; }")
        self.label_34.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_34, 4, 0, 1, 1)

        self.label_41 = QLabel(self.groupBox_4)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setStyleSheet(u"QLabel { color: gray; }")
        self.label_41.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_41, 3, 3, 1, 1)

        self.difficultyDateVersionLabel = QLabel(self.groupBox_4)
        self.difficultyDateVersionLabel.setObjectName(u"difficultyDateVersionLabel")
        self.difficultyDateVersionLabel.setText(u"...")

        self.gridLayout_4.addWidget(self.difficultyDateVersionLabel, 0, 4, 1, 1)

        self.label_26 = QLabel(self.groupBox_4)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setStyleSheet(u"QLabel { color: gray; }")
        self.label_26.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_26, 1, 3, 1, 1)

        self.label_42 = QLabel(self.groupBox_4)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setStyleSheet(u"QLabel { color: gray; }")
        self.label_42.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_42, 4, 3, 1, 1)

        self.label_29 = QLabel(self.groupBox_4)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setStyleSheet(u"QLabel { color: gray; }")
        self.label_29.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_29, 2, 0, 1, 1)

        self.difficultyArtistLabel = QLabel(self.groupBox_4)
        self.difficultyArtistLabel.setObjectName(u"difficultyArtistLabel")
        self.difficultyArtistLabel.setText(u"...")

        self.gridLayout_4.addWidget(self.difficultyArtistLabel, 2, 4, 1, 1)

        self.difficultyJacketDesignerLabel = QLabel(self.groupBox_4)
        self.difficultyJacketDesignerLabel.setObjectName(u"difficultyJacketDesignerLabel")
        self.difficultyJacketDesignerLabel.setText(u"...")

        self.gridLayout_4.addWidget(self.difficultyJacketDesignerLabel, 1, 4, 1, 1)

        self.difficultyTitleLabel = QLabel(self.groupBox_4)
        self.difficultyTitleLabel.setObjectName(u"difficultyTitleLabel")
        self.difficultyTitleLabel.setText(u"...")

        self.gridLayout_4.addWidget(self.difficultyTitleLabel, 2, 1, 1, 1)

        self.line_3 = QFrame(self.groupBox_4)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_3, 0, 2, 6, 1)

        self.gridLayout_4.setColumnStretch(1, 1)
        self.gridLayout_4.setColumnStretch(4, 1)
        self.gridLayout_4.setColumnMinimumWidth(1, 50)
        self.gridLayout_4.setColumnMinimumWidth(4, 50)

        self.horizontalLayout_4.addWidget(self.groupBox_4)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addWidget(self.groupBox_2)


        self.retranslateUi(TabTools_InfoLookup)

        QMetaObject.connectSlotsByName(TabTools_InfoLookup)
    # setupUi

    def retranslateUi(self, TabTools_InfoLookup):
        self.label_9.setText(QCoreApplication.translate("TabTools_InfoLookup", u"langSelect.label", None))
        self.groupBox.setTitle(QCoreApplication.translate("TabTools_InfoLookup", u"songSelect", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("TabTools_InfoLookup", u"packInfo", None))
        self.label_10.setText(QCoreApplication.translate("TabTools_InfoLookup", u"pack.description", None))
        self.label_5.setText(QCoreApplication.translate("TabTools_InfoLookup", u"pack.id", None))
        self.label_7.setText(QCoreApplication.translate("TabTools_InfoLookup", u"pack.name", None))
        self.songInfoGroupBox.setTitle(QCoreApplication.translate("TabTools_InfoLookup", u"songInfo", None))
        self.label_23.setText(QCoreApplication.translate("TabTools_InfoLookup", u"song.bgDayNight", None))
        self.label_27.setText(QCoreApplication.translate("TabTools_InfoLookup", u"song.audioPreview", None))
        self.label_11.setText(QCoreApplication.translate("TabTools_InfoLookup", u"song.artist", None))
        self.label_19.setText(QCoreApplication.translate("TabTools_InfoLookup", u"song.bgSide", None))
        self.label_3.setText(QCoreApplication.translate("TabTools_InfoLookup", u"song.id", None))
        self.label_15.setText(QCoreApplication.translate("TabTools_InfoLookup", u"song.date&version", None))
        self.label_6.setText(QCoreApplication.translate("TabTools_InfoLookup", u"song.title", None))
        self.label_14.setText(QCoreApplication.translate("TabTools_InfoLookup", u"song.bpm", None))
        self.label_25.setText(QCoreApplication.translate("TabTools_InfoLookup", u"song.source", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("TabTools_InfoLookup", u"chartSelect", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("TabTools_InfoLookup", u"chartInfo", None))
        self.label_2.setText(QCoreApplication.translate("TabTools_InfoLookup", u"chart.constant", None))
        self.label_8.setText(QCoreApplication.translate("TabTools_InfoLookup", u"chart.notes", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("TabTools_InfoLookup", u"difficultyInfo", None))
        self.label_18.setText(QCoreApplication.translate("TabTools_InfoLookup", u"difficulty.date&version", None))
        self.label_31.setText(QCoreApplication.translate("TabTools_InfoLookup", u"difficulty.artist", None))
        self.label_13.setText(QCoreApplication.translate("TabTools_InfoLookup", u"difficulty.rating", None))
        self.label_33.setText(QCoreApplication.translate("TabTools_InfoLookup", u"difficulty.bg", None))
        self.label_43.setText(QCoreApplication.translate("TabTools_InfoLookup", u"difficulty.jacketOverride", None))
        self.label_22.setText(QCoreApplication.translate("TabTools_InfoLookup", u"difficulty.chartDesigner", None))
        self.label_35.setText(QCoreApplication.translate("TabTools_InfoLookup", u"difficulty.audioOverride", None))
        self.label_34.setText(QCoreApplication.translate("TabTools_InfoLookup", u"difficulty.bpm", None))
        self.label_41.setText(QCoreApplication.translate("TabTools_InfoLookup", u"difficulty.bgInverse", None))
        self.label_26.setText(QCoreApplication.translate("TabTools_InfoLookup", u"difficulty.jacketDesigner", None))
        self.label_42.setText(QCoreApplication.translate("TabTools_InfoLookup", u"difficulty.jacketNight", None))
        self.label_29.setText(QCoreApplication.translate("TabTools_InfoLookup", u"difficulty.title", None))
        pass
    # retranslateUi

