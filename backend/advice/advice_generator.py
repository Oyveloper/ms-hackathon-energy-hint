from consumption_data.consumption_data import (
    get_consumption_data,
    get_consumption_all_devices,
)
from datetime import date, datetime, timedelta
from advice.advice_data import Advice, ApplianceAdvice, HighDailyAdvice
import pandas as pd
import numpy as np


CUTOFF_THRESHOLD = 1.5
DAILY_AVERAGE = -1

# Some device: 707057500100175148


def get_averages_all_devices(start_date: str, end_date: str):
    data = get_consumption_all_devices(start_date, end_date)
    d = data[0]
    for i in range(1, len(data)):
        d = pd.concat([d, data[i]], axis=1)
    d = d.drop(columns="ds")
    d = d.mean(axis=1)
    return d


def get_all_advice_for_device(device_id: str):
    data = get_consumption_data(device_id, "2019-09-10", "2020-09-10")

    data_remap = dict()

    for _, row in data.iterrows():
        data_remap[row["ds"]] = row["y"]

    return make_advice(data_remap, dict())


def make_advice(
    consumption_map: "dict[datetime, float]", appliance_map: "dict[datetime, str]"
) -> "list[Advice]":
    averages = aggregate_averages(consumption_map)
    spikes = find_spikes(averages, consumption_map)

    def make_adv_local(time: int) -> Advice:
        return make_advice_for(
            time, consumption_map[time], averages, consumption_map, appliance_map
        )

    return [adv for adv in map(make_adv_local, list(reversed(sorted(spikes)))) if adv]


def aggregate_averages(
    consumption_map: "dict[datetime, float]",
) -> "dict[tuple[int, int], float]":
    sum_map = dict()
    count_map = dict()

    for timestamp, value in consumption_map.items():
        key = (timestamp.weekday(), timestamp.hour)
        if not key in sum_map:
            sum_map[key] = value
            count_map[key] = 1
        else:
            sum_map[key] += value
            count_map[key] += 1

    for key, val in sum_map.items():
        sum_map[key] = val / count_map[key]

    for day in range(7):
        sum = 0
        for hour in range(24):
            sum += sum_map[(day, hour)]

        sum_map[(day, DAILY_AVERAGE)] = sum

    return sum_map


def make_advice_for(
    time: datetime,
    value: float,
    average_map: "dict[tuple[int, int], float]",
    consumption_map: "dict[datetime, float]",
    appliance_map: "dict[datetime, str]",
) -> Advice:
    appliance = appliance_map.get(time)
    if appliance:
        move_to = find_lowest_point(consumption_map)
        return ApplianceAdvice(appliance, move_to, value, time)

    daily_average = average_map[(time.weekday(), DAILY_AVERAGE)]
    daily_total = 0

    day_start = time - timedelta(hours=time.hour)

    for clock in range(24):
        tmp = day_start + timedelta(hours=clock)
        if tmp not in consumption_map:
            continue

        val = consumption_map[tmp]
        if val > value:
            return None

        daily_total += val

    if daily_total < daily_average * CUTOFF_THRESHOLD:
        return None

    return HighDailyAdvice(daily_average, daily_total, time)


def find_spikes(
    aggregate_averages: "dict[tuple[int, int], float]",
    consumption_map: "dict[datetime, float]",
) -> "list[int]":
    def check_cutoff(time: datetime) -> bool:
        average = aggregate_averages[(time.weekday(), time.hour)]
        return consumption_map[time] >= (average * CUTOFF_THRESHOLD)

    return filter(check_cutoff, consumption_map.keys())


def find_lowest_point(consumption_map: "dict[datetime, float]") -> int:
    return min(consumption_map.keys(), key=consumption_map.__getitem__)


def find_base_energy_consumption(meteringpointId: str) -> int:
    return find_lowest_point(
        get_consumption_data(meteringpointId, "2019-09-10", "2020-09-10")
    )
