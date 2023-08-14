from widgets.ui_user_progress import Ui_nutrition_progress
from classes.User import User

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class NutritionProgress(QWidget, Ui_nutrition_progress):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("VitaScan Nutrition Progress")
        self.reset_bars_btn.clicked.connect(self.resetBars)
        self.ok_btn.clicked.connect(self.close)

        self.cal_label.setToolTip("A calorie is a unit of energy. In nutrition, calories refer to the energy people get from the food and drink they consume, and the energy they use in physical activity.")
        self.sat_fat_label.setToolTip("Saturated fat is a type of fat containing a high proportion of fatty acid molecules without double bonds, considered to be less healthy in the diet than unsaturated fat. Try to limit your intake of this.")
        self.carb_label.setToolTip("Carbohydrates are found in a wide array of both healthy and unhealthy foods, such as bread, beans, milk, popcorn, potatoes, cookies, spaghetti, soft drinks, corn, and cherry pie. They also come in a variety of forms. The most common and abundant forms are sugars, fibers, and starches.")
        self.sugars_label.setToolTip("Sugar is used as a preservative, a viscosity-enhancing agent, a sweetening agent, and for other reasons in foods and beverages. Health Canaday has said that consuming too many added sugars has been linked to an increased risk of tooth decay and increased calorie consumption, which leads to obesity and other chronic illnesses.")
        self.fibre_label.setToolTip("Fiber is a type of carbohydrate that the body can’t digest. Though most carbohydrates are broken down into sugar molecules called glucose, fiber cannot be broken down into sugar molecules, and instead it passes through the body undigested. Fiber helps regulate the body’s use of sugars, helping to keep hunger and blood sugar in check.")
        self.protein_label.setToolTip("Protein is an essential macronutrient. It is found throughout the body—in muscle, bone, skin, hair, and virtually every other body part or tissue. It makes up the enzymes that power many chemical reactions and the hemoglobin that carries oxygen in your blood. At least 10,000 different proteins make you what you are and keep you that way.")
        self.calcium_label.setToolTip("Calcium is a mineral most often associated with healthy bones and teeth, although it also plays an important role in blood clotting, helping muscles to contract, and regulating normal heart rhythms and nerve functions. About 99% \of the body's calcium is stored in bones, and the remaining 1% \is found in blood, muscle, and other tissues.")
        self.sodium_label.setToolTip("Sodium is an essential nutrient involved in the maintenance of normal cellular homeostasis and in the regulation of fluid and electrolyte balance and blood pressure (BP). Its role is crucial for maintaining ECF volume because of its important osmotic action and is equally important for the excitability of muscle and nerve cells and for the transport of nutrients and substrates through plasma membranes.")

        self.setStyleSheet("""
            QWidget {
                background-color: #323232;
                color: white;
            }

            QProgressBar {
                border: 2px solid grey;
                border-width: 2px;
                text-align: center;
            }

            QProgressBar::chunk {
                width: 2px;
                background-color: #de7c09;
                margin: 3px;
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
        """)
    
    def initalizeBars(self, user: User) -> None:
        self.calorie_progress.setMaximum(user.getCalNeeded())
        self.saturated_fat_progress.setMaximum(user.getSatFatNeeded())
        self.carb_progress.setMaximum(user.getCarbsNeeded())
        self.sugar_progress.setMaximum(user.getSugarNeeded())
        self.fibre_progress.setMaximum(user.getFibreNeeded())
        self.sodium_progress.setMaximum(user.getSodiumNeeded())
        self.calcium_progress.setMaximum(user.getCalciumNeeded())
        self.protein_progress.setMaximum(user.getProteinNeeded())
    
    def setBars(self, user: User) -> None:
        self.calorie_progress.setValue(int(user.nutrition["Calories"][0])+1)
        self.saturated_fat_progress.setValue(int(user.nutrition["Saturated Fat"][0])+1)
        self.carb_progress.setValue(int(user.nutrition["Carbohydrates"][0])+1)
        self.sugar_progress.setValue(int(user.nutrition["Sugars"][0])+1)
        self.fibre_progress.setValue(int(user.nutrition["Fibre"][0])+1)
        self.sodium_progress.setValue(int(user.nutrition["Sodium"][0])+1)
        self.calcium_progress.setValue(int(user.nutrition["Calcium"][0])+1)
        self.protein_progress.setValue(int(user.nutrition["Protein"][0])+1)

    def resetBars(self):
        self.calorie_progress.setValue(0)
        self.saturated_fat_progress.setValue(0)
        self.carb_progress.setValue(0)
        self.sugar_progress.setValue(0)
        self.fibre_progress.setValue(0)
        self.sodium_progress.setValue(0)
        self.calcium_progress.setValue(0)
        self.protein_progress.setValue(0)