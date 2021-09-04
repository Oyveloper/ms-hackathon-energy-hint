from consumption_data.consumption_data import get_consumption_data
from datetime import datetime
from advice.advice_data import Advice, GenericAdvice, ApplianceAdvice


CUTOFF_THRESHOLD = 1.5
DAILY_AVERAGE = -1

# Some device: 707057500100175148


def get_all_advice_for_device(device_id: str):
    data = get_consumption_data(device_id, "2019-09-10", "2020-09-10")

    data_remap = dict()

    for _, row in data.iterrows():
        data_remap[row["ds"]] = row["y"]

    return make_advice(data_remap, dict())


def make_advice(
    consumption_map: dict[datetime, float], appliance_map: dict[datetime, str]
) -> list[Advice]:
    averages = aggregate_averages(consumption_map)
    spikes = find_spikes(averages, consumption_map)

    def make_adv_local(time: int) -> Advice:
        return make_advice_for(
            time, consumption_map[time], consumption_map, appliance_map
        )

    return list(map(make_adv_local, list(reversed(sorted(spikes)))[:10]))


def aggregate_averages(
    consumption_map: dict[datetime, float]
) -> dict[tuple[int, int], float]:
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
    time: int,
    value: float,
    consumption_map: dict[datetime, float],
    appliance_map: dict[datetime, str],
) -> Advice:
    appliance = appliance_map.get(time)
    if appliance:
        move_to = find_lowest_point(consumption_map)
        return ApplianceAdvice(appliance, move_to, value, time)

    return GenericAdvice(value, time)


def find_spikes(
    aggregate_averages: dict[tuple[int, int], float],
    consumption_map: dict[datetime, float],
) -> list[int]:
    def check_cutoff(time: datetime) -> bool:
        average = aggregate_averages[(time.weekday(), time.hour)]
        return consumption_map[time] >= (average * CUTOFF_THRESHOLD)

    return filter(check_cutoff, consumption_map.keys())


def find_lowest_point(consumption_map: dict[datetime, float]) -> int:
    return min(consumption_map.keys(), key=consumption_map.__getitem__)
