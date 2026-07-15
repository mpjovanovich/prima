from Primitive import Primitive
from WorldConfig import WorldConfig

class PrimitiveAlphabetBuilder:
    def build_primitives(self, config: WorldConfig) -> list[Primitive]:
        primitives = []
        cur_char = 65
        for _ in range(config.primitive_count):
            charge = config.get_random_charge()
            primitives.append(Primitive(chr(cur_char), charge))
            cur_char += 1

        return primitives
