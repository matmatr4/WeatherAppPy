import sys
import requests 
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class WeatherApp (QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Weather App")
        self.setGeometry(100,100,600,700)

        self.WelcomeLabel = QLabel("Welcome to Weather App!", self)
        self.WelcomeLabel.setGeometry(0,0,600,60)
        self.WelcomeLabel.setStyleSheet("color: white;"
                                        "font-size: 35px;"
                                        "font-weight: bold;")
        self.WelcomeLabel.setAlignment(Qt.AlignCenter)

        self.CitySearch = QLineEdit(self)
        self.CitySearch.setGeometry(30,70,340,30)
        self.CitySearch.setStyleSheet("font-size: 20px;")
        self.CitySearch.setPlaceholderText("Enter your city")

        self.SearchButton = QPushButton("Search", self)
        self.SearchButton.setGeometry(400,67,170,36)
        self.SearchButton.setStyleSheet("font-size: 20px;")

    def initUI():
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())