
import requests

#for secure import of API key
from dotenv import load_dotenv
import os

from error import displayError
from GUI import displayWeather, displayWeeklyWeather

#function to retrieve weather data from the API
def getWeather(self):

    load_dotenv("resources/.env") #loads the .env file, so that the API key can be retrieved from it
    personalApiKey = os.getenv("API_KEY") #retrieving API key from .env file, so that it is not exposed in the code
    cityIn = self.CitySearch.text()
    self.CitySearch.clear()
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{cityIn}?key={personalApiKey}&include=fcst&elements=datetime,temp,precip,windspeed,humidity,icon,tempmax,tempmin,conditions&unitGroup=metric"
    
    self.TemperatureUnit2.setText("°F")
    self.TemperatureUnitSel.setText("°C")

    try:
        response = requests.get(url)
        response.raise_for_status() #so that an error is raised if response is bad
        data = response.json()
        displayWeather(self, data)
        displayWeeklyWeather(self, data)
    
    #catches errors with API response received
    except requests.exceptions.HTTPError:
        match response.status_code:
            case 400:
                print("400 BAD REQUEST: Invalid request format or parameters")
                displayError(self, "400 BAD REQUEST: Invalid request format or parameters", "400 Error")
            case 401:
                print("401 UNAUTHORIZED: API key or account problem.")
                displayError(self, "401 UNAUTHORIZED: API key or account problem", "401 Error")
            case 404: 
                print("404 NOT FOUND: Endpoint does not exist.")
                displayError(self, "404 NOT FOUND: Endpoint does not exist", "404 Error")
            case 429:
                print("429 TOO MANY REQUESTS: Rate limit exceeded.")
                displayError(self, "429 TOO MANY REQUESTS: Rate limit exceeded", "429 Error")
            case 500:
                print("500 INTERNAL SERVER ERROR: Server problem.")
                displayError(self, "500 INTERNAL SERVER ERROR: Server problem", "500 Error")
            case _:
                print(f"HTTP error occurred: {response.status_code}")
                displayError(self, f"HTTP error occurred: {response.status_code}", "HTTP Error")

    #catches network errors
    except requests.exceptions.ConnectionError:
        print("Network or connection error")
        displayError(self, "Network or connection error", "Network/Connection Error")

    #catches timeout errors
    except requests.exceptions.Timeout:
        print("Request time out")
        displayError(self, "Request time out", "Request Time Out Error")

    #catches URL errors
    except requests.exceptions.TooManyRedirects:
        print("URL error, too many or wrong redirects")
        displayError(self, "URL error, too many or wrong redirects", "URL Error")

    #catches any other errors
    except requests.exceptions.RequestException as e:
        print(f"Other error occurred:{e}")
        displayError(self, f"Other error occurred:{e}", "Error")

