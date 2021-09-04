from enum import Enum


class AdviceType(Enum):
    GENERIC = 0
    APPLIANCE_MOVE = 1
    APPLIANCE_SPIKE = 2


class Advice:
    def __init__(self, consumption: float, timestamp: int, type: AdviceType) -> None:
        self.type = type
        self.timestamp = timestamp
        self.consumption = consumption


class GenericAdvice(Advice):
    def __init__(self, text: str, consumption: float, timestamp: int) -> None:
        super().__init__(consumption, timestamp, AdviceType.GENERIC)
        self.text = text
