import sys
import requests 
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class WeatherApp (QMainWindow):
    def __init__(self):
        super().__init__()

        self.cityVar = "City"

        self.setWindowTitle("Weather App")
        self.setGeometry(100,100,600,800)

        self.backgroundPic = QPixmap("pexels-photo-1571730.jpeg")
        self.backgroundLabel = QLabel(self)
        self.backgroundLabel.setGeometry(0,0,600,800)
        self.backgroundLabel.setPixmap(self.backgroundPic)
        self.backgroundLabel.setScaledContents(True)
        self.WeatherPanel = QLabel(self)
        self.WeatherPanel.setGeometry(0,0,600,800)
        self.WeatherPanel.setStyleSheet("background-color: rgba(0, 0, 0, 90)")

        self.WelcomeLabel = QLabel("Welcome to Weather App!", self)
        self.WelcomeLabel.setGeometry(0,0,600,60)
        self.WelcomeLabel.setStyleSheet("color: white;"
                                        "font-size: 35px;"
                                        "font-weight: bold;")
        self.WelcomeLabel.setAlignment(Qt.AlignCenter)

        self.CitySearch = QLineEdit(self)
        self.CitySearch.setGeometry(30,70,370,30)
        self.CitySearch.setStyleSheet("font-size: 15px;"
                                      "background-color: white;"
                                      "border-radius: 15px;"
                                      "color: #2a2a2a")
        self.CitySearch.setPlaceholderText("Enter your city and country (e.g. London, UK)")

        self.SearchButton = QPushButton("Search", self)
        self.SearchButton.setGeometry(420,67,150,36)
        self.SearchButton.setStyleSheet("""
                                        QPushButton {
                                            font-size: 20px;
                                            background-color: grey;
                                            border-radius: 15px; 
                                        }
                                        QPushButton:hover {
                                            background-color: #bdbdbd;
                                        }                       
                                        """)
        self.SearchButton.clicked.connect(self.getWeather)
        

        #UI part 2
        self.WeatherPanel = QLabel(self)
        self.WeatherPanel.setGeometry(20,120,560,660)
        self.WeatherPanel.setStyleSheet("background-color: rgba(0, 0, 0, 90)")

        self.City = QLabel(self.cityVar, self)
        self.City.setGeometry(20,150,560,80)
        self.City.setStyleSheet("font-size: 70px;"
                                "color: white;"
                                "background-color: transparent;"
                                "font-weight: bold;")
        self.City.setAlignment(Qt.AlignCenter)
        
        self.Temperature = QLabel("15", self)
        self.Temperature.setGeometry(260,240,200,200)
        self.Temperature.setStyleSheet("font-size: 140px;"
                                       "font-weight: bold;")
        self.Temperature.setAlignment(Qt.AlignCenter)

        self.TemperatureUnitSel = QPushButton("°C", self)
        self.TemperatureUnitSel.setGeometry(440,290,60,50)
        self.TemperatureUnitSel.setStyleSheet("""
                                            QPushButton {
                                                font-size: 30px;
                                                border: none;
                                                color: white; 
                                            }
                                            """)

        self.TempSlash = QLabel("/", self)
        self.TempSlash.setGeometry(505,290,10,50)
        self.TempSlash.setStyleSheet("font-size: 30px;"
                                     "color: grey;")

        self.TemperatureUnit2 = QPushButton("°F", self)
        self.TemperatureUnit2.setGeometry(510,290,60,50)
        self.TemperatureUnit2.setStyleSheet("""
                                            QPushButton {
                                                font-size: 30px;
                                                border: none;
                                                color: grey; 
                                            }
                                            QPushButton:hover {
                                                color: #bdbdbd;
                                            }
                                            """)

        self.WeatherIcon = QLabel("🌤️", self)
        self.WeatherIcon.setGeometry(80,240,200,200)
        self.WeatherIcon.setStyleSheet("font-size: 190px;"
                                       "font-weight: bold;")
        self.WeatherIcon.setAlignment(Qt.AlignCenter)

        self.Rain = QLabel("Precipitation: 100%", self)
        self.Rain.setGeometry(80,450,150,70)
        self.Rain.setStyleSheet("font-size: 15px;"
                                "font-weight: bold;")

        self.Humidity = QLabel("Humidity: 100%", self)
        self.Humidity.setGeometry(255,450,120,70)
        self.Humidity.setStyleSheet("font-size: 15px;"
                                    "font-weight: bold;")

        self.Windspeed = QLabel("Wind Speed: 5km/h", self)
        self.Windspeed.setGeometry(410,450,150,70)
        self.Windspeed.setStyleSheet("font-size: 15px;"
                                     "font-weight: bold;")


    def initUI(self):
        pass

    def getWeather(self):
        
        personalApiKey = "937SX7U7TTKKHLWMKQQTMVC2G"
        cityIn = self.CitySearch.text()
        url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{cityIn}?key={personalApiKey}"
        
        
        response = requests.get(url)
        data = response.json()

        #print(data['resolvedAddress'])
        #print(data['days'][0]['temp'])

        if response.status_code == 200:
            print(response.status_code)
            self.displayWeather(data)
        else:
            print("error") 

    def displayError(self):
        pass

    def displayWeather(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())