from random import Random
from Primitive import Primitive
from WorldConfig import WorldConfig

# A proxy for the random generators
class RandomGenerator:
    def __init__(self, config: WorldConfig, random_number_generator: Random | None = None):
        self._config = config
        self._random_number_generator = random_number_generator if random_number_generator is not None else Random()

    def get_random_charge(self) -> float:
        return self._random_number_generator.uniform(self._config.charge_range.min, self._config.charge_range.max)

    def get_random_coords(self) -> tuple[int, ...]:
        return tuple(self._random_number_generator.randint(0, d - 1) for d in self._config.dimensions)

    def get_random_primitive(self, primitives: list[Primitive]) -> Primitive:
        return self._random_number_generator._choice(primitives)

    def get_random_vector(self) -> int:
        return self._random_number_generator.uniform(self._config.initial_vector_range.min, self._config.initial_vector_range.max)