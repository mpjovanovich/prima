from World import World
from WorldConfig import WorldConfig
from WorldFactory import WorldFactory

world = WorldFactory.create(WorldConfig(dimensions=(10,), primitive_count=3, population_size=5))
print(world.to_string())