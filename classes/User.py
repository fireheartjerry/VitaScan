from PySide6.QtWidgets import QMessageBox

class User:
    def __init__(self, user_data=None) -> None:
        self.stats = {}
        if not user_data:
            self.stats["age"] = 0
            self.stats["name"] = ""
            self.stats["height"] = 0.0
            self.stats["weight"] = 0.0
            self.stats["fitness_goals"] = ""
            self.stats["gender"] = ""
            self.stats["exercise"] = ""
        else:
            self.stats["age"] = int(user_data["age"])
            self.stats["name"] = user_data["name"]
            self.stats["height"] = float(user_data["height"])
            self.stats["weight"] = float(user_data["weight"])
            self.stats["fitness_goals"] = user_data["fitness_goal"]
            self.stats["gender"] = user_data["gender"]
            self.stats["exercise"] = user_data["exercise"]

        self.nutrition = {
            "Calories": [0.0, "cal", -1.0],
            "Saturated Fat": [0.0, "g", 0.0],
            "Carbohydrates": [0.0, "g", -1.0],
            "Fibre": [0.0, "g", 0.0],
            "Sugars": [0.0, "g", 0.0],
            "Sodium": [0.0, "mg", 0.0],
            "Cholesterol": [0.0, "mg", -1.0],
            "Calcium": [0.0, "mg", 0.0],
            "Protein": [0.0, "g", -1.0]
        }
        
        self.BMR = 66.5+(13.75*self.stats["weight"])+(5.003*self.stats["height"])-(6.75*self.stats["age"])\
                   if (self.stats["gender"] == "Male") else\
                   655.1+(9.563*self.stats["weight"])+(1.850*self.stats["height"])-(4.676*self.stats["age"]) 

    def update_stats(self, update_data: dict[str, str]) -> None:
        if any(value == "" for value in update_data.values()):
            QMessageBox.critical(None, "Error", "The data given is empty.")
            return
        
        self.stats["age"] = int(update_data["age"])
        self.stats["name"] = update_data["name"]
        self.stats["height"] = float(update_data["height"])
        self.stats["weight"] = float(update_data["weight"])
        self.stats["fitness_goals"] = update_data["fitness_goal"]
        self.stats["gender"] = update_data["gender"]
        self.stats["exercise"] = update_data["exercise"]

    def update_nutrition(self, add_data) -> bool:
        new_vals = self.nutrition
        for val in new_vals:
            limit = 0
            if (val == "Calories"):
                limit = self.getCalNeeded()
            elif (val == "Saturated Fat"):
                limit = self.getSatFatNeeded()
            elif (val == "Carbohydrates"):
                limit = self.getCarbsNeeded()
            elif (val == "Fibre"):
                limit = 1000
            elif (val == "Sugars"):
                limit = self.getSugarNeeded()
            elif (val == "Sodium"):
                limit = self.getSodiumNeeded()
            elif (val == "Protein"):
                limit = self.getProteinNeeded()
            elif (val == "Calcium"):
                limit = self.getCalciumNeeded()
            else:
                limit = 90 # for cholesterol
            if (new_vals[val][0]+add_data[val][0] > limit):
                add = QMessageBox.question(None, "Daily Max Exceeded!", f"The food item you selected will overflow your daily nutritional needs for {val}! Do you still want to eat this?", QMessageBox.Yes, QMessageBox.No)
                if (add == QMessageBox.No):
                    QMessageBox.information(None, "Aborted", "Food logging action aborted by user.")
                    return False
            else:
                new_vals[val][0] += add_data[val][0]
            if (new_vals[val][2] != -1.0):
                if (add_data[val][2] >= 15 and val in ["Sugars", "Saturated Fat", "Sodium"]):
                    add = QMessageBox.question(None, "Thats alot of nutrition!", f"The food item you selected has a large (>15) percent amount for {val}, which makes the food UNHEALTHY! Do you still want to eat this?", QMessageBox.Yes, QMessageBox.No)
                    if (add == QMessageBox.No):
                        QMessageBox.information(None, "Aborted", "Food logging action aborted by user.")
                        return False
                else:
                    new_vals[val][2] += add_data[val][2] if add_data[val][2] > 0 else 0
        self.nutrition = new_vals
        return True
    
    def getCalNeeded(self) -> float:
        delta = 0
        if (self.stats["fitness_goals"] == "Weight Loss"):
            delta = -0.15
        elif (self.stats["fitness_goals"] == "Weight Gain"):
            delta = 0.15
        if (self.stats["exercise"] == "Sedentary (little or no exercise)"):
            return self.BMR*(1.2+delta)
        elif (self.stats["exercise"] == "Lightly active (light exercise/sports 1-3 days/week"):
            return self.BMR*(1.375+delta)
        elif (self.stats["exercise"] == "Moderately active (moderate exercise/sports 3-5 days/week)"):
            return self.BMR*(1.55+delta)
        elif (self.stats["exercise"] == "Very active (hard exercise/sports 6-7 days a week)"):
            return self.BMR*(1.725+delta)
        elif (self.stats["exercise"] == "Super active (very hard exercise/sports, physical job, or training)"):
            return self.BMR*(1.9+delta)

    def getProteinNeeded(self) -> int:
        return (0.225*self.getCalNeeded())//4+1

    def getCarbsNeeded(self) -> int:
        return (0.55*self.getCalNeeded())//4+1

    def getSatFatNeeded(self) -> int:
        return (0.1*self.getCalNeeded())//9+1

    def getFibreNeeded(self) -> int:
        return (self.getCalNeeded()//1000)*14

    def getSugarNeeded(self) -> int:
        return (self.getCalNeeded()//40)

    def getSodiumNeeded(self) -> int:
        if (self.stats["exercise"] == "Sedentary (little or no exercise)"):
            return int(2300*1.05)
        elif (self.stats["exercise"] == "Lightly active (light exercise/sports 1-3 days/week"):
            return int(2300*1.15)
        elif (self.stats["exercise"] == "Moderately active (moderate exercise/sports 3-5 days/week)"):
            return int(2300*1.25)
        elif (self.stats["exercise"] == "Very active (hard exercise/sports 6-7 days a week)"):
            return int(2300*1.35)
        elif (self.stats["exercise"] == "Super active (very hard exercise/sports, physical job, or training)"):
            return int(2300*1.4)
    
    def getCalciumNeeded(self) -> int:
        if (self.stats["age"] < 1):
            return 260
        elif (self.stats["age"] < 3):
            return 700
        elif (self.stats["age"] < 8):
            return 1000
        elif (self.stats["age"] < 18):
            return 1300
        elif (self.stats["age"] < 50):
            return 1000
        elif (self.stats["age"] < 70):
            return 1000 if self.stats["gender"] == "Male" else 1200
        else:
            return 1200