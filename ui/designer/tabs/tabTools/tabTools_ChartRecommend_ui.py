# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tabTools_ChartRecommend.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_TabTools_ChartRecommend(object):
    def setupUi(self, TabTools_ChartRecommend):
        if not TabTools_ChartRecommend.objectName():
            TabTools_ChartRecommend.setObjectName(u"TabTools_ChartRecommend")
        TabTools_ChartRecommend.resize(668, 546)
        TabTools_ChartRecommend.setWindowTitle(u"TabTools_ChartRecommend")
        self.verticalLayout = QVBoxLayout(TabTools_ChartRecommend)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(TabTools_ChartRecommend)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.rangeFromPlayRating_playRatingSpinBox = QDoubleSpinBox(self.groupBox)
        self.rangeFromPlayRating_playRatingSpinBox.setObjectName(u"rangeFromPlayRating_playRatingSpinBox")
        self.rangeFromPlayRating_playRatingSpinBox.setMinimumSize(QSize(100, 0))
        self.rangeFromPlayRating_playRatingSpinBox.setMaximumSize(QSize(100, 16777215))
        self.rangeFromPlayRating_playRatingSpinBox.setDecimals(3)
        self.rangeFromPlayRating_playRatingSpinBox.setMaximum(100.000000000000000)
        self.rangeFromPlayRating_playRatingSpinBox.setSingleStep(0.100000000000000)

        self.verticalLayout_2.addWidget(self.rangeFromPlayRating_playRatingSpinBox)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setText(u"AA")
        self.label_3.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout_3.addWidget(self.label_3, 0, 2, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setText(u"EX")
        self.label_2.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout_3.addWidget(self.label_2, 0, 1, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setText(u"EX+")
        self.label.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.rangeFromPlayRating_ExPlusLabel = QLabel(self.groupBox)
        self.rangeFromPlayRating_ExPlusLabel.setObjectName(u"rangeFromPlayRating_ExPlusLabel")
        self.rangeFromPlayRating_ExPlusLabel.setText(u"...")
        self.rangeFromPlayRating_ExPlusLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout_3.addWidget(self.rangeFromPlayRating_ExPlusLabel, 1, 0, 1, 1)

        self.rangeFromPlayRating_ExLabel = QLabel(self.groupBox)
        self.rangeFromPlayRating_ExLabel.setObjectName(u"rangeFromPlayRating_ExLabel")
        self.rangeFromPlayRating_ExLabel.setText(u"...")
        self.rangeFromPlayRating_ExLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout_3.addWidget(self.rangeFromPlayRating_ExLabel, 1, 1, 1, 1)

        self.rangeFromPlayRating_AaLabel = QLabel(self.groupBox)
        self.rangeFromPlayRating_AaLabel.setObjectName(u"rangeFromPlayRating_AaLabel")
        self.rangeFromPlayRating_AaLabel.setText(u"...")
        self.rangeFromPlayRating_AaLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout_3.addWidget(self.rangeFromPlayRating_AaLabel, 1, 2, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_3)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(TabTools_ChartRecommend)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.chartsByConstant_constantSpinBox = QDoubleSpinBox(self.groupBox_2)
        self.chartsByConstant_constantSpinBox.setObjectName(u"chartsByConstant_constantSpinBox")
        self.chartsByConstant_constantSpinBox.setMinimumSize(QSize(100, 0))
        self.chartsByConstant_constantSpinBox.setMaximumSize(QSize(100, 16777215))
        self.chartsByConstant_constantSpinBox.setDecimals(1)
        self.chartsByConstant_constantSpinBox.setMaximum(100.000000000000000)
        self.chartsByConstant_constantSpinBox.setSingleStep(0.100000000000000)

        self.horizontalLayout_3.addWidget(self.chartsByConstant_constantSpinBox)

        self.chartsByConstant_numLabel = QLabel(self.groupBox_2)
        self.chartsByConstant_numLabel.setObjectName(u"chartsByConstant_numLabel")
        self.chartsByConstant_numLabel.setText(u"...")

        self.horizontalLayout_3.addWidget(self.chartsByConstant_numLabel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.chartsByConstant_refreshButton = QPushButton(self.groupBox_2)
        self.chartsByConstant_refreshButton.setObjectName(u"chartsByConstant_refreshButton")
        self.chartsByConstant_refreshButton.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.chartsByConstant_refreshButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.widget = QWidget(self.groupBox_2)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.chartsByConstant_gridLayout = QGridLayout(self.widget)
        self.chartsByConstant_gridLayout.setObjectName(u"chartsByConstant_gridLayout")

        self.verticalLayout_3.addWidget(self.widget)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(TabTools_ChartRecommend)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.chartsRecommendFromPlayRating_playRatingSpinBox = QDoubleSpinBox(self.groupBox_3)
        self.chartsRecommendFromPlayRating_playRatingSpinBox.setObjectName(u"chartsRecommendFromPlayRating_playRatingSpinBox")
        self.chartsRecommendFromPlayRating_playRatingSpinBox.setMinimumSize(QSize(100, 0))
        self.chartsRecommendFromPlayRating_playRatingSpinBox.setMaximumSize(QSize(100, 16777215))
        self.chartsRecommendFromPlayRating_playRatingSpinBox.setDecimals(3)
        self.chartsRecommendFromPlayRating_playRatingSpinBox.setMaximum(100.000000000000000)
        self.chartsRecommendFromPlayRating_playRatingSpinBox.setSingleStep(0.100000000000000)

        self.horizontalLayout_2.addWidget(self.chartsRecommendFromPlayRating_playRatingSpinBox)

        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setText(u"\u00b1")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.chartsRecommendFromPlayRating_boundsSpinBox = QDoubleSpinBox(self.groupBox_3)
        self.chartsRecommendFromPlayRating_boundsSpinBox.setObjectName(u"chartsRecommendFromPlayRating_boundsSpinBox")
        self.chartsRecommendFromPlayRating_boundsSpinBox.setMaximum(2.000000000000000)
        self.chartsRecommendFromPlayRating_boundsSpinBox.setSingleStep(0.010000000000000)
        self.chartsRecommendFromPlayRating_boundsSpinBox.setValue(0.100000000000000)

        self.horizontalLayout_2.addWidget(self.chartsRecommendFromPlayRating_boundsSpinBox)

        self.chartsRecommendFromPlayRating_numLabel = QLabel(self.groupBox_3)
        self.chartsRecommendFromPlayRating_numLabel.setObjectName(u"chartsRecommendFromPlayRating_numLabel")
        self.chartsRecommendFromPlayRating_numLabel.setText(u"...")

        self.horizontalLayout_2.addWidget(self.chartsRecommendFromPlayRating_numLabel)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.chartsRecommendFromPlayRating_refreshButton = QPushButton(self.groupBox_3)
        self.chartsRecommendFromPlayRating_refreshButton.setObjectName(u"chartsRecommendFromPlayRating_refreshButton")
        self.chartsRecommendFromPlayRating_refreshButton.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.chartsRecommendFromPlayRating_refreshButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.widget_2 = QWidget(self.groupBox_3)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.chartsRecommendFromPlayRating_gridLayout = QGridLayout(self.widget_2)
        self.chartsRecommendFromPlayRating_gridLayout.setObjectName(u"chartsRecommendFromPlayRating_gridLayout")

        self.verticalLayout_4.addWidget(self.widget_2)


        self.verticalLayout.addWidget(self.groupBox_3)


        self.retranslateUi(TabTools_ChartRecommend)

        QMetaObject.connectSlotsByName(TabTools_ChartRecommend)
    # setupUi

    def retranslateUi(self, TabTools_ChartRecommend):
        self.groupBox.setTitle(QCoreApplication.translate("TabTools_ChartRecommend", u"constantRangeFromPlayRating", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("TabTools_ChartRecommend", u"chartsByConstant", None))
        self.chartsByConstant_refreshButton.setText(QCoreApplication.translate("TabTools_ChartRecommend", u"refreshButton", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("TabTools_ChartRecommend", u"chartsRecommendFromPlayRating", None))
        self.chartsRecommendFromPlayRating_refreshButton.setText(QCoreApplication.translate("TabTools_ChartRecommend", u"refreshButton", None))
        pass
    # retranslateUi

