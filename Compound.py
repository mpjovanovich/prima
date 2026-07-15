from Primitive import Primitive

class Compound:
    def __init__(self, primitives: list[Primitive], vector: int):
        # The primitives that make up the compound, spacially encoded in n
        # dimensions. Empty space is represented by None.
        self.primitives = primitives
        # Movement per tick
        self.vector = vector