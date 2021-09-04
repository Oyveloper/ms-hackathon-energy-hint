from enum import Enum


class AdviceType(Enum):
    SPIKE = 0
    APPLIANCE = 1


class Advice:
    def __init__(self, consumption: float, timestamp: int, type: AdviceType) -> None:
        self.type = type
        self.timestamp = timestamp
        self.consumption = consumption


class GenericAdvice(Advice):
    def __init__(self, consumption: float, timestamp: int) -> None:
        super().__init__(consumption, timestamp, AdviceType.GENERIC)


class ApplianceAdvice(Advice):
    def __init__(
        self, appliance: str, move_to: int, consumption: float, timestamp: int
    ) -> None:
        super().__init__(consumption, timestamp, AdviceType.APPLIANCE)
        self.appliance = appliance
        self.move_to = move_to
