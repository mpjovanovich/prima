from math import prod
from random import Random
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
        rng = Random(config.seed) if config.seed is not None else Random()

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
            WorldFactory._populate_world_with_primitives(world, config, rng)

        return world

    # Returns the compound that was added
    @staticmethod
    def _add_primitive_compound_to_random_cell(world: World, config: WorldConfig, primitive_compound: Compound, rng: Random) -> None:
        # Get a cell that has None
        while True:
            coords = WorldFactory._get_random_coords(config.dimensions, rng)

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

    # Creates the primitive alphabet
    @staticmethod
    def _create_primitive_alphabet(config: WorldConfig, rng: Random) -> list[Primitive]:
        primitives = []
        cur_char = 65
        for _ in range(config.primitive_count):
            primitives.append(Primitive(chr(cur_char), WorldFactory._get_random_charge(config, rng)))
            cur_char += 1

        return primitives

    @staticmethod
    def _get_random_charge(config: WorldConfig, rng: Random) -> float:
        return rng.uniform(config.charge_range.min, config.charge_range.max)

    # Returns a random coordinate within the grid
    @staticmethod
    def _get_random_coords(dimensions: tuple[int, ...], rng: Random) -> tuple[int, ...]:
        return tuple(rng.randint(0, d - 1) for d in dimensions)

    @staticmethod
    def _get_random_vector(config: WorldConfig, rng: Random) -> int:
        return rng.uniform(config.initial_vector_range.min, config.initial_vector_range.max)

    @staticmethod
    def _populate_world_with_primitives(world: World, config: WorldConfig, rng: Random) -> None:
        # Add one of each primitive to the world
        primitives = WorldFactory._create_primitive_alphabet(config, rng)
        for primitive in primitives:
            compound = Compound([primitive], WorldFactory._get_random_vector(config, rng))
            WorldFactory._add_primitive_compound_to_random_cell(world, config, compound, rng)

        # Populates the world with the remaining population
        for _ in range(config.population_size - config.primitive_count):
            primitive = rng.choice(primitives)
            compound = Compound([primitive], WorldFactory._get_random_vector(config, rng))
            WorldFactory._add_primitive_compound_to_random_cell(world, config, compound, rng)