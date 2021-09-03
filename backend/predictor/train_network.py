import json

import pandas as pd
import requests
from prophet import Prophet


def get_data():
    url = "https://power-hack.azurewebsites.net/Volumes?Start=2019-09-03T18%3A50%3A21.114Z&End=2020-09-03T18%3A50%3A21.114Z&MeteringpointId=707057500100175148"
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

    return df


def fit_model_to_data():
    """Fits the prophet model to the given historical data"""
    data = get_data()
    m = Prophet(changepoint_prior_scale=0.01)
    m.fit(data)
    return m


def get_prediction(model: Prophet) -> pd.DataFrame:
    future = model.make_future_dataframe(periods=300, freq="H")
    return model.predict(future)
