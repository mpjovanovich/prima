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

    def to_string(self) -> str:
        # TODO: if we're in a compound we need to show the bonds with '-'
        output = '[ '
        for i, cell in enumerate(self.state):
            if cell is None:
                output += ' '
                i += 1
            else:
                for j, primitive in enumerate(cell.primitives):
                    output += primitive.name
                    if j < len(cell.primitives) - 1:
                        output += '-'
                    i += 1
            if i < len(self.state):
                output += ' '
        output += ' ]'
        return output

        # contents = (cell.primitives[0].name if cell is not None else ' ' for cell in self.state)
        # return f"[{''.join(contents)}]"

# 1. Move          — apply vectors, resolve blocking/overlap (1D: head-on rules)
# 2. Inter         — adjacent cells, different compounds → bond / merge?
# 3. Intra         — bonded pairs within each compound → break?
# 4. Split         — if bonds removed, split disconnected pieces into new compounds
# 5. Sync grid     — refresh cell → compound from member positions

# TODO: collisions can't currently break bonds as they would in reality. The
# model doesn't capture this.