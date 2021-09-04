from advice.advice_generator import find_base_energy_consumption
from collections import defaultdict
from advice.advice_data import Advice, AdviceType
from advice.advice_generator import aggregate_averages, get_all_advice_for_device, get_averages_all_devices, find_lowest_point
from consumption_data.consumption_data import get_consumption_data
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def visualize(data: pd.DataFrame, advice_list: "list[AdviceType]"):
    data_remap = defaultdict(lambda: 0.0)

    for _, row in data.iterrows():
        data_remap[row["ds"]] = row["y"]

    averages = aggregate_averages(data_remap)

    for advice in advice_list:
        time = advice.timestamp - timedelta(hours=12)
        dates = list(map(lambda x: time + timedelta(hours=x), range(24)))
        values = list(map(data_remap.__getitem__, dates))
        pop_avg = list(get_averages_all_devices(str(time), str(time + timedelta(hours=24))))
        visualize_single(averages, dates, values, advice, pop_avg)


def visualize_single(
    averages: "dict[tuple[int, int], float]",
    dates: "list[datetime]",
    values: "list[float]",
    advice: Advice,
    pop_avg: "list[float]" = []
):
    def get_name(date: datetime) -> str:
        if date == advice.timestamp:
            return "SPIKE!"
        return date.strftime("%H")

    tick_label = list(map(get_name, dates))

    indices = list(range(24))

    plt.bar(
        indices,
        values,
        tick_label=tick_label,
        width=0.8,
        color=["red", "green"],
    )


    min_val = np.where(np.array(values) <= min(values), values, 0)
    plt.bar(
        indices,
        min_val,
        tick_label=tick_label,
        width=0.8,
        color='blue'
    )

    """
    plt.bar(
        indices,
        pop_avg,
        tick_label=tick_label,
        width=0.4,
        color=["blue", "red"],
    )
    """

    average = []
    for date in dates:
        average.append(averages[(date.weekday(), date.hour)])

    plt.plot(indices, average)

    plt.xlabel("Time")
    plt.ylabel("Consumption")
    plt.title("Consumption")

    plt.show()


if __name__ == "__main__":
    d1 = find_base_energy_consumption('707057500100175148')
    print(d1)
    data = get_consumption_data("707057500100175148", "2019-09-10", "2020-09-10")
    advice = get_all_advice_for_device("707057500100175148")

    visualize(data, advice)
