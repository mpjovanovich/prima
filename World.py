import random
from typing import TypeAlias
from Compound import Compound

Cell = Compound | None
Dimensions = tuple[int, ...]

class World:
    # For the state variable, Compound is a reference type, so a compound of
    # length three on a grid of length five would look like: 
    # [C1, C1, C1, None, None]. 
    # The C1 compound has the information about its component primitives.
    def __init__(
        self,
        dimensions: Dimensions,
        seed: int | None = None,
    ) -> None:
        if seed:
            random.seed(seed)
        self.dimensions = dimensions
        self.state = self.build_empty_grid(self.dimensions)

    def build_empty_grid(self, dimensions: list[int]):
        if len(dimensions) > 3:
            raise ValueError("World dimensions cannot be greater than 3")

        if len(dimensions) == 1:
            return [None] * dimensions[0]

        return [self.build_empty_grid(dimensions[1:]) for _ in range(dimensions[0])]

    # Returns a random coordinate within the grid
    def get_random_coords(self) -> tuple[int, ...]:
        return tuple(random.randint(0, d - 1) for d in self.dimensions)

    # def add_primitive_compound_to_random_cell(self, primitive_compound: Compound):
    #     # Get random coords within the grid
    #     coords = self.get_random_coords(self.state.dimensions)

# 1. Move          — apply vectors, resolve blocking/overlap (1D: head-on rules)
# 2. Inter         — adjacent cells, different compounds → bond / merge?
# 3. Intra         — bonded pairs within each compound → break?
# 4. Split         — if bonds removed, split disconnected pieces into new compounds
# 5. Sync grid     — refresh cell → compound from member positions

# TODO: collisions can't currently break bonds as they would in reality. The
# model doesn't capture this.