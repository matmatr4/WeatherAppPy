
from datetime import datetime

#function to turn any date into its corresponding weekday 
def dateToWeekday(date):
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
def IconManagement(weatherID):
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
