from random import Random
from World import World
from WorldConfig import WorldConfig
from WorldFactory import WorldFactory

rng = Random()
world = WorldFactory.create(WorldConfig(dimensions=(10,), primitive_count=3, population_size=5, random_number_generator=rng))
print(world.to_string())