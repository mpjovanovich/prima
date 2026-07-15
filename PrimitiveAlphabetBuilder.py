from random import Random
from Primitive import Primitive
from Range import Range
from WorldConfig import WorldConfig

class PrimitiveAlphabetBuilder:
    def build_primitives(self, config: WorldConfig, rng: Random) -> list[Primitive]:
        primitives = []
        cur_char = 65
        for _ in range(config.primitive_count):
            charge = config.get_random_charge(rng)
            primitives.append(Primitive(chr(cur_char), charge))
            cur_char += 1

        return primitives
