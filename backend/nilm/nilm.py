from datetime import datetime, timedelta
import numpy as np
from applience_split import ApplienceSplit
from tensorflow.keras.models import load_model


def get_applience_consumption(fromDate: datetime, toDate: datetime) -> ApplienceSplit:
    # TODO: Replace with actual 6-second usage
    total_usage = np.ones((1, 60 * 60 * 24, 1))

    # Get seconds at start and end of day
    seconds_in_day = 60 * 60 * 24
    start_seconds = int(fromDate.timestamp() % seconds_in_day)
    end_seconds = int(toDate.timestamp() % seconds_in_day)

    model_names = ['dishwasher', 'fridge', 'kettle', 'microwave', 'washing_machine']
    model_totals = {}

    for model_name in model_names:
        model_path = f'models/{model_name}.hdf5'
        model_totals[model_name] = get_model_total(model_path, total_usage, start_seconds, end_seconds)

    print(model_totals['dishwasher'])

    return ApplienceSplit(model_totals['dishwasher'], model_totals['fridge'], model_totals['kettle'], model_totals['microwave'], model_totals['washing_machine'])


def get_model_total(model_path: str, total_usage, start_seconds: int, end_seconds: int) -> int:
    model = load_model(model_path)
    increment = 50

    total = 0
    for period_start in range(start_seconds, end_seconds, increment):
        period = np.expand_dims(total_usage[0][period_start:period_start + increment], axis=0)
        total += model.predict(period)[0][0]

    print(model_path, total)
    return total
