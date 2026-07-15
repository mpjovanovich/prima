# from random import Random
# from PrimitiveAlphabetBuilder import PrimitiveAlphabetBuilder
# from Compound import Compound
# from Primitive import Primitive
# from World import World
# from WorldConfig import WorldConfig
# from WorldFactory import WorldFactory

# rng = Random()
# config = WorldConfig(
#     dimensions=(10,), 
#     primitive_count=3, 
#     population_size=5, 
#     random_number_generator=rng
# )

# alphabet_builder = PrimitiveAlphabetBuilder()
# world = WorldFactory.create(config, alphabet_builder)

# print(world.to_string())

## Make a world directly with constructor in order to test to_string output when there are compounds
c1 = Compound([Primitive('A', 0.1), Primitive('C', 0.5)], 0.2)
c2 = Compound([Primitive('B', 0.3)], 0.4)
# world = World(state=[c1, c1, c2])
world = World(state=[c1, c1, None, c2])
print(world.to_string())