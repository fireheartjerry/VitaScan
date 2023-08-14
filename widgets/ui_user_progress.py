# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'progress_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QProgressBar,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_nutrition_progress(object):
    def setupUi(self, nutrition_progress):
        if not nutrition_progress.objectName():
            nutrition_progress.setObjectName(u"nutrition_progress")
        nutrition_progress.resize(706, 695)
        self.info_label = QLabel(nutrition_progress)
        self.info_label.setObjectName(u"info_label")
        self.info_label.setGeometry(QRect(9, 9, 681, 51))
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.info_label.setFont(font)
        self.info_label.setAlignment(Qt.AlignCenter)
        self.layoutWidget = QWidget(nutrition_progress)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(12, 72, 681, 611))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.cal_label = QLabel(self.layoutWidget)
        self.cal_label.setObjectName(u"cal_label")
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.cal_label.setFont(font1)

        self.verticalLayout.addWidget(self.cal_label)

        self.calorie_progress = QProgressBar(self.layoutWidget)
        self.calorie_progress.setObjectName(u"calorie_progress")
        self.calorie_progress.setValue(0)

        self.verticalLayout.addWidget(self.calorie_progress)

        self.sat_fat_label = QLabel(self.layoutWidget)
        self.sat_fat_label.setObjectName(u"sat_fat_label")
        self.sat_fat_label.setFont(font1)

        self.verticalLayout.addWidget(self.sat_fat_label)

        self.saturated_fat_progress = QProgressBar(self.layoutWidget)
        self.saturated_fat_progress.setObjectName(u"saturated_fat_progress")
        self.saturated_fat_progress.setValue(0)

        self.verticalLayout.addWidget(self.saturated_fat_progress)

        self.carb_label = QLabel(self.layoutWidget)
        self.carb_label.setObjectName(u"carb_label")
        self.carb_label.setFont(font1)

        self.verticalLayout.addWidget(self.carb_label)

        self.carb_progress = QProgressBar(self.layoutWidget)
        self.carb_progress.setObjectName(u"carb_progress")
        self.carb_progress.setValue(0)

        self.verticalLayout.addWidget(self.carb_progress)

        self.sugars_label = QLabel(self.layoutWidget)
        self.sugars_label.setObjectName(u"sugars_label")
        self.sugars_label.setFont(font1)

        self.verticalLayout.addWidget(self.sugars_label)

        self.sugar_progress = QProgressBar(self.layoutWidget)
        self.sugar_progress.setObjectName(u"sugar_progress")
        self.sugar_progress.setValue(0)

        self.verticalLayout.addWidget(self.sugar_progress)

        self.fibre_label = QLabel(self.layoutWidget)
        self.fibre_label.setObjectName(u"fibre_label")
        self.fibre_label.setFont(font1)

        self.verticalLayout.addWidget(self.fibre_label)

        self.fibre_progress = QProgressBar(self.layoutWidget)
        self.fibre_progress.setObjectName(u"fibre_progress")
        self.fibre_progress.setValue(0)

        self.verticalLayout.addWidget(self.fibre_progress)

        self.sodium_label = QLabel(self.layoutWidget)
        self.sodium_label.setObjectName(u"sodium_label")
        self.sodium_label.setFont(font1)

        self.verticalLayout.addWidget(self.sodium_label)

        self.sodium_progress = QProgressBar(self.layoutWidget)
        self.sodium_progress.setObjectName(u"sodium_progress")
        self.sodium_progress.setValue(0)

        self.verticalLayout.addWidget(self.sodium_progress)

        self.protein_label = QLabel(self.layoutWidget)
        self.protein_label.setObjectName(u"protein_label")
        self.protein_label.setFont(font1)

        self.verticalLayout.addWidget(self.protein_label)

        self.protein_progress = QProgressBar(self.layoutWidget)
        self.protein_progress.setObjectName(u"protein_progress")
        self.protein_progress.setValue(0)

        self.verticalLayout.addWidget(self.protein_progress)

        self.calcium_label = QLabel(self.layoutWidget)
        self.calcium_label.setObjectName(u"calcium_label")
        self.calcium_label.setFont(font1)

        self.verticalLayout.addWidget(self.calcium_label)

        self.calcium_progress = QProgressBar(self.layoutWidget)
        self.calcium_progress.setObjectName(u"calcium_progress")
        self.calcium_progress.setValue(0)

        self.verticalLayout.addWidget(self.calcium_progress)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ok_btn = QPushButton(self.layoutWidget)
        self.ok_btn.setObjectName(u"ok_btn")
        self.ok_btn.setFont(font1)
        self.ok_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.ok_btn)

        self.reset_bars_btn = QPushButton(self.layoutWidget)
        self.reset_bars_btn.setObjectName(u"reset_bars_btn")
        self.reset_bars_btn.setFont(font1)
        self.reset_bars_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.reset_bars_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(nutrition_progress)

        QMetaObject.connectSlotsByName(nutrition_progress)
    # setupUi

    def retranslateUi(self, nutrition_progress):
        nutrition_progress.setWindowTitle(QCoreApplication.translate("nutrition_progress", u"Form", None))
        self.info_label.setText(QCoreApplication.translate("nutrition_progress", u"Nutritional Progress", None))
        self.cal_label.setText(QCoreApplication.translate("nutrition_progress", u"Calories", None))
        self.sat_fat_label.setText(QCoreApplication.translate("nutrition_progress", u"Saturated Fat", None))
        self.carb_label.setText(QCoreApplication.translate("nutrition_progress", u"Carbohydrates", None))
        self.sugars_label.setText(QCoreApplication.translate("nutrition_progress", u"Sugars", None))
        self.fibre_label.setText(QCoreApplication.translate("nutrition_progress", u"Fibre", None))
        self.sodium_label.setText(QCoreApplication.translate("nutrition_progress", u"Sodium", None))
        self.protein_label.setText(QCoreApplication.translate("nutrition_progress", u"Protein", None))
        self.calcium_label.setText(QCoreApplication.translate("nutrition_progress", u"Calcium", None))
        self.ok_btn.setText(QCoreApplication.translate("nutrition_progress", u"Ok!", None))
        self.reset_bars_btn.setText(QCoreApplication.translate("nutrition_progress", u"Reset Bars", None))
    # retranslateUi

