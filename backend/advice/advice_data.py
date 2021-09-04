from datetime import datetime
from enum import Enum


class AdviceType(Enum):
    SPIKE = 0
    APPLIANCE = 1
    DAILY = 2


class Advice:
    def __init__(
        self, consumption: float, timestamp: datetime, type: AdviceType
    ) -> None:
        self.type = type
        self.timestamp = timestamp
        self.consumption = consumption

    def as_dict(self) -> dict[str, object]:
        pass

    def __repr__(self) -> str:
        return f"Advice: {self.type} @ {self.timestamp} w/ {self.consumption}"


class GenericAdvice(Advice):
    def __init__(self, consumption: float, timestamp: datetime) -> None:
        super().__init__(consumption, timestamp, AdviceType.SPIKE)

    def as_dict(self) -> dict[str, object]:
        return {
            "type": self.type.name,
            "timestamp": str(self.timestamp),
            "consumption": self.consumption,
        }


class ApplianceAdvice(Advice):
    def __init__(
        self, appliance: str, move_to: int, consumption: float, timestamp: datetime
    ) -> None:
        super().__init__(consumption, timestamp, AdviceType.APPLIANCE)
        self.appliance = appliance
        self.move_to = move_to

    def as_dict(self) -> dict[str, object]:
        return {
            "type": self.type.name,
            "timestamp": str(self.timestamp),
            "consumption": self.consumption,
            "appliance": self.appliance,
            "move_to": self.move_to,
        }


class HighDailyAdvice(Advice):
    def __init__(self, average: float, consumption: float, timestamp: datetime) -> None:
        super().__init__(consumption, timestamp, AdviceType.DAILY)
        self.average = average

    def as_dict(self) -> dict[str, object]:
        return {
            "type": self.type.name,
            "timestamp": str(self.timestamp),
            "consumption": self.consumption,
            "average": self.average,
        }
