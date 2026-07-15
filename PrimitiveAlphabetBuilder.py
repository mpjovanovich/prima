# from Primitive import Primitive
# from RandomGenerator import RandomGenerator

# class PrimitiveAlphabetBuilder:
#     def build_primitives(self, primitive_count: int, random_generator: RandomGenerator) -> list[Primitive]:
#         primitives = []
#         cur_char = 65
#         for _ in range(primitive_count):
#             charge = random_generator.get_random_charge()
#             primitives.append(Primitive(chr(cur_char), charge))
#             cur_char += 1

#         return primitives
