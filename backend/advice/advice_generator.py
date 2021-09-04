from advice.advice_data import Advice, GenericAdvice, ApplianceAdvice


SPIKE_THRESHOLD_PERCENT = 1.5


def get_all_advice_for_device(device_id: str):
    pass


def make_advice(
    consumption_map: dict[int, float], appliance_map: dict[int, str]
) -> list[Advice]:
    spikes = find_spikes(consumption_map)

    def make_adv_local(time: int) -> Advice:
        return make_advice(time, consumption_map[time], consumption_map, appliance_map)

    return filter(map(make_adv_local, spikes))


def make_advice_for(
    time: int,
    value: float,
    consumption_map: dict[int, float],
    appliance_map: dict[int, str],
) -> Advice:
    appliance = appliance_map.get(time)
    if appliance:
        move_to = find_lowest_point(consumption_map)
        return ApplianceAdvice(appliance, move_to, value, time)

    return GenericAdvice(value, time)


def find_spikes(consumption_map: dict[int, float]) -> list[int]:
    # Could potentially also use some historical average here?
    average = sum(consumption_map.values()) / len(consumption_map)
    cutoff_threshold = average * SPIKE_THRESHOLD_PERCENT

    def check_cutoff(time: int) -> bool:
        return consumption_map[time] >= cutoff_threshold

    return filter(check_cutoff, consumption_map.keys())


def find_lowest_point(consumption_map: dict[int, float]) -> int:
    return min(consumption_map.keys(), key=consumption_map.__getitem__)
