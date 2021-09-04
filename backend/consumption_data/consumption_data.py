import json

import pandas as pd
import requests


def get_consumption_data(device_id: str, start_date_time: str, end_date_time: str) -> pd.DataFrame:
    url = f"https://power-hack.azurewebsites.net/Volumes?Start={start_date_time}&End={end_date_time}&MeteringpointId={device_id}"
    url_data = requests.get(url).content

    real_data = {
        "ds": [],
        "y": []
    }
    data = json.loads(url_data)
    for data_point in data:
        real_data["ds"].append(data_point["measurementTime"].split("+")[0])
        real_data["y"].append(data_point["value"])

    df = pd.DataFrame(data=real_data)
    df["ds"] = pd.to_datetime(df["ds"])

    return df


def get_consumption_all_devices(start_date: str, end_date: str):

    url = f"https://power-hack.azurewebsites.net/Meteringpoint"
    url_data = requests.get(url).content

    data = json.loads(url_data)
    real_data = []
    i = 0
    for househould in data:
        df = get_consumption_data(househould['meteringpointId'], start_date, end_date)
        real_data.append(df)
        i += 1
        if i >= 3:
            break
    return real_data