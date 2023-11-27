from datetime import datetime,timedelta
import requests
import numpy as np
import pandas as pd


API_KEY = ""


def get_data(location):
    

    current_date = datetime.now()
    till_date = current_date + timedelta(days=2)

    date1 = current_date.strftime("%Y-%m-%d")
    date2 = till_date.strftime("%Y-%m-%d")

    location = str(location)
    
    k = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"+location+"/"+date1+"/"+date2+"?unitGroup=metric&include=days&key="+API_KEY+"&contentType=json"
    x = requests.get(k).json()['days']


    data = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    #'tempmax','temp','humidity','precip','precipprob','precipcover','snowdepth','windspeed','cloudcover'


    for i in x:
        data[0] += i['tempmax']
        data[1] += i['temp']
        data[2] += i['humidity']
        data[3] += i['precip']
        data[4] += i['precipprob']
        data[5] += i['precipcover']
        data[6] += i['snowdepth']
        data[7] += i['windspeed']
        data[8] += i['cloudcover']

           

    data_arr = np.array(data)

    data_arr = data_arr / 3
    data_arr = data_arr.reshape(1,-1)

    result = pd.DataFrame(data_arr, columns=['tempmax','temp','humidity','precip','precipprob','precipcover','snowdepth','windspeed','cloudcover'])

    return result

