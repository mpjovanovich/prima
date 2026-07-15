from dataclasses import dataclass

# This may need split up later

@dataclass(frozen=True)
class WorldConfig:
    dimensions: tuple[int, ...]
    primitive_count: int
    population_size: int
    # population_skew: float = 0.5 # TODO: skew the distribution of initial positions of primitives
    # ticks: int = 1000
    seed: int | None = None