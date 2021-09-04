from advice.advice_data import Advice


SPIKE_THRESHOLD_PERCENT = 1.5


def get_all_advice_for_device(device_id: str):
    pass


def make_advice(
    consumption_map: dict[int, float], appliance_map: dict[int, str]
) -> list[Advice]:
    pass


def find_spikes(consumption_map: dict[int, float]) -> list[int]:
    average = sum(consumption_map.values()) / len(consumption_map)
    cutoff_threshold = average * SPIKE_THRESHOLD_PERCENT

    def check_cutoff(time: int) -> bool:
        return consumption_map[time] >= cutoff_threshold

    return filter(check_cutoff, consumption_map.keys())


def find_lowest_point(consumption_map: dict[int, float]) -> int:
    return min(consumption_map.keys(), key=consumption_map.__getitem__)
