import re
VALUES = {"saturated", "carbohydrate", "fibre", "sugars", "sodium", "cholesterol", "calcium", "protein"}

def convert(s: str) -> str:
    if (s == "saturated"): return "Saturated Fat"
    elif (s == "carbohydrate"): return "Carbohydrates"
    elif (s == "fibre"): return "Fibre"
    elif (s == "sugars"): return "Sugars"
    elif (s == "sodium"): return "Sodium"
    elif (s == "cholesterol"): return "Cholesterol"
    elif (s == "calcium"): return "Calcium"
    elif (s == "protein"): return "Protein"

def process(ocr_data: list[str]) -> dict[str, list[float, float]]:
    data = [re.sub(r'[^a-zA-Z0-9%]', '', s) for s in ocr_data]
    data = [x.lower() for x in data if x.strip()]
    data = data[data.index("calories"):]
    final_data = {}
    final_data["Calories"] = [float(data[1]), "cal", -1.0]
    i = 0
    for val in VALUES:
        i = data.index(val)+1
        add_data = []
        while (i < len(data) and data[i] != val):
            if (data[i].isdigit()):
                add_data.append(float(data[i])*0.1 if (data[i][0] == '0' and len(data[i]) > 1) else float(data[i]))
                add_data.append("g" if data[i+1] == 'g' else "mg")
                i += 1
                percent_data = data[i+1]
                if (percent_data.isdigit()):
                    add_data.append(float(percent_data))
                elif (percent_data[:-1].isdigit() and percent_data[-1] == '%'):
                    add_data.append(float(percent_data[:-1]))
                break
            elif (data[i][-1] == 'g' and data[i][:-1].isdigit()) or (data[i][-2:] == "mg" and data[i][:-2].isdigit()):
                amt = data[i][:-1] if data[i][-1] == 'g' else data[i][:-2]
                add_data.append(float(amt)*0.1 if (amt[0] == '0') else float(amt))
                add_data.append("g" if amt[-1] == 'g' else "mg")
                i += 1
                percent_data = data[i+1]
                if (percent_data.isdigit()):
                    add_data.append(float(percent_data))
                elif (percent_data[:-1].isdigit() and percent_data[-1] == '%'):
                    add_data.append(float(percent_data[:-1]))
                break
            i += 1
        if (len(add_data) == 2):
            add_data.append(-1.0)
        if (not add_data):
            add_data = [0.0, "", -1.0]
        final_data[convert(val)] = add_data
    return final_data