import os
from datetime import datetime
from functools import cache

import numpy as np
from tensorflow.keras.models import load_model

from nilm.applience_split import ApplienceSplit


@cache
def get_applience_consumption(fromDate: datetime, toDate: datetime) -> ApplienceSplit:
    # TODO: Replace with actual 6-second usage
    total_usage = np.ones((1, 60 * 60 * 24, 1))

    # Get seconds at start and end of day
    seconds_in_day = 60 * 60 * 24
    start_seconds = int(fromDate.timestamp() % seconds_in_day)
    end_seconds = int(toDate.timestamp() % seconds_in_day)

    model_names = ['dishwasher', 'fridge', 'microwave', 'washing_machine']
    model_totals = {}

    for model_name in model_names:
        dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
        model_path = f'models/{model_name}.hdf5'
        abs_file_path = os.path.join(dir, model_path)
        model_totals[model_name] = __get_model_total(abs_file_path, total_usage, start_seconds, end_seconds)

    print(model_totals['dishwasher'])

    return ApplienceSplit(model_totals['dishwasher'], model_totals['fridge'],
                          model_totals['microwave'], model_totals['washing_machine'])


def __get_model_total(model_path: str, total_usage, start_seconds: int, end_seconds: int) -> int:
    model = load_model(model_path)
    increment = 50

    total = 0
    for period_start in range(start_seconds, end_seconds, increment):
        period = np.expand_dims(total_usage[0][period_start:period_start + increment], axis=0)
        total += model.predict(period)[0][0]

    print(model_path, total)
    return total
