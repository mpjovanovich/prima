from random import Random
from PrimitiveAlphabetBuilder import PrimitiveAlphabetBuilder
from World import World
from WorldConfig import WorldConfig
from WorldFactory import WorldFactory

rng = Random()
config = WorldConfig(
    dimensions=(10,), 
    primitive_count=3, 
    population_size=5, 
    random_number_generator=rng
)

alphabet_builder = PrimitiveAlphabetBuilder()
world = WorldFactory.create(config, alphabet_builder)

print(world.to_string())