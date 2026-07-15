import random
from dataclasses import dataclass

# Primitive is just a value object
@dataclass(frozen=True)
class Primitive:
    def __init__(self, name: str, charge: float):
        if charge < -1 or charge > 1:
            raise ValueError("Charge must be between -1 and 1")
        if not name or len(name) != 1:
            raise ValueError("Name must be a single character")
        self.name = name
        self.charge = charge

    @staticmethod
    def get_random_charge() -> float:
        return random.uniform(-1, 1)