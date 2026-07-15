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
    random_number_generator: Random
    # TODO: how many of each type of primitive to add
    # population_skew: float = 0.5
    # ticks: int = 1000
    charge_range: Range = Range(min=-1, max=1)
    initial_vector_range: Range = Range(min=-1, max=1)

    def get_random_charge(self) -> float:
        return self.random_number_generator.uniform(self.charge_range.min, self.charge_range.max)

    def get_random_coords(self) -> tuple[int, ...]:
        return tuple(self.random_number_generator.randint(0, d - 1) for d in self.dimensions)

    def get_random_primitive(self, primitives: list[Primitive]) -> Primitive:
        return self.random_number_generator.choice(primitives)

    def get_random_vector(self) -> int:
        return self.random_number_generator.uniform(self.initial_vector_range.min, self.initial_vector_range.max)