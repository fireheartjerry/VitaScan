# user imports
from classes.NutritionProgress import NutritionProgress
from widgets.ui_main_window import Ui_MainWindow
from modules.helpers import process
from classes.User import User

# pyside6 imports
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

# other imports
import pytesseract as pyt
import numpy as np
import cv2

pyt.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

user = User()
opener = None

from classes.UserStats import UserStats

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app: QApplication) -> None:
        super().__init__()
        self.setupUi(self)
        self.app = app
        self.setWindowTitle("VitaScan Home")
        self.setWindowIcon(QIcon("static/logo_icon.ico"))

        global user
        self.img_path = ""
        self.img = ""
        self.food_info = {}
        self.image_label.setPixmap(QPixmap("static/background.jpg").scaledToWidth(self.image_label.width(), Qt.SmoothTransformation))

        self.select_img_btn.clicked.connect(self.selectImage)
        self.fetch_data_btn.clicked.connect(self.getData)
        self.enter_user_data_btn.clicked.connect(self.enterStats)
        self.view_progress_btn.clicked.connect(self.viewProgress)

        self.setStyleSheet("""
            QWidget {
                background-color: #323232;
                font-size: 20px;
                color: #b1b1b1;
            }

            QPushButton {
                height: 25px;
                background-color: QLinearGradient(
                    x1: 0,
                    x2: 0,
                    y1: 0,
                    y2: 1,
                    stop: 0 #565656,
                    stop: 0.1 #525252,
                    stop: 0.5 #4e4e4e,
                    stop: 0.9 #4a4a4a,
                    stop: 1.0 #464646
                );
                border: 2px solid #1e1e1e;
                border-radius: 15px;
                padding: 5px;
                padding-left: 10px;
                padding-right: 10px;
                color: white;
            }

            QPushButton:pressed {
                background-color: orange;
            }

            QPushButton:hover {
                border-color: orange;
                border-color: white;
            }
        """)

    def displayImage(self) -> None:
        if self.img_path:
            pixmap = QPixmap(self.img_path)
            self.image_label.setPixmap(pixmap.scaledToHeight(self.image_label.height(), Qt.SmoothTransformation))

    def selectImage(self) -> None:
        f_path = QFileDialog.getOpenFileName(QFileDialog(), "Select an Image to Scan", "","Images(*.png *.jpeg *.jpg)")[0]
        if not f_path:
            QMessageBox.critical(self, "Path Error", "Make sure to select a file")
        self.img_path = f_path

        try:
            self.displayImage()
        except Exception as e:
            QMessageBox.critical(self, "Image Display Error", f"An error occurred while displaying the image:\n\n {str(e)}")

    def getData(self) -> None:
        if not self.img_path:
            QMessageBox.critical(self, "No Image", "You have not selected an image.")
        else:
            try:
                self.img = cv2.imread(self.img_path)
                sharpen_kernel = np.array([[0,-1,0], [-1,5,-1], [0,-1,0]])
                self.img = cv2.filter2D(self.img, -1, sharpen_kernel)
                img_data = pyt.image_to_data(self.img, lang="eng", config="--psm 4", output_type=pyt.Output.DICT)["text"]

                self.food_info = process(img_data)
                add = QMessageBox.question(self, "Add Food?", "The data has been successfully fetched. Do you want to log this food info to your profile?", QMessageBox.Yes, QMessageBox.No)

                if (add == QMessageBox.Yes):
                    try:
                        user.update_nutrition(self.food_info)
                        food_msg = "Summary of Nutrition:\n"
                        for val in self.food_info:
                            if (val == "Calories"):
                                food_msg += f"Calories: {self.food_info[val][0]}\n"
                            else:
                                food_msg += f"{val}: {self.food_info[val][0]}{self.food_info[val][1]}"
                                if (self.food_info[val][2] != -1):
                                    food_msg += f", {self.food_info[val][2]}% of daily value."
                                    if (self.food_info[val][2] < 5):
                                        food_msg += " This is a small amount."
                                    elif (self.food_info[val][2] < 15):
                                        food_msg += " This is a good amount."
                                    else:
                                        food_msg += " This is alot!"
                                food_msg += "\n"
                        QMessageBox.information(self, "Food Summary", food_msg)
                    except Exception as e:
                        QMessageBox.critical(self, "Processing Error", f"An error occurred while logging the data:\n\n {str(e)}")
                else:
                    QMessageBox.information(self, "Aborted", "Food adding aborted by user.")
            except Exception as e:
                QMessageBox.critical(self, "Display Error", f"An error occurred while displaying the image data:\n\n {str(e)}")
    
    def enterStats(self) -> None:
        global opener
        opener = UserStats()
        opener.show()
    
    def viewProgress(self) -> None:
        if (not user.stats["gender"] or not user.stats["fitness_goals"] or not user.stats["exercise"]):
            QMessageBox.critical(self, "Error", "User data not filled in")
            return
        global opener
        opener = NutritionProgress()
        opener.info_label.setText(f"{user.stats['name']}\'s Nutritional Progress")
        opener.initalizeBars(user)
        opener.setBars(user)
        opener.show()
