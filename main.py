import sys
import requests 
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMainWindow, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class WeatherApp (QMainWindow):
    def __init__(self):
        super().__init__()

        self.cityDisp = "City"

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

        self.City = QLabel(self.cityDisp, self)
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

        self.ErrorMsgBox = QMessageBox(self)
        self.ErrorMsgBox.setIcon(QMessageBox.Warning)


    def initUI(self):
        pass

    def getWeather(self):
        
        personalApiKey = "937SX7U7TTKKHLWMKQQTMVC2G"
        cityIn = self.CitySearch.text()
        url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{cityIn}?key={personalApiKey}"
        
        try:
            response = requests.get(url)
            response.raise_for_status() #so that an error is raised if response is bad
            data = response.json()
            self.displayWeather(data)
        
        #catches errors with API response received
        except requests.exceptions.HTTPError:
            match response.status_code:
                case 400:
                    print("400 BAD REQUEST: Invalid request format or parameters")
                    self.displayError("400 BAD REQUEST: Invalid request format or parameters", "400 Error")
                case 401:
                    print("401 UNAUTHORIZED: API key or account problem.")
                    self.displayError("401 UNAUTHORIZED: API key or account problem", "401 Error")
                case 404: 
                    print("404 NOT FOUND: Endpoint does not exist.")
                    self.displayError("404 NOT FOUND: Endpoint does not exist", "404 Error")
                case 429:
                    print("429 TOO MANY REQUESTS: Rate limit exceeded.")
                    self.displayError("429 TOO MANY REQUESTS: Rate limit exceeded", "429 Error")
                case 500:
                    print("500 INTERNAL SERVER ERROR: Server problem.")
                    self.displayError("500 INTERNAL SERVER ERROR: Server problem", "500 Error")
                case _:
                    print(f"HTTP error occurred: {response.status_code}")
                    self.displayError("HTTP error occurred: {response.status_code}", "HTTP Error")

        #catches network errors
        except requests.exceptions.ConnectionError:
            print("Network or connection error")
            self.displayError("Network or connection error", "Network/Connection Error")

        #catches timeout errors
        except requests.exceptions.Timeout:
            print("Request time out")
            self.displayError("Request time out", "Request Time Out Error")

        #catches URL errors
        except requests.exceptions.TooManyRedirects:
            print("URL error, too many or wrong redirects")
            self.displayError("URL error, too many or wrong redirects", "URL Error")

        #catches any other errors
        except requests.exceptions.RequestException as e:
            print(f"Other error occurred:{e}")
            self.displayError(f"Other error occurred:{e}", "Error")
           
        #print(data['resolvedAddress'])
        #print(data['days'][0]['temp'])

    #displays an error message for the user after an error occurs
    def displayError(self, ErrorName, ErrorTitle):
        self.ErrorMsgBox.setText(ErrorName)
        self.ErrorMsgBox.setWindowTitle(ErrorTitle)
        self.ErrorMsgBox.exec_()

    def displayWeather(self, data):
        print(data)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())