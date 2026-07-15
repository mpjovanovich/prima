from math import prod
from prima.objects.world_config import WorldConfig
from prima.domain.compound import Compound
from prima.domain.primitive import Primitive
from prima.domain.world import World
from prima.simulation.random_generator import RandomGenerator

"""
This is the starting point for all worlds.
DO NOT USE CONSTRUCTORS ANYWHERE! HORRIBLE AWFUL THINGS WILL HAPPEN!
"""
class WorldBuilder:
    def __init__(self, config: WorldConfig, random_generator: RandomGenerator):
        self.config = config
        self.random_generator = random_generator

    def create_world(self) -> World:
        # Primitive count cannot be greater than number of cells in the grid
        num_cells = prod(self.config.dimensions)
        if self.config.primitive_count > num_cells:
            raise ValueError(
                f"Primitive count ({self.config.primitive_count}) cannot be greater than number of cells in the grid ({num_cells})"
            )

        # Population size must be at least as large as the primitive count
        if self.config.population_size < self.config.primitive_count:
            raise ValueError(
                f"Population size ({self.config.population_size}) cannot be less than primitive count ({self.config.primitive_count})"
            )

        # Create the primitives
        primitives = self._create_primitives()

        # Creates an empty world with the given dimensions
        state = self._build_empty_grid(self.config.dimensions)
        world = World(state, primitives)

        if self.config.population_size > 0:
            self._populate_world_with_primitives(world)

        return world

    def _build_empty_grid(self, dimensions: tuple[int, ...]) -> list[None]:
        if len(dimensions) > 3:
            raise ValueError("World dimensions cannot be greater than 3")

        if len(dimensions) == 1:
            return [None] * dimensions[0]

        return [self._build_empty_grid(dimensions[1:]) for _ in range(dimensions[0])]

    def _create_primitives(self) -> list[Primitive]:
        primitives = []
        cur_char = 65
        for _ in range(self.config.primitive_count):
            charge = self.random_generator.get_random_charge()
            primitives.append(Primitive(chr(cur_char), charge))
            cur_char += 1

        return primitives

    def _find_empty_cell(self, world: World) -> tuple[int, ...]:
        while True:
            coords = self.random_generator.get_random_coords()
            if world.get_cell(coords) is None:
                return coords

    def _populate_world_with_primitives(self, world: World) -> None:
        # Add one of each primitive to the world
        for primitive in world._primitives:
            compound = Compound([primitive], self.random_generator.get_random_vector())
            coords = self._find_empty_cell(world)
            world.set_cell(coords, compound)

        # Populates the world with the remaining population
        for _ in range(self.config.population_size - self.config.primitive_count):
            primitive = self.random_generator.get_random_primitive(world._primitives)
            compound = Compound([primitive], self.random_generator.get_random_vector())
            coords = self._find_empty_cell(world)
            world.set_cell(coords, compound)
