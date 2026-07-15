from dataclasses import dataclass

# Primitive is just a value object
@dataclass(frozen=True)
class Primitive:
    name: str
    charge: float

    def __post_init__(self):
        if self.charge < -1 or self.charge > 1:
            raise ValueError("Charge must be between -1 and 1")
        if not self.name or len(self.name) != 1:
            raise ValueError("Name must be a single character")
