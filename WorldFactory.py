from math import prod
from random import Random
from Compound import Compound
from Primitive import Primitive
from WorldConfig import WorldConfig
from PrimitiveAlphabetBuilder import PrimitiveAlphabetBuilder
from World import World

"""
This is the starting point for all worlds.
DO NOT USE CONSTRUCTORS ANYWHERE! HORRIBLE AWFUL THINGS WILL HAPPEN!
"""
class WorldFactory:
    @staticmethod
    def create(config: WorldConfig, alphabet_builder: PrimitiveAlphabetBuilder, rng: Random | None = None) -> World:
        if rng is None:
            rng = Random()

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
            WorldFactory._populate_world_with_primitives(world, config, alphabet_builder, rng)

        return world

    # Returns the compound that was added
    @staticmethod
    def _add_primitive_compound_to_random_cell(world: World, config: WorldConfig, primitive_compound: Compound, rng: Random) -> None:
        # Get a cell that has None
        while True:
            coords = WorldFactory._get_random_coords(config, rng)

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
    def _get_random_charge(config: WorldConfig, rng: Random) -> float:
        return rng.uniform(config.charge_range.min, config.charge_range.max)

    # Returns a random coordinate within the grid
    @staticmethod
    def _get_random_coords(config: WorldConfig, rng: Random) -> tuple[int, ...]:
        return tuple(rng.randint(0, d - 1) for d in config.dimensions)

    @staticmethod
    def _get_random_vector(config: WorldConfig, rng: Random) -> int:
        return rng.uniform(config.initial_vector_range.min, config.initial_vector_range.max)

    @staticmethod
    def _populate_world_with_primitives(world: World, config: WorldConfig, alphabet_builder: PrimitiveAlphabetBuilder, rng: Random) -> None:
        # Add one of each primitive to the world
        # primitives = WorldFactory._create_primitive_alphabet(config, rng)
        primitives = alphabet_builder.build_primitives(config.primitive_count, config.charge_range, rng)
        for primitive in primitives:
            compound = Compound([primitive], WorldFactory._get_random_vector(config, rng))
            WorldFactory._add_primitive_compound_to_random_cell(world, config, compound, rng)

        # Populates the world with the remaining population
        for _ in range(config.population_size - config.primitive_count):
            primitive = rng.choice(primitives)
            compound = Compound([primitive], WorldFactory._get_random_vector(config, rng))
            WorldFactory._add_primitive_compound_to_random_cell(world, config, compound, rng)