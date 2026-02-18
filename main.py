import sys
import requests 
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QMainWindow, QMessageBox, QWidget, QFrame
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from datetime import datetime, date

class WeatherApp (QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Weather App")
        self.setGeometry(100,100,600,750)

        self.backgroundPic = QPixmap("pexels-photo-1571730.jpeg")
        self.backgroundLabel = QLabel(self)
        
        self.WeatherPanel = QLabel(self)
        
        self.WelcomeLabel = QLabel("Welcome to Weather App!", self)
        self.CitySearch = QLineEdit(self)
        self.SearchButton = QPushButton("Search", self)
        
        #UI part 2
        self.WeatherPanel2 = QLabel(self)
        
        self.City = QLabel("City", self)
        self.Temperature = QLabel("150", self)
        self.TemperatureUnitSel = QPushButton("°C", self)
        self.TempSlash = QLabel("/", self)
        self.TemperatureUnit2 = QPushButton("°F", self)
        self.WeatherIcon = QLabel("", self)
        self.DefaultPixmap = QPixmap("partly-cloudy-day.png")
        self.WeatherDesc = QLabel("Partially cloudy", self)
        
        self.Rain = QLabel("Precipitation: 100%", self)
        self.Humidity = QLabel("Humidity: 100%", self)
        self.Windspeed = QLabel("Wind Speed: 5km/h", self)
        
        self.ErrorMsgBox = QMessageBox(self)
        self.ErrorMsgBox.setIcon(QMessageBox.Warning)

        self.initUI1()
        self.initUI2()


    #all of the details regarding UI design of the main title, search button and text field, also the background
    def initUI1(self):
        self.backgroundLabel.setGeometry(0,0,600,800)
        self.backgroundLabel.setPixmap(self.backgroundPic)
        self.backgroundLabel.setScaledContents(True)

        self.WeatherPanel.setGeometry(0,0,600,800)
        self.WeatherPanel.setStyleSheet("background-color: rgba(0, 0, 0, 90)")

        self.WelcomeLabel.setGeometry(0,0,600,60)
        self.WelcomeLabel.setStyleSheet("color: white;"
                                        "font-size: 35px;"
                                        "font-weight: bold;")
        self.WelcomeLabel.setAlignment(Qt.AlignCenter)

        self.CitySearch.setGeometry(30,70,370,30)
        self.CitySearch.setStyleSheet("font-size: 15px;"
                                      "background-color: white;"
                                      "border-radius: 15px;"
                                      "color: #2a2a2a")
        self.CitySearch.setPlaceholderText("Enter your city and country (e.g. London, UK)")

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


    #characteristics of the UI responsible for displaying weather details of a place at the current time
    def initUI2(self):
        self.WeatherPanel2.setGeometry(20,120,560,610)
        self.WeatherPanel2.setStyleSheet("background-color: rgba(0, 0, 0, 90)")

        self.City.setGeometry(20,150,560,80)
        self.City.setStyleSheet("font-size: 70px;"
                                "color: white;"
                                "background-color: transparent;"
                                "font-weight: bold;")
        self.City.setAlignment(Qt.AlignCenter)

        self.Temperature.setGeometry(260,240,180,200)
        self.Temperature.setStyleSheet("font-size: 100px;"
                                       "font-weight: bold;")
        self.Temperature.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        self.TemperatureUnitSel.setGeometry(440,290,60,50)
        self.TemperatureUnitSel.setStyleSheet("""
                                            QPushButton {
                                                font-size: 30px;
                                                border: none;
                                                color: white; 
                                            }
                                            """)
        
        self.TempSlash.setGeometry(505,290,10,50)
        self.TempSlash.setStyleSheet("font-size: 30px;"
                                     "color: grey;")
        
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
        self.TemperatureUnit2.clicked.connect(self.UnitConversion)

        self.WeatherIcon.setPixmap(self.DefaultPixmap)
        self.WeatherIcon.setScaledContents(True)
        self.WeatherIcon.setGeometry(70,250,170,170)
        self.WeatherIcon.setStyleSheet("font-size: 190px;"
                                       "font-weight: bold;")
        self.WeatherIcon.setAlignment(Qt.AlignCenter)

        self.WeatherDesc.setGeometry(50,420,200,50)
        self.WeatherDesc.setStyleSheet("font-size: 12px;"
                                       "font-weight: bold")
        
        self.Rain.setGeometry(80,450,150,70)
        self.Rain.setStyleSheet("font-size: 15px;"
                                "font-weight: bold;")
        
        self.Humidity.setGeometry(255,450,120,70)
        self.Humidity.setStyleSheet("font-size: 15px;"
                                    "font-weight: bold;")
        
        self.Windspeed.setGeometry(410,450,150,70)
        self.Windspeed.setStyleSheet("font-size: 15px;"
                                     "font-weight: bold;")


    #function to retrieve weather data from the API
    def getWeather(self):

        personalApiKey = "937SX7U7TTKKHLWMKQQTMVC2G"
        cityIn = self.CitySearch.text()
        self.CitySearch.clear()
        url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{cityIn}?key={personalApiKey}&include=fcst&elements=datetime,temp,precip,windspeed,humidity,icon,tempmax,tempmin,conditions&unitGroup=metric"
        
        self.TemperatureUnit2.setText("°F")
        self.TemperatureUnitSel.setText("°C")

        try:
            response = requests.get(url)
            response.raise_for_status() #so that an error is raised if response is bad
            data = response.json()
            self.displayWeather(data)
            self.displayWeeklyWeather(data)
        
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


    #displays an error message for the user after an error occurs
    def displayError(self, ErrorName, ErrorTitle):
        self.ErrorMsgBox.setText(ErrorName)
        self.ErrorMsgBox.setWindowTitle(ErrorTitle)
        self.ErrorMsgBox.exec_()


    #function to retrieve todays weather data and display it in UI components from the retrieved .json 
    def displayWeather(self, data):
        self.City.setText((data['resolvedAddress'].split(",")[0]).capitalize())
        self.Temperature.setText(str(int(round(data['days'][0]['temp'], 0))))
        self.Rain.setText(f"Precipitation: {(data['days'][0]['precip']):.0f}%")
        self.Humidity.setText(f"Humidity: {(data['days'][0]['humidity']):.0f}%")
        self.Windspeed.setText(f"Wind Speed: {(data['days'][0]['humidity']):.0f}km/h")
        self.WeatherDesc.setText((data['days'][0]['conditions']))
        
        #setting weather icons
        self.pixmapIcon = QPixmap(self.IconManagement(str(data['days'][0]['icon'])))
        self.WeatherIcon.setPixmap(self.pixmapIcon)
        self.WeatherIcon.setScaledContents(True)


    #function to display the upcoming week's weather in the widget at the bottom of the window
    def displayWeeklyWeather(self, data):
        
        #preventing overlay issues, by checking if a widget object already exists, and if so, deleting it
        if self.findChild(QWidget, 'weekWidget') is not None:
                self.findChild(QWidget, 'weekWidget').deleteLater()
            
        self.weekLayout = QHBoxLayout()
        self.weekLayout.setAlignment(Qt.AlignCenter)

        self.weekWidget = QWidget(self)
        self.weekWidget.setGeometry(30,520,540,200)
        self.weekWidget.setStyleSheet("background-color: rgba(0, 0, 0, 0);"
                                      "")

        for i in range(7):
            tempMin = f"{data['days'][i]['tempmin']:.0f}"
            tempMax = f"{data['days'][i]['tempmax']:.0f}"
            pixmapIcon = QPixmap(self.IconManagement(str(data['days'][i]['icon']))) 
            weekday = self.dateToWeekday(data['days'][i]['datetime'])

            dayBlock = self.weeklyWeatherBlock(tempMin, tempMax, pixmapIcon, weekday, i)
            self.weekLayout.addWidget(dayBlock)
        
        self.weekWidget.setLayout(self.weekLayout)
        self.weekWidget.show()

        #this will be used to find the object with find name (line 236), so in case such object already exists it can be deleted
        self.weekWidget.setObjectName("weekWidget")

    
    #function that adds a block for each day of the upcoming week's onto the upcoming week weather widget (weekWidget)
    def weeklyWeatherBlock(self, tempMin, tempMax, pixmapIcon, weekday, index):
        
        self.dayBlock = QFrame(self)
        self.dayBlock.setFixedSize(70,150)
        self.dayBlock.setStyleSheet("background-color: rgba(0, 0, 0, 90);"
                                    "border-radius: 10px;")

        self.dayBlockLayout = QVBoxLayout()
        self.dayBlockLayout.setAlignment(Qt.AlignCenter)

        self.weekdayLabel = QLabel(weekday)
        self.weekdayLabel.setAlignment(Qt.AlignCenter)
        self.weekdayLabel.setStyleSheet("font-weight: bold;"
                                        "font-size: 18px;"
                                        "background-color: transparent;")
        self.dayBlockLayout.addWidget(self.weekdayLabel)

        self.iconLabel = QLabel()
        self.iconLabel.setPixmap(pixmapIcon)
        self.iconLabel.setScaledContents(True)
        self.iconLabel.setAlignment(Qt.AlignCenter)
        self.iconLabel.setStyleSheet("background-color: transparent;")
        self.dayBlockLayout.addWidget(self.iconLabel)

        self.tempLabel = QLabel(f"{tempMin} | {tempMax}")
        self.tempLabel.setObjectName(f"tempLabel{index}")
        self.tempLabel.setProperty("minTemp", int(tempMin))
        self.tempLabel.setProperty("maxTemp", int(tempMax))
        self.tempLabel.setAlignment(Qt.AlignCenter)
        self.tempLabel.setStyleSheet("font-size: 12px;"
                                     "background-color: transparent;")
        self.dayBlockLayout.addWidget(self.tempLabel)


        self.dayBlock.setLayout(self.dayBlockLayout)
        return self.dayBlock
    

    #function to turn any date into its corresponding weekday 
    def dateToWeekday(self, date):
        match datetime.strptime(date, "%Y-%m-%d").weekday():
            case 0:
                return "Mon"
            case 1:
                return "Tue"
            case 2:
                return "Wed"
            case 3:
                return "Thu"
            case 4:
                return "Fri"
            case 5: 
                return "Sat"
            case 6:
                return "Sun"
    

    #function to display particular weather icons
    def IconManagement(self, weatherID):
        match weatherID:
            case "snow":
                return "icons/snow.png"
            case "rain":
                return "icons/rain.png"
            case "fog":
                return "icons/fog.png"
            case "wind":
                return "icons/wind.png"
            case "cloudy":
                return "icons/cloudy.png"
            case "partly-cloudy-day":
                return "icons/partly-cloudy-day.png"
            case "partly-cloudy-night":
                return "icons/partly-cloudy-night.png"
            case "clear-day":
                return "icons/clear-day.png"
            case "clear-night":
                return "icons/clear-night.png"
    

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
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())