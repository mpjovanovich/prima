import random
from math import prod
from Compound import Compound
from Primitive import Primitive
from WorldConfig import WorldConfig
from World import World

"""
This is the starting point for all worlds.
DO NOT USE CONSTRUCTORS ANYWHERE! HORRIBLE AWFUL THINGS WILL HAPPEN!
"""
class WorldFactory:
    @staticmethod
    def create(config: WorldConfig) -> World:
        if config.seed is not None:
            random.seed(config.seed)

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
            # Add one of each primitive to the world
            primitives = WorldFactory._create_primitive_alphabet(config)
            for primitive in primitives:
                compound = Compound([primitive])
                WorldFactory._add_primitive_compound_to_random_cell(world, compound)

            # Populates the world with the remaining population
            for _ in range(config.population_size - config.primitive_count):
                primitive = random.choice(primitives)
                compound = Compound([primitive])
                WorldFactory._add_primitive_compound_to_random_cell(world, compound)

        return world

    # Returns the compound that was added
    @staticmethod
    def _add_primitive_compound_to_random_cell(world: World, primitive_compound: Compound) -> None:
        # Get a cell that has None
        while True:
            coords = WorldFactory._get_random_coords(world.dimensions)
            if world.state[coords] is None:
                break

        # Add the compound to the cell
        world.state[coords] = primitive_compound

    @staticmethod
    def _build_empty_grid(dimensions: tuple[int, ...]) -> list[None]:
        if len(dimensions) > 3:
            raise ValueError("World dimensions cannot be greater than 3")

        if len(dimensions) == 1:
            return [None] * dimensions[0]

        return [WorldFactory._build_empty_grid(dimensions[1:]) for _ in range(dimensions[0])]

    # Creates the primitive alphabet
    @staticmethod
    def _create_primitive_alphabet(config: WorldConfig) -> list[Primitive]:
        primitives = []
        cur_char = 65
        for _ in range(config.primitive_count):
            primitives.append(Primitive(chr(cur_char), random.uniform(-1, 1)))
            cur_char += 1

    # Returns a random coordinate within the grid
    @staticmethod
    def _get_random_coords(dimensions: tuple[int, ...]) -> tuple[int, ...]:
        return tuple(random.randint(0, d - 1) for d in dimensions)

    @staticmethod
    def _populate_world_with_primitives(world: World, config: WorldConfig) -> None:
        # Add one of each primitive to the world
        primitives = WorldFactory._create_primitive_alphabet(config)
        for primitive in primitives:
            compound = Compound([primitive])
            WorldFactory._add_primitive_compound_to_random_cell(world, compound)

        # Populates the world with the remaining population
        for _ in range(config.population_size - config.primitive_count):
            primitive = random.choice(primitives)
            compound = Compound([primitive])
            WorldFactory._add_primitive_compound_to_random_cell(world, compound)