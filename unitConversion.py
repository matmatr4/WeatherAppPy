
from PyQt5.QtWidgets import QLabel

#function to convert celsius to fahrenheit and vice versa 
def UnitConversion(self):
    if self.TemperatureUnitSel.text() == "°C":
        self.TemperatureUnit2.setText("°C")
        self.TemperatureUnitSel.setText("°F")
        self.Temperature.setText(f"{int(self.Temperature.text()) *(9/5)+32:.0f}")
        
        for i in range(7):
            self.tempLabel = self.findChild(QLabel, f"tempLabel{i}")
            self.newMinTemp = self.tempLabel.property("minTemp")
            self.newMaxTemp = self.tempLabel.property("maxTemp")
            self.tempLabel.setText((f"{(int(self.newMinTemp) * 9/5) + 32:.0f} | {(int(self.newMaxTemp) * 9/5) + 32:.0f}"))

    elif self.TemperatureUnitSel.text() == "°F":
        self.TemperatureUnit2.setText("°F")
        self.TemperatureUnitSel.setText("°C")
        self.Temperature.setText(f"{(int(self.Temperature.text()) -32)*(5/9):.0f}")

        for i in range(7):
            self.tempLabel = self.findChild(QLabel, f"tempLabel{i}")
            self.newMinTemp = self.tempLabel.property("minTemp")
            self.newMaxTemp = self.tempLabel.property("maxTemp")
            self.tempLabel.setText((f"{self.newMinTemp:.0f} | {self.newMaxTemp:.0f}"))
    