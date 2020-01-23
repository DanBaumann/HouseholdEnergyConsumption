import requests
import json
from dotenv import load_dotenv
import os
import numpy as np
load_dotenv()


class WeatherGetter(object):
    
    def __init__(self):
        self.secret_key = os.getenv("DARKSKY_KEY")
        self.sceaux_lat = "48.8405"
        self.sceaux_long = "2.3238"
        self.url_base = "https://api.darksky.net/forecast"
        self.exclude = "latitude,longitude,timezone,offset,daily,hourly,flags,minutely,alerts"
        
    def format_datetime(self, datetime_string):
        """
        Arguments:
        datetime_string: a string in datetime format
        """
        year = datetime_string[:4]
        month = datetime_string[5:7]
        day = datetime_string[8:10]
        hour = datetime_string[11:]
        
        return year, month, day, hour
        
    def get_weather_for_hour(self, datetime_string, verbose=True):
        year, month, day, hour = self.format_datetime(datetime_string)
        datetime = "{}-{}-{}T{}".format(year, month, day, hour)
        full_url = "{}/{}/{},{},{}?exclude={}".format(self.url_base, self.secret_key, 
                                                     self.sceaux_lat, self.sceaux_long, 
                                                     datetime, self.exclude)
        response = requests.get(full_url)
        return response
#         if response.status_code == 200:
#             if verbose:
#                 print(response.status_code)
#             return response
#         else:
#             raise ValueError("Error getting data from DarkSky API: Response Code {}".
#                              format(response.status_code))
            
    def current_temperature(self, datetime_string):
        result = self.get_weather_for_hour(datetime_string)
        result = result.json()
        try:
            temp_in_farenheit = result['currently']['temperature']
            cel = (temp_in_farenheit-32)*(5/9)
            temp = "%.2f" % cel
        except:
            temp = np.nan
            
        return temp