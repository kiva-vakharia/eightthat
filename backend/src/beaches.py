import pysurfline
import pandas as pd
from datetime import datetime, timedelta

beaches = {
    'The Wedge': '5842041f4e65fad6a770882b', 
    'Corona Del Mar': '5842041f4e65fad6a77088f3', 
    'Newport Point': '5842041f4e65fad6a77088f2', 
    'Blackies': '584204204e65fad6a7709115',
    'Newport Lower Jetties': '5842041f4e65fad6a770882a',
    'Crystal Cove': '5842041f4e65fad6a7708f21',
    'Newport Upper Jetties': '5842041f4e65fad6a7708e54',
    'River Jetties': '5842041f4e65fad6a77088ee',
    'Crescent Bay': '640a3f7ae92030a2449dd23c',
    'Rockpile': '5842041f4e65fad6a77088e3',
    'Huntington State Beach': '584204204e65fad6a770998c',
    'Thalia Street': '5842041f4e65fad6a77088de',
    'Brooks Street': '5842041f4e65fad6a77088dd',
    'Huntington St.': '58bdebbc82d034001252e3d2',
    'Agate Street': '640a3f794eb37508e5945334',
    'Huntington Beach Pier Southside': '5842041f4e65fad6a77088ed',
    'North HB': '5842041f4e65fad6a77088ea',
    'Aliso Creek': '5842041f4e65fad6a77088dc',
    'HB Cliffs': '640a3f7c606c45fdf1b09880'
     }

zipcodes = {
    'The Wedge': '92663', 
    'Corona Del Mar': '92625', 
    'Newport Point': '92625', 
    'Blackies': '92663',
    'Newport Lower Jetties': '92663',
    'Crystal Cove': '92651',
    'Newport Upper Jetties': '92663',
    'River Jetties': '92646',
    'Crescent Bay': '92651',
    'Rockpile': '92651',
    'Huntington State Beach': '92646',
    'Thalia Street': '92651',
    'Brooks Street': '92651',
    'Huntington St.': '92648',
    'Agate Street': '92651',
    'Huntington Beach Pier Southside': '92648',
    'North HB': '92615',
    'Aliso Creek': '92651',
    'HB Cliffs': '92646'
     }


def get_zip(beach_name):
    return zipcodes[beach_name]


def get_beach_id(name_beach):
    if name_beach in beaches:
        return beaches[name_beach]
    else:
        return None
    

def list_beaches():
    all_beaches = list(beaches.keys())
    return all_beaches

def timestamp_power_data(spot_forecast):
    data = {}
    timestamps = []
    power = []
    
    for wave in spot_forecast.waves:
        timestamps.append(str(wave.timestamp)[5:-2])
        power.append(wave.power)
    
    data["timestamps"] = timestamps
    data["power"] = power
    dataframe = pd.DataFrame(data)
    dataframe['timestamps'] = pd.to_datetime(dataframe['timestamps'])
    return dataframe


def get_power_range_for_time(df, user_time: str):
    user_time = pd.to_datetime(user_time)
    df['time_difference'] = abs(df['timestamps'] - user_time)

    exact_match = df[df['timestamps'] == user_time]
    if not exact_match.empty:
        power_value = float(exact_match.iloc[0]['power'])
        return power_value, None

    closest_points = df.nsmallest(2, 'time_difference').sort_values(by='timestamps')
    power_range = closest_points['power'].tolist()
    
    return power_range[0], power_range[1]


def return_power(name_beach: str, user_time: str):
    """
    time should be in format: 2024-11-02 13:00:00
    """
    beach_id = get_beach_id(name_beach)
    spot_forecasts = pysurfline.get_spot_forecasts(spotId=beach_id, days=1)
    max_power = 0

    for wave in spot_forecasts.waves:
        if wave.power > max_power:
            max_power = wave.power
    dataframe = timestamp_power_data(spot_forecasts)
    lower_power, upper_power = get_power_range_for_time(dataframe, user_time)

    return lower_power, upper_power


def beach_ranking(power):
    """
    Returns 0 if beginner, 1 for intermediate, 2 for advanced.
    """

    if power <= 18.5:
        return 'Beginner'
    elif 18.5 < power <= 24.5:
        return 'Gnarly'
    else:
        return 'Firing'
    


def rank_beach(beach_name: str, user_time_input):
    power1, power2 = return_power(beach_name, user_time_input)
    if not power2:
        power = power1
    else:
        power = (power1 + power2) / 2
    print(power)

    level = beach_ranking(power)
    return level