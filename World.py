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

    def get_cell(self, coords: tuple[int, ...]):
        cell = self.state
        for c in coords:
            cell = cell[c]
        return cell

    def set_cell(self, coords: tuple[int, ...], value: Cell) -> None:
        cell = self.state
        for c in coords[:-1]:
            cell = cell[c]
        cell[coords[-1]] = value
    
    def to_string(self) -> str:
        output = '[ '
        i = 0
        while i < len(self.state):
            cell = self.state[i]
            if cell is None:
                output += ' '
                i += 1
            else:
                for j, primitive in enumerate(cell.primitives):
                    output += primitive.name
                    i += 1
                    if j < len(cell.primitives) - 1:
                        output += '-'
            if i < len(self.state):
                output += ' '
        output += ' ]'
        return output
        
# 1. Move          — apply vectors, resolve blocking/overlap (1D: head-on rules)
# 2. Inter         — adjacent cells, different compounds → bond / merge?
# 3. Intra         — bonded pairs within each compound → break?
# 4. Split         — if bonds removed, split disconnected pieces into new compounds
# 5. Sync grid     — refresh cell → compound from member positions

# TODO: collisions can't currently break bonds as they would in reality. The
# model doesn't capture this.