from Compound import Compound

Cell = Compound | None

class World:
    # For the state variable, Compound is a reference type, so a compound of
    # length three on a grid of length five would look like: 
    # [C1, C1, C1, None, None]. 
    # The C1 compound has the information about its component primitives.
    def __init__(
        self,
        state: list[Cell],
    ) -> None:
        self.state = state

# 1. Move          — apply vectors, resolve blocking/overlap (1D: head-on rules)
# 2. Inter         — adjacent cells, different compounds → bond / merge?
# 3. Intra         — bonded pairs within each compound → break?
# 4. Split         — if bonds removed, split disconnected pieces into new compounds
# 5. Sync grid     — refresh cell → compound from member positions

# TODO: collisions can't currently break bonds as they would in reality. The
# model doesn't capture this.