from dataclasses import dataclass
from random import Random
from Range import Range

# This may need split up later
@dataclass(frozen=True)
class WorldConfig:
    dimensions: tuple[int, ...]
    primitive_count: int
    population_size: int
    # random_number_generator: Random
    # TODO: how many of each type of primitive to add
    # population_skew: float = 0.5
    # ticks: int = 1000
    charge_range: Range = Range(min=-1, max=1)
    initial_vector_range: Range = Range(min=-1, max=1)

    def get_random_charge(self, rng: Random) -> float:
        return rng.uniform(self.charge_range.min, self.charge_range.max)

    def get_random_coords(self, rng: Random) -> tuple[int, ...]:
        return tuple(rng.randint(0, d - 1) for d in self.dimensions)

    def get_random_vector(self, rng: Random) -> int:
        return rng.uniform(self.initial_vector_range.min, self.initial_vector_range.max)