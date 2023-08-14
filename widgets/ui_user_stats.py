# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_stats.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_user_statistics(object):
    def setupUi(self, user_statistics):
        if not user_statistics.objectName():
            user_statistics.setObjectName(u"user_statistics")
        user_statistics.resize(652, 406)
        self.verticalLayout_3 = QVBoxLayout(user_statistics)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.age_label = QLabel(user_statistics)
        self.age_label.setObjectName(u"age_label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.age_label.setFont(font)

        self.verticalLayout_2.addWidget(self.age_label)

        self.weight_label = QLabel(user_statistics)
        self.weight_label.setObjectName(u"weight_label")
        self.weight_label.setFont(font)

        self.verticalLayout_2.addWidget(self.weight_label)

        self.height_label = QLabel(user_statistics)
        self.height_label.setObjectName(u"height_label")
        self.height_label.setFont(font)

        self.verticalLayout_2.addWidget(self.height_label)

        self.name_label = QLabel(user_statistics)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setFont(font)

        self.verticalLayout_2.addWidget(self.name_label)

        self.goals_label = QLabel(user_statistics)
        self.goals_label.setObjectName(u"goals_label")
        self.goals_label.setFont(font)

        self.verticalLayout_2.addWidget(self.goals_label)

        self.gender_label = QLabel(user_statistics)
        self.gender_label.setObjectName(u"gender_label")
        self.gender_label.setFont(font)

        self.verticalLayout_2.addWidget(self.gender_label)

        self.excercise_label = QLabel(user_statistics)
        self.excercise_label.setObjectName(u"excercise_label")
        self.excercise_label.setFont(font)

        self.verticalLayout_2.addWidget(self.excercise_label)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.age_inp = QLineEdit(user_statistics)
        self.age_inp.setObjectName(u"age_inp")
        font1 = QFont()
        font1.setPointSize(12)
        self.age_inp.setFont(font1)
        self.age_inp.setCursor(QCursor(Qt.IBeamCursor))

        self.verticalLayout.addWidget(self.age_inp)

        self.weight_inp = QLineEdit(user_statistics)
        self.weight_inp.setObjectName(u"weight_inp")
        self.weight_inp.setFont(font1)
        self.weight_inp.setCursor(QCursor(Qt.IBeamCursor))

        self.verticalLayout.addWidget(self.weight_inp)

        self.height_inp = QLineEdit(user_statistics)
        self.height_inp.setObjectName(u"height_inp")
        self.height_inp.setFont(font1)
        self.height_inp.setCursor(QCursor(Qt.IBeamCursor))

        self.verticalLayout.addWidget(self.height_inp)

        self.name_inp = QLineEdit(user_statistics)
        self.name_inp.setObjectName(u"name_inp")
        self.name_inp.setFont(font1)
        self.name_inp.setCursor(QCursor(Qt.IBeamCursor))

        self.verticalLayout.addWidget(self.name_inp)

        self.goals_select = QComboBox(user_statistics)
        self.goals_select.addItem("")
        self.goals_select.addItem("")
        self.goals_select.addItem("")
        self.goals_select.addItem("")
        self.goals_select.setObjectName(u"goals_select")
        self.goals_select.setFont(font1)
        self.goals_select.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.goals_select)

        self.gender_select = QComboBox(user_statistics)
        self.gender_select.addItem("")
        self.gender_select.addItem("")
        self.gender_select.addItem("")
        self.gender_select.setObjectName(u"gender_select")
        self.gender_select.setFont(font1)
        self.gender_select.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.gender_select)

        self.exercise_select = QComboBox(user_statistics)
        self.exercise_select.addItem("")
        self.exercise_select.addItem("")
        self.exercise_select.addItem("")
        self.exercise_select.addItem("")
        self.exercise_select.addItem("")
        self.exercise_select.addItem("")
        self.exercise_select.setObjectName(u"exercise_select")
        self.exercise_select.setFont(font1)
        self.exercise_select.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.exercise_select)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.submit_data_btn = QPushButton(user_statistics)
        self.submit_data_btn.setObjectName(u"submit_data_btn")
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        self.submit_data_btn.setFont(font2)
        self.submit_data_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.submit_data_btn)


        self.retranslateUi(user_statistics)

        QMetaObject.connectSlotsByName(user_statistics)
    # setupUi

    def retranslateUi(self, user_statistics):
        user_statistics.setWindowTitle(QCoreApplication.translate("user_statistics", u"Dialog", None))
        self.age_label.setText(QCoreApplication.translate("user_statistics", u"Age:", None))
        self.weight_label.setText(QCoreApplication.translate("user_statistics", u"Weight (lbs):", None))
        self.height_label.setText(QCoreApplication.translate("user_statistics", u"Height (cm):", None))
        self.name_label.setText(QCoreApplication.translate("user_statistics", u"First Name:", None))
        self.goals_label.setText(QCoreApplication.translate("user_statistics", u"Fitness Goals:", None))
        self.gender_label.setText(QCoreApplication.translate("user_statistics", u"Biological Gender:", None))
        self.excercise_label.setText(QCoreApplication.translate("user_statistics", u"Exercise Amounts:", None))
        self.age_inp.setPlaceholderText(QCoreApplication.translate("user_statistics", u"Example: 65", None))
        self.weight_inp.setPlaceholderText(QCoreApplication.translate("user_statistics", u"Example: 140", None))
        self.height_inp.setPlaceholderText(QCoreApplication.translate("user_statistics", u"Example: 183", None))
        self.name_inp.setPlaceholderText(QCoreApplication.translate("user_statistics", u"Example: John", None))
        self.goals_select.setItemText(0, "")
        self.goals_select.setItemText(1, QCoreApplication.translate("user_statistics", u"Maintain Weight", None))
        self.goals_select.setItemText(2, QCoreApplication.translate("user_statistics", u"Weight Loss", None))
        self.goals_select.setItemText(3, QCoreApplication.translate("user_statistics", u"Weight Gain", None))

        self.gender_select.setItemText(0, "")
        self.gender_select.setItemText(1, QCoreApplication.translate("user_statistics", u"Male", None))
        self.gender_select.setItemText(2, QCoreApplication.translate("user_statistics", u"Female", None))

        self.exercise_select.setItemText(0, "")
        self.exercise_select.setItemText(1, QCoreApplication.translate("user_statistics", u"Sedentary (little or no exercise)", None))
        self.exercise_select.setItemText(2, QCoreApplication.translate("user_statistics", u"Lightly active (light exercise/sports 1-3 days/week)", None))
        self.exercise_select.setItemText(3, QCoreApplication.translate("user_statistics", u"Moderately active (moderate exercise/sports 3-5 days/week)", None))
        self.exercise_select.setItemText(4, QCoreApplication.translate("user_statistics", u"Very active (hard exercise/sports 6-7 days a week)", None))
        self.exercise_select.setItemText(5, QCoreApplication.translate("user_statistics", u"Super active (very hard exercise/sports, physical job, or training)", None))

        self.submit_data_btn.setText(QCoreApplication.translate("user_statistics", u"Submit", None))
    # retranslateUi

