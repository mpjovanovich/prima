from math import prod
from random import Random
from Compound import Compound
from WorldConfig import WorldConfig
from PrimitiveAlphabetBuilder import PrimitiveAlphabetBuilder
from World import World

"""
This is the starting point for all worlds.
DO NOT USE CONSTRUCTORS ANYWHERE! HORRIBLE AWFUL THINGS WILL HAPPEN!
"""
class WorldFactory:
    @staticmethod
    def create(config: WorldConfig, alphabet_builder: PrimitiveAlphabetBuilder) -> World:
        # Primitive count cannot be greater than number of cells in the grid
        num_cells = prod(config.dimensions)
        if config.primitive_count > num_cells:
            raise ValueError(
                f"Primitive count ({config.primitive_count}) cannot be greater than number of cells in the grid ({num_cells})"
            )

        # Population size must be at least as large as the primitive count
        if config.population_size < config.primitive_count:
            raise ValueError(
                f"Population size ({config.population_size}) cannot be less than primitive count ({config.primitive_count})"
            )

        # Creates an empty world with the given dimensions
        state = WorldFactory._build_empty_grid(config.dimensions)
        world = World(state)

        if config.population_size > 0:
            WorldFactory._populate_world_with_primitives(world, config, alphabet_builder)

        return world

    # Returns the compound that was added
    @staticmethod
    def _add_primitive_compound_to_random_cell(world: World, config: WorldConfig, primitive_compound: Compound) -> None:
        # Get a cell that has None
        while True:
            coords = config.get_random_coords()

            # This will break later when we're not using 1D
            # temp workaround
            index = coords[0]

            if world.state[index] is None:
                break

        # Add the compound to the cell
        world.state[index] = primitive_compound

    @staticmethod
    def _build_empty_grid(dimensions: tuple[int, ...]) -> list[None]:
        if len(dimensions) > 3:
            raise ValueError("World dimensions cannot be greater than 3")

        if len(dimensions) == 1:
            return [None] * dimensions[0]

        return [WorldFactory._build_empty_grid(dimensions[1:]) for _ in range(dimensions[0])]

    @staticmethod
    def _populate_world_with_primitives(world: World, config: WorldConfig, alphabet_builder: PrimitiveAlphabetBuilder) -> None:
        # Add one of each primitive to the world
        primitives = alphabet_builder.build_primitives(config)
        for primitive in primitives:
            compound = Compound([primitive], config.get_random_vector())
            WorldFactory._add_primitive_compound_to_random_cell(world, config, compound)

        # Populates the world with the remaining population
        for _ in range(config.population_size - config.primitive_count):
            primitive = config.get_random_primitive(primitives)
            compound = Compound([primitive], config.get_random_vector())
            WorldFactory._add_primitive_compound_to_random_cell(world, config, compound)