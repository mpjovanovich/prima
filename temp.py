from random import Random
from Compound import Compound
from Primitive import Primitive
from RandomGenerator import RandomGenerator
from World import World
from WorldConfig import WorldConfig
from WorldBuilder import WorldBuilder

config = WorldConfig(
    dimensions=(10,), 
    primitive_count=3, 
    population_size=5, 
)
random_generator = RandomGenerator(config)

# world = WorldBuilder(config, random_generator).create_world()
# print(world.to_string())

## Make a world directly with constructor in order to test to_string output when there are compounds
## This is a hack to test the print output when there are compounds
primitives = [Primitive('A', 0.1), Primitive('B', 0.3), Primitive('C', 0.5)]
c1 = Compound([Primitive('A', 0.1), Primitive('C', 0.5)], 0.2)
c2 = Compound([Primitive('B', 0.3)], 0.4)
# world = World(state=[c1, c1, c2], primitives=primitives)
world = World(state=[c1, c1, None, c2], primitives=primitives)
print(world.to_string())