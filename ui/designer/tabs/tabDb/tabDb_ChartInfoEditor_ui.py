# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tabDb_ChartInfoEditor.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFormLayout, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QListView, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from ui.implements.components.chartSelector import ChartSelector

class Ui_TabDb_ChartInfoEditor(object):
    def setupUi(self, TabDb_ChartInfoEditor):
        if not TabDb_ChartInfoEditor.objectName():
            TabDb_ChartInfoEditor.setObjectName(u"TabDb_ChartInfoEditor")
        TabDb_ChartInfoEditor.resize(659, 570)
        TabDb_ChartInfoEditor.setWindowTitle(u"TabDb_ChartInfoEditor")
        self.gridLayout = QGridLayout(TabDb_ChartInfoEditor)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(TabDb_ChartInfoEditor)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(self.groupBox)
        self.widget.setObjectName(u"widget")
        self.formLayout = QFormLayout(self.widget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.notesLineEdit = QLineEdit(self.widget)
        self.notesLineEdit.setObjectName(u"notesLineEdit")
        font = QFont()
        font.setFamilies([u"GeosansLight"])
        font.setPointSize(14)
        font.setBold(True)
        self.notesLineEdit.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.notesLineEdit)

        self.jacketLabel = QLabel(self.widget)
        self.jacketLabel.setObjectName(u"jacketLabel")
        self.jacketLabel.setMinimumSize(QSize(100, 100))
        self.jacketLabel.setMaximumSize(QSize(100, 100))
        self.jacketLabel.setText(u"")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.jacketLabel)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.titleLabel = QLabel(self.widget)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setText(u"...")

        self.verticalLayout.addWidget(self.titleLabel)

        self.ratingLabel = QLabel(self.widget)
        self.ratingLabel.setObjectName(u"ratingLabel")
        self.ratingLabel.setText(u"...")

        self.verticalLayout.addWidget(self.ratingLabel)

        self.verticalSpacer_2 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.verticalLayout)

        self.horizontalWidget_2 = QWidget(self.widget)
        self.horizontalWidget_2.setObjectName(u"horizontalWidget_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget_2.sizePolicy().hasHeightForWidth())
        self.horizontalWidget_2.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.constantLineEdit = QLineEdit(self.horizontalWidget_2)
        self.constantLineEdit.setObjectName(u"constantLineEdit")
        self.constantLineEdit.setFont(font)

        self.horizontalLayout_2.addWidget(self.constantLineEdit)

        self.constantPreviewLabel = QLabel(self.horizontalWidget_2)
        self.constantPreviewLabel.setObjectName(u"constantPreviewLabel")
        self.constantPreviewLabel.setText(u"> ...")

        self.horizontalLayout_2.addWidget(self.constantPreviewLabel)


        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.horizontalWidget_2)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.label_4)


        self.verticalLayout_2.addWidget(self.widget)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.deleteButton = QPushButton(self.groupBox)
        self.deleteButton.setObjectName(u"deleteButton")

        self.horizontalLayout.addWidget(self.deleteButton)

        self.commitButton = QPushButton(self.groupBox)
        self.commitButton.setObjectName(u"commitButton")

        self.horizontalLayout.addWidget(self.commitButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.gridLayout.addWidget(self.groupBox, 1, 1, 1, 1)

        self.chartSelector = ChartSelector(TabDb_ChartInfoEditor)
        self.chartSelector.setObjectName(u"chartSelector")

        self.gridLayout.addWidget(self.chartSelector, 0, 0, 1, 2)

        self.listView = QListView(TabDb_ChartInfoEditor)
        self.listView.setObjectName(u"listView")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.listView.sizePolicy().hasHeightForWidth())
        self.listView.setSizePolicy(sizePolicy2)
        self.listView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listView.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.listView.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.gridLayout.addWidget(self.listView, 1, 0, 1, 1)


        self.retranslateUi(TabDb_ChartInfoEditor)

        QMetaObject.connectSlotsByName(TabDb_ChartInfoEditor)
    # setupUi

    def retranslateUi(self, TabDb_ChartInfoEditor):
        self.groupBox.setTitle(QCoreApplication.translate("TabDb_ChartInfoEditor", u"editor.title", None))
        self.label.setText(QCoreApplication.translate("TabDb_ChartInfoEditor", u"editor.constant", None))
        self.label_2.setText(QCoreApplication.translate("TabDb_ChartInfoEditor", u"editor.notes", None))
        self.label_3.setText(QCoreApplication.translate("TabDb_ChartInfoEditor", u"editor.tip", None))
        self.label_4.setText(QCoreApplication.translate("TabDb_ChartInfoEditor", u"editor.tip.content", None))
        self.deleteButton.setText(QCoreApplication.translate("TabDb_ChartInfoEditor", u"editor.delete", None))
        self.commitButton.setText(QCoreApplication.translate("TabDb_ChartInfoEditor", u"editor.commit", None))
        pass
    # retranslateUi

