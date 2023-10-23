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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDoubleSpinBox, QFormLayout,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QListView, QSizePolicy, QTableView,
    QVBoxLayout, QWidget)

class Ui_TabTools_ChartRecommend(object):
    def setupUi(self, TabTools_ChartRecommend):
        if not TabTools_ChartRecommend.objectName():
            TabTools_ChartRecommend.setObjectName(u"TabTools_ChartRecommend")
        TabTools_ChartRecommend.resize(616, 500)
        TabTools_ChartRecommend.setWindowTitle(u"TabTools_ChartRecommend")
        self.gridLayout = QGridLayout(TabTools_ChartRecommend)
        self.gridLayout.setObjectName(u"gridLayout")
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
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chartsByConstant_numLabel.sizePolicy().hasHeightForWidth())
        self.chartsByConstant_numLabel.setSizePolicy(sizePolicy)
        self.chartsByConstant_numLabel.setText(u"...")

        self.horizontalLayout_3.addWidget(self.chartsByConstant_numLabel)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.chartsByConstant_modelView = QListView(self.groupBox_2)
        self.chartsByConstant_modelView.setObjectName(u"chartsByConstant_modelView")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.chartsByConstant_modelView.sizePolicy().hasHeightForWidth())
        self.chartsByConstant_modelView.setSizePolicy(sizePolicy1)
        self.chartsByConstant_modelView.setMinimumSize(QSize(150, 0))
        self.chartsByConstant_modelView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.chartsByConstant_modelView.setSelectionMode(QAbstractItemView.NoSelection)
        self.chartsByConstant_modelView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.chartsByConstant_modelView.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.chartsByConstant_modelView.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.verticalLayout_3.addWidget(self.chartsByConstant_modelView)


        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 1)

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

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.formLayout.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setText(u"EX+")
        self.label.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.rangeFromPlayRating_ExPlusLabel = QLabel(self.groupBox)
        self.rangeFromPlayRating_ExPlusLabel.setObjectName(u"rangeFromPlayRating_ExPlusLabel")
        self.rangeFromPlayRating_ExPlusLabel.setText(u"...")
        self.rangeFromPlayRating_ExPlusLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.rangeFromPlayRating_ExPlusLabel)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setText(u"EX")
        self.label_2.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.rangeFromPlayRating_ExLabel = QLabel(self.groupBox)
        self.rangeFromPlayRating_ExLabel.setObjectName(u"rangeFromPlayRating_ExLabel")
        self.rangeFromPlayRating_ExLabel.setText(u"...")
        self.rangeFromPlayRating_ExLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.rangeFromPlayRating_ExLabel)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setText(u"AA")
        self.label_3.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.rangeFromPlayRating_AaLabel = QLabel(self.groupBox)
        self.rangeFromPlayRating_AaLabel.setObjectName(u"rangeFromPlayRating_AaLabel")
        self.rangeFromPlayRating_AaLabel.setText(u"...")
        self.rangeFromPlayRating_AaLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.rangeFromPlayRating_AaLabel)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setText(u"A")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_5)

        self.rangeFromPlayRating_ALabel = QLabel(self.groupBox)
        self.rangeFromPlayRating_ALabel.setObjectName(u"rangeFromPlayRating_ALabel")
        self.rangeFromPlayRating_ALabel.setText(u"...")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.rangeFromPlayRating_ALabel)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setText(u"B")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_8)

        self.rangeFromPlayRating_BLabel = QLabel(self.groupBox)
        self.rangeFromPlayRating_BLabel.setObjectName(u"rangeFromPlayRating_BLabel")
        self.rangeFromPlayRating_BLabel.setText(u"...")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.rangeFromPlayRating_BLabel)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setText(u"C")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_10)

        self.rangeFromPlayRating_CLabel = QLabel(self.groupBox)
        self.rangeFromPlayRating_CLabel.setObjectName(u"rangeFromPlayRating_CLabel")
        self.rangeFromPlayRating_CLabel.setText(u"...")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.rangeFromPlayRating_CLabel)


        self.verticalLayout_2.addLayout(self.formLayout)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

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
        sizePolicy.setHeightForWidth(self.chartsRecommendFromPlayRating_numLabel.sizePolicy().hasHeightForWidth())
        self.chartsRecommendFromPlayRating_numLabel.setSizePolicy(sizePolicy)
        self.chartsRecommendFromPlayRating_numLabel.setText(u"...")

        self.horizontalLayout_2.addWidget(self.chartsRecommendFromPlayRating_numLabel)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.chartsRecommendFromPlayRating_modelView = QTableView(self.groupBox_3)
        self.chartsRecommendFromPlayRating_modelView.setObjectName(u"chartsRecommendFromPlayRating_modelView")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.chartsRecommendFromPlayRating_modelView.sizePolicy().hasHeightForWidth())
        self.chartsRecommendFromPlayRating_modelView.setSizePolicy(sizePolicy2)
        self.chartsRecommendFromPlayRating_modelView.setMinimumSize(QSize(200, 0))
        self.chartsRecommendFromPlayRating_modelView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.chartsRecommendFromPlayRating_modelView.setSelectionMode(QAbstractItemView.NoSelection)
        self.chartsRecommendFromPlayRating_modelView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.chartsRecommendFromPlayRating_modelView.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.chartsRecommendFromPlayRating_modelView.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.verticalLayout_4.addWidget(self.chartsRecommendFromPlayRating_modelView)


        self.gridLayout.addWidget(self.groupBox_3, 1, 0, 1, 2)


        self.retranslateUi(TabTools_ChartRecommend)

        QMetaObject.connectSlotsByName(TabTools_ChartRecommend)
    # setupUi

    def retranslateUi(self, TabTools_ChartRecommend):
        self.groupBox_2.setTitle(QCoreApplication.translate("TabTools_ChartRecommend", u"chartsByConstant", None))
        self.groupBox.setTitle(QCoreApplication.translate("TabTools_ChartRecommend", u"constantRangeFromPlayRating", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("TabTools_ChartRecommend", u"chartsRecommendFromPlayRating", None))
        pass
    # retranslateUi

