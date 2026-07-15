from dataclasses import dataclass

@dataclass(frozen=True)
class FloatRange:
    min: float
    max: float

    def __post_init__(self):
        if self.min > self.max:
            raise ValueError("Min must be less than max")