from Primitive import Primitive

class FakeRandomGenerator:
    def __init__(self, charges: list[float], coords: list[tuple[int, ...]], primitives: list[Primitive], vectors: list[int]):
        self.charges = iter(charges)
        self.coords = iter(coords)
        self.primitives = iter(primitives)
        self.vectors = iter(vectors)

        self.used_charges = []
        self.used_coords = []
        self.used_primitives = []
        self.used_vectors = []

    def get_random_charge(self) -> float:
        charge = next(self.charges)
        self.used_charges.append(charge)
        return charge

    def get_random_coords(self) -> tuple[int, ...]:
        coords = next(self.coords)
        self.used_coords.append(coords)
        return coords

    def get_random_primitive(self) -> Primitive:
        primitive = next(self.primitives)
        self.used_primitives.append(primitive)
        return primitive

    def get_random_vector(self) -> int:
        vector = next(self.vectors)
        self.used_vectors.append(vector)
        return vector
    
    @staticmethod
    def Create(num_values: int, dimensions: tuple[int, ...]) -> FakeRandomGenerator:
        random_generator = FakeRandomGenerator(
            charges=[i / num_values for i in range(num_values)],
            coords=[tuple(i % d for d in dimensions) for i in range(num_values)],
            # A, B, C, ...
            primitives=[Primitive(chr(65+i), i / num_values) for i in range(num_values)],
            vectors=[i for i in range(num_values)],
        )
        return random_generator