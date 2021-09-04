from datetime import datetime
from enum import Enum


class AdviceType(Enum):
    SPIKE = 0
    APPLIANCE = 1


class Advice:
    def __init__(self, consumption: float, timestamp: datetime, type: AdviceType) -> None:
        self.type = type
        self.timestamp = timestamp
        self.consumption = consumption            

    def __repr__(self) -> str:
        return f"Advice: {self.type} @ {self.timestamp} w/ {self.consumption}"

class GenericAdvice(Advice):
    def __init__(self, consumption: float, timestamp: datetime) -> None:
        super().__init__(consumption, timestamp, AdviceType.SPIKE)


class ApplianceAdvice(Advice):
    def __init__(
        self, appliance: str, move_to: int, consumption: float, timestamp: datetime
    ) -> None:
        super().__init__(consumption, timestamp, AdviceType.APPLIANCE)
        self.appliance = appliance
        self.move_to = move_to
