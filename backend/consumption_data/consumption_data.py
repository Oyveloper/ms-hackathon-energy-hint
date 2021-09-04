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
