import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from GUI import initUI


class WeatherApp (QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Weather App")
        self.setGeometry(100,100,600,750)

        initUI(self)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())