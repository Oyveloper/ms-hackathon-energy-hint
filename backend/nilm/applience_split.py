class ApplienceSplit:
    def __init__(self, dishwasher: int, fridge: int, microwave: int, washing_machine: int):
        self.dishwasher = dishwasher
        self.fridge = fridge
        self.microwave = microwave
        self.washing_machine = washing_machine

    def as_json(self):
        return [
            {
                "name": "dishwasher",
                "power": self.dishwasher
            },
            {
                "name": "fridge",
                "power": self.fridge
            },
            {
                "name": "microwave",
                "power": self.microwave
            },
            {
                "name": "washing_machine",
                "power": self.washing_machine
            },
        ]

    def __str__(self) -> str:
        return f'[\n dishwasher: {self.dishwasher} \n fridge: {self.fridge} \n  microwave: {self.microwave} \n washin_machine: {self.washing_machine} \n]'
