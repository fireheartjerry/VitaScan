# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(796, 641)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.image_label = QLabel(self.centralwidget)
        self.image_label.setObjectName(u"image_label")
        self.image_label.setGeometry(QRect(-10, 110, 811, 541))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.image_label.setFont(font)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(11, 10, 771, 91))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.select_img_btn = QPushButton(self.layoutWidget)
        self.select_img_btn.setObjectName(u"select_img_btn")
        self.select_img_btn.setFont(font)
        self.select_img_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.select_img_btn)

        self.fetch_data_btn = QPushButton(self.layoutWidget)
        self.fetch_data_btn.setObjectName(u"fetch_data_btn")
        self.fetch_data_btn.setFont(font)
        self.fetch_data_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.fetch_data_btn)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.enter_user_data_btn = QPushButton(self.layoutWidget)
        self.enter_user_data_btn.setObjectName(u"enter_user_data_btn")
        self.enter_user_data_btn.setFont(font)
        self.enter_user_data_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.enter_user_data_btn)

        self.view_progress_btn = QPushButton(self.layoutWidget)
        self.view_progress_btn.setObjectName(u"view_progress_btn")
        self.view_progress_btn.setFont(font)
        self.view_progress_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.view_progress_btn)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.image_label.setText("")
        self.select_img_btn.setText(QCoreApplication.translate("MainWindow", u"Select Image", None))
        self.fetch_data_btn.setText(QCoreApplication.translate("MainWindow", u"Fetch Data", None))
        self.enter_user_data_btn.setText(QCoreApplication.translate("MainWindow", u"Enter User Data", None))
        self.view_progress_btn.setText(QCoreApplication.translate("MainWindow", u"View Progress", None))
    # retranslateUi

