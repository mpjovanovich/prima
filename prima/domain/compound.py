from prima.domain.primitive import Primitive

class Compound:
    def __init__(self, primitives: list[Primitive], vector: int):
        # The primitives that make up the compound, spacially encoded in n
        # dimensions. Empty space is represented by None.
        self.primitives = primitives
        # Movement per tick
        self.vector = vector

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Compound):
            return NotImplemented
        return self.primitives == other.primitives and self.vector == other.vector
