from abc import ABC, abstractmethod
import urllib.request
import urllib.error
import json


class WebAPI(ABC):
    """Handles basic functions to handle API content."""

    def __init__(self):
        self.apikey = ""

    def _download_url(self, url: str) -> dict:
        """Downloads an API's url and loads its data into the object."""
        response = None

        try:
            response = urllib.request.urlopen(url)
            json_results = response.read()
            obj = json.loads(json_results)

        except urllib.error.HTTPError as e:
            if e.code == 401:
                print("Unauthorized to access.")
            elif e.code == (404 or 503):
                print("Remote API unavailable.")
            else:
                print("Failed to download contents of URL")
                print("Status code: {}".format(e.code))
        except ValueError:
            print("Invalid JSON response format.")
        except urllib.error.URLError as e:
            print(e.reason)
            print("Loss of internet connection.")

        finally:
            if response is not None:
                response.close()

        return obj

    def set_apikey(self, apikey: str) -> None:
        """
        Sets the apikey required to make requests to a web API.
        :param apikey: The apikey supplied by the API service
        """
        self.apikey = apikey
        return self.apikey

    @abstractmethod
    def load_data(self):
        """Abstract method to extract data from the JSON object."""


class OpenWeather(WebAPI):
    """Inherits from the WebAPI class and handles data from the OpenWeather API."""

    def __init__(self, zipcode="", ccode="US", apikey=None):
        self.zipcode = zipcode
        self.ccode = ccode
        self.apikey = apikey
        self.temperature = ""
        self.high_temperature = ""
        self.low_temperature = ""
        self.longitude = ""
        self.latitude = ""
        self.description = ""
        self.humidity = ""
        self.city = ""
        self.sunset = ""

    def load_data(self) -> None:
        """
        Calls the web api using the required values and stores the response in
        class data attributes.
        """
        zipcode = self.zipcode
        ccode = self.ccode
        url = f"http://api.openweathermap.org/data/2.5/weather?units=imperial&zip={zipcode},{ccode}&appid={self.apikey}"
        obj = self._download_url(url)

        self.temperature = obj["main"]["temp"]
        self.high_temperature = obj["main"]["temp_max"]
        self.low_temperature = obj["main"]["temp_min"]
        self.longitude = obj["coord"]["lon"]
        self.latitude = obj["coord"]["lat"]
        self.description = obj["weather"][0]["description"]
        self.humidity = obj["main"]["humidity"]
        self.sea_level = obj["main"]["sea_level"]
        self.city = obj["name"]
        self.sunset = obj["sys"]["sunset"]
        return obj


def pull_data(zip, key):
    weather = OpenWeather(zipcode=zip, apikey=key)
    weather.load_data()
    return_obj = {}
    return_obj["city"] = weather.city
    return_obj["temp_now"] = weather.temperature
    return_obj["temp_min"] = weather.low_temperature
    return_obj["temp_max"] = weather.high_temperature
    return_obj["desc"] = weather.description
    return_obj["sea_level"] = weather.sea_level
    return_obj["humidity"] = weather.humidity

    return return_obj
