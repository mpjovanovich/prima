from dataclasses import dataclass
from random import Random
from Primitive import Primitive
from Range import Range

# This may need split up later
@dataclass(frozen=True)
class WorldConfig:
    dimensions: tuple[int, ...]
    primitive_count: int
    population_size: int
    # TODO: how many of each type of primitive to add
    # population_skew: float = 0.5
    # ticks: int = 1000
    charge_range: Range = Range(min=-1, max=1)
    initial_vector_range: Range = Range(min=-1, max=1)