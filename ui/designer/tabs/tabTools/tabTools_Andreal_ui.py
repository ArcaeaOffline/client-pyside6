# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tabTools_Andreal.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QHBoxLayout,
    QLabel, QPushButton, QRadioButton, QSizePolicy,
    QSlider, QSpacerItem, QSpinBox, QWidget)

from ui.implements.components.fileSelector import FileSelector

class Ui_TabTools_Andreal(object):
    def setupUi(self, TabTools_Andreal):
        if not TabTools_Andreal.objectName():
            TabTools_Andreal.setObjectName(u"TabTools_Andreal")
        TabTools_Andreal.resize(551, 500)
        TabTools_Andreal.setWindowTitle(u"TabTools_Andreal")
        self.formLayout = QFormLayout(TabTools_Andreal)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label = QLabel(TabTools_Andreal)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.andrealFolderSelector = FileSelector(TabTools_Andreal)
        self.andrealFolderSelector.setObjectName(u"andrealFolderSelector")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.andrealFolderSelector)

        self.label_2 = QLabel(TabTools_Andreal)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.andrealExecutableSelector = FileSelector(TabTools_Andreal)
        self.andrealExecutableSelector.setObjectName(u"andrealExecutableSelector")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.andrealExecutableSelector)

        self.label_3 = QLabel(TabTools_Andreal)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.horizontalWidget = QWidget(TabTools_Andreal)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalLayout = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.imageType_infoRadioButton = QRadioButton(self.horizontalWidget)
        self.imageType_infoRadioButton.setObjectName(u"imageType_infoRadioButton")
        self.imageType_infoRadioButton.setChecked(True)

        self.horizontalLayout.addWidget(self.imageType_infoRadioButton)

        self.imageType_best30RadioButton = QRadioButton(self.horizontalWidget)
        self.imageType_best30RadioButton.setObjectName(u"imageType_best30RadioButton")

        self.horizontalLayout.addWidget(self.imageType_best30RadioButton)

        self.imageType_bestRadioButton = QRadioButton(self.horizontalWidget)
        self.imageType_bestRadioButton.setObjectName(u"imageType_bestRadioButton")

        self.horizontalLayout.addWidget(self.imageType_bestRadioButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.imageTypeWhatIsThisButton = QPushButton(self.horizontalWidget)
        self.imageTypeWhatIsThisButton.setObjectName(u"imageTypeWhatIsThisButton")

        self.horizontalLayout.addWidget(self.imageTypeWhatIsThisButton)


        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.horizontalWidget)

        self.chartFormLabel = QLabel(TabTools_Andreal)
        self.chartFormLabel.setObjectName(u"chartFormLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.chartFormLabel)

        self.label_5 = QLabel(TabTools_Andreal)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.imageVersionComboBox = QComboBox(TabTools_Andreal)
        self.imageVersionComboBox.setObjectName(u"imageVersionComboBox")
        self.imageVersionComboBox.setMaximumSize(QSize(100, 16777215))

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.imageVersionComboBox)

        self.label_6 = QLabel(TabTools_Andreal)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_6)

        self.jpgQualityFormLabel = QLabel(TabTools_Andreal)
        self.jpgQualityFormLabel.setObjectName(u"jpgQualityFormLabel")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.jpgQualityFormLabel)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.exportJsonButton = QPushButton(TabTools_Andreal)
        self.exportJsonButton.setObjectName(u"exportJsonButton")

        self.horizontalLayout_5.addWidget(self.exportJsonButton)

        self.generatePreviewButton = QPushButton(TabTools_Andreal)
        self.generatePreviewButton.setObjectName(u"generatePreviewButton")

        self.horizontalLayout_5.addWidget(self.generatePreviewButton)

        self.generateImageButton = QPushButton(TabTools_Andreal)
        self.generateImageButton.setObjectName(u"generateImageButton")
        font = QFont()
        font.setBold(True)
        self.generateImageButton.setFont(font)

        self.horizontalLayout_5.addWidget(self.generateImageButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.formLayout.setLayout(7, QFormLayout.SpanningRole, self.horizontalLayout_5)

        self.horizontalWidget_2 = QWidget(TabTools_Andreal)
        self.horizontalWidget_2.setObjectName(u"horizontalWidget_2")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget_2.sizePolicy().hasHeightForWidth())
        self.horizontalWidget_2.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.imageFormat_jpgRadioButton = QRadioButton(self.horizontalWidget_2)
        self.imageFormat_jpgRadioButton.setObjectName(u"imageFormat_jpgRadioButton")
        self.imageFormat_jpgRadioButton.setText(u"JPG")
        self.imageFormat_jpgRadioButton.setChecked(True)

        self.horizontalLayout_2.addWidget(self.imageFormat_jpgRadioButton)

        self.imageFormat_pngRadioButton = QRadioButton(self.horizontalWidget_2)
        self.imageFormat_pngRadioButton.setObjectName(u"imageFormat_pngRadioButton")
        self.imageFormat_pngRadioButton.setText(u"PNG")

        self.horizontalLayout_2.addWidget(self.imageFormat_pngRadioButton)


        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.horizontalWidget_2)

        self.label_8 = QLabel(TabTools_Andreal)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_8)

        self.previewLabel = QLabel(TabTools_Andreal)
        self.previewLabel.setObjectName(u"previewLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.previewLabel.sizePolicy().hasHeightForWidth())
        self.previewLabel.setSizePolicy(sizePolicy1)
        self.previewLabel.setStyleSheet(u"QLabel { color: red }")
        self.previewLabel.setText(u"")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.previewLabel)

        self.jpgQualityHolderWidget = QWidget(TabTools_Andreal)
        self.jpgQualityHolderWidget.setObjectName(u"jpgQualityHolderWidget")
        self.horizontalLayout_3 = QHBoxLayout(self.jpgQualityHolderWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.jpgQualitySlider = QSlider(self.jpgQualityHolderWidget)
        self.jpgQualitySlider.setObjectName(u"jpgQualitySlider")
        self.jpgQualitySlider.setMinimum(10)
        self.jpgQualitySlider.setMaximum(100)
        self.jpgQualitySlider.setValue(90)
        self.jpgQualitySlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.jpgQualitySlider)

        self.jpgQualitySpinBox = QSpinBox(self.jpgQualityHolderWidget)
        self.jpgQualitySpinBox.setObjectName(u"jpgQualitySpinBox")
        self.jpgQualitySpinBox.setMinimum(10)
        self.jpgQualitySpinBox.setMaximum(100)
        self.jpgQualitySpinBox.setValue(90)

        self.horizontalLayout_3.addWidget(self.jpgQualitySpinBox)


        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.jpgQualityHolderWidget)

        self.chartHolderWidget = QWidget(TabTools_Andreal)
        self.chartHolderWidget.setObjectName(u"chartHolderWidget")
        self.chartHolderWidget.setEnabled(False)
        self.horizontalLayout_8 = QHBoxLayout(self.chartHolderWidget)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.chartSelectButton = QPushButton(self.chartHolderWidget)
        self.chartSelectButton.setObjectName(u"chartSelectButton")
        self.chartSelectButton.setMaximumSize(QSize(100, 100))

        self.horizontalLayout_8.addWidget(self.chartSelectButton)

        self.chartSelectLabel = QLabel(self.chartHolderWidget)
        self.chartSelectLabel.setObjectName(u"chartSelectLabel")
        self.chartSelectLabel.setText(u"...")

        self.horizontalLayout_8.addWidget(self.chartSelectLabel)


        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.chartHolderWidget)


        self.retranslateUi(TabTools_Andreal)
        self.imageFormat_jpgRadioButton.toggled.connect(self.jpgQualityHolderWidget.setEnabled)
        self.imageType_bestRadioButton.toggled.connect(self.chartHolderWidget.setEnabled)

        QMetaObject.connectSlotsByName(TabTools_Andreal)
    # setupUi

    def retranslateUi(self, TabTools_Andreal):
        self.label.setText(QCoreApplication.translate("TabTools_Andreal", u"andrealFolder", None))
        self.label_2.setText(QCoreApplication.translate("TabTools_Andreal", u"andrealExecutable", None))
        self.label_3.setText(QCoreApplication.translate("TabTools_Andreal", u"imageType", None))
        self.imageType_infoRadioButton.setText(QCoreApplication.translate("TabTools_Andreal", u"/a", None))
        self.imageType_best30RadioButton.setText(QCoreApplication.translate("TabTools_Andreal", u"/a b30", None))
        self.imageType_bestRadioButton.setText(QCoreApplication.translate("TabTools_Andreal", u"/a info", None))
        self.imageTypeWhatIsThisButton.setText(QCoreApplication.translate("TabTools_Andreal", u"imageTypeWhatIsThisButton", None))
        self.chartFormLabel.setText(QCoreApplication.translate("TabTools_Andreal", u"chart", None))
        self.label_5.setText(QCoreApplication.translate("TabTools_Andreal", u"imageVersion", None))
        self.label_6.setText(QCoreApplication.translate("TabTools_Andreal", u"imageFormat", None))
        self.jpgQualityFormLabel.setText(QCoreApplication.translate("TabTools_Andreal", u"jpgQuality", None))
        self.exportJsonButton.setText(QCoreApplication.translate("TabTools_Andreal", u"exportJsonButton", None))
        self.generatePreviewButton.setText(QCoreApplication.translate("TabTools_Andreal", u"generatePreviewButton", None))
        self.generateImageButton.setText(QCoreApplication.translate("TabTools_Andreal", u"generateImageButton", None))
        self.label_8.setText(QCoreApplication.translate("TabTools_Andreal", u"preview", None))
        self.chartSelectButton.setText(QCoreApplication.translate("TabTools_Andreal", u"chart.selectButton", None))
        pass
    # retranslateUi

