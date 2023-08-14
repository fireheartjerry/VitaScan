# user imports
from widgets.ui_user_stats import Ui_user_statistics
from classes.MainWindow import user
from classes.User import User

# pyside6 imports
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

def has_error(data: dict[str, str]) -> str:
    if any(value == "" for value in data.values()):
        return "Please fill in all data values."
    if not (0 <= int(data["age"]) <= 130):
        return "Enter a realistic age between 0 and 130."
    if not (20 <= float(data["height"]) <= 275):
        return "Enter a realistic height between 20 and 275."
    if not (7.5 <= float(data["weight"]) <= 500):
        return "Enter a realistic weight between 7.5 and 500."
    if not (len(data["name"]) <= 15):
        return "Enter a name that is at most 15 charectars."
    if (' ' in data["name"]):
        return "Enter first name only."
    return ""

class UserStats(QWidget, Ui_user_statistics):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("VitaScan UserStats")
        self.setWindowIcon(QIcon("static/logo_icon.ico"))

        global user
        if (user.stats["age"]):
            self.age_inp.setText(str(user.stats["age"]))
            self.weight_inp.setText(str(user.stats["weight"]))
            self.height_inp.setText(str(user.stats["height"]))
            self.name_inp.setText(str(user.stats["name"]))

            self.goals_select.setCurrentIndex(self.goals_select.findText(user.stats["fitness_goals"], Qt.MatchFixedString))
            self.gender_select.setCurrentIndex(self.gender_select.findText(user.stats["gender"], Qt.MatchFixedString))
            self.exercise_select.setCurrentIndex(self.exercise_select.findText(user.stats["exercise"], Qt.MatchFixedString))
            
        self.submit_data_btn.clicked.connect(self.get_user_data)
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
                color: white;
            }

            QPushButton:hover {
                border-color: orange;
                border-color: white;
            }

            QComboBox, QLineEdit {
                background-color: #464646;
                border-radius: 10px;
                border: 1.5px solid #1e1e1e;
                padding: 5px;
                color: white;
            }

            QComboBox::drop-down {
                image: url(static/down_arrow.png);
                padding-right: 5px;
                padding-top: 11px;
            }

            QComboBox QAbstractItemView {
                background-color: #464646;
                border: 1px solid #1e1e1e;
                border-radius: 3px;
                selection-background-color: #4a4a4a;
                color: white;
            }

            QLineEdit:focus, QComboBox:focus {
                border: 1.5px solid orange;
                border-radius: 10px;
            }
        """)

    def set_user(self, user: User) -> None:
        user.update_stats(user.stats)
        user.update_nutrition(user.nutrition)

    def get_user_data(self) -> None:
        global user
        age = self.age_inp.text()
        weight = self.weight_inp.text()
        height = self.height_inp.text()
        name = self.name_inp.text()
        fitness_goal = self.goals_select.currentText()
        gender = self.gender_select.currentText()
        exercise = self.exercise_select.currentText()

        data = {
            "age": age,
            "weight": weight,
            "height": height,
            "name": name,
            "fitness_goal": fitness_goal,
            "gender": gender,
            "exercise": exercise
        }
        
        err = has_error(data)
        if (err):
            QMessageBox.critical(self, "Error", err)
            return

        msg = ""
        for val in data:
            msg += f"{val}: {data[val]}\n"
        
        cont = QMessageBox.question(self, "Verify your info", f"Please verify the information you entered, would you like to proceed with this?\n\n{msg}", QMessageBox.Yes, QMessageBox.No)
        if (cont == QMessageBox.No):
            QMessageBox.information(self, "Aborted", "Operation aborted by user, please re-enter data.")
            return

        user.update_stats(data)
        self.close()
        QMessageBox.information(self, "Successfull", "Data has been saved!")