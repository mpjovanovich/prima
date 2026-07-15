from random import Random
from Primitive import Primitive
from Range import Range


class PrimitiveAlphabetBuilder:
    def build_primitives(self, primitive_count: int, charge_range: Range, rng: Random) -> list[Primitive]:
        primitives = []
        cur_char = 65
        for _ in range(primitive_count):
            charge = rng.uniform(charge_range.min, charge_range.max)
            primitives.append(Primitive(chr(cur_char), charge))
            cur_char += 1

        return primitives
