from random import Random
from prima.domain.world import World
from prima.objects.world_config import WorldConfig
from prima.simulation.random_generator import RandomGenerator
from prima.simulation.world_builder import WorldBuilder

class WorldEngine:
    def __init__(self, config: WorldConfig) -> None:
        self._config = config

        # Create a random generator with the given config
        random_generator = Random()
        if config.seed is not None:
            random_generator.seed(config.seed)
        self._random_generator = RandomGenerator(config, random_generator)

        # Create the world with the given parameters
        self._world = WorldBuilder(config, self._random_generator).create_world()

    def step(self) -> None:
        # temp - just print the world
        print(self._world.to_string())