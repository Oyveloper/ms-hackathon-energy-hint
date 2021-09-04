import os
from datetime import datetime

import numpy as np
from tensorflow.keras.models import load_model

from nilm.applience_split import ApplienceSplit


def get_applience_consumption(fromDate: datetime, toDate: datetime, detail_data) -> ApplienceSplit:
    # TODO: Replace with actual 6-second usage
    total_usage = np.array([d[0] for d in detail_data])[::3]

    print(total_usage.shape)

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
        model_totals[model_name] = __get_model_total(abs_file_path, total_usage)

    print(model_totals['dishwasher'])

    return ApplienceSplit(model_totals['dishwasher'], model_totals['fridge'],
                          model_totals['microwave'], model_totals['washing_machine'])


def __get_model_total(model_path: str, total_usage) -> int:
    model = load_model(model_path)
    increment = 50

    total = 0
    for period_start in range(0, len(total_usage), increment):
        slice = total_usage[period_start:period_start + increment]
        # period = np.expand_dims(total_usage[period_start:period_start + increment], axis=0)
        period = np.reshape(slice, (1, len(slice), 1))
        total += model.predict(period)[0][0] * 6 / 3600 * increment

    print(model_path, total)
    return total
