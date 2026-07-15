from random import Random
from prima.domain import Compound, World
from prima.objects import WorldConfig
from prima.simulation import RandomGenerator, WorldBuilder
from tests.test_helpers import FakeRandomGenerator

NUM_RANDOM_VALUES = 10

def _get_empty_world(dimensions: tuple[int, ...]) -> World:
    config = WorldConfig(dimensions=dimensions, primitive_count=0, population_size=0)
    random_generator = RandomGenerator(config, Random())
    return WorldBuilder(config, random_generator).create_world()

def test_build_empty_grid_1d_correct_length():
    world = _get_empty_world((5,))
    assert len(world._state) == 5

def test_build_empty_grid_1d_correct_contents():
    world = _get_empty_world((5,))
    assert all(cell is None for cell in world._state)

def test_build_empty_grid_2d_correct_length():
    world = _get_empty_world((2, 3))
    assert len(world._state) == 2
    assert all(len(row) == 3 for row in world._state)

def test_build_empty_grid_2d_correct_contents():
    world = _get_empty_world((2, 3))
    assert all(all(cell is None for cell in row) for row in world._state)

def test_single_cell_single_primitive_world_creates_correct_primitive_in_cell():
    config = WorldConfig(dimensions=(1,), primitive_count=1, population_size=1)
    random_generator = FakeRandomGenerator.Create(NUM_RANDOM_VALUES, config.dimensions)
    primitive = random_generator.get_random_primitive()
    world = WorldBuilder(config, random_generator).create_world()

    assert world.get_cell((0,)) == Compound([primitive], random_generator.used_vectors[0])

def test_two_cells_one_primitive_world_puts_primitive_in_one_cell_with_other_empty():
    config = WorldConfig(dimensions=(2,), primitive_count=1, population_size=1)
    random_generator = FakeRandomGenerator.Create(NUM_RANDOM_VALUES, config.dimensions)
    primitive = random_generator.get_random_primitive()
    world = WorldBuilder(config, random_generator).create_world()

    assert world.get_cell((0,)) == Compound([primitive], random_generator.used_vectors[0])
    assert world.get_cell((1,)) is None

def test_two_cells_two_primitive_world_puts_different_primitives_in_each_cell():
    config = WorldConfig(dimensions=(2,), primitive_count=2, population_size=2)
    random_generator = FakeRandomGenerator.Create(NUM_RANDOM_VALUES, config.dimensions)
    primitives = [random_generator.get_random_primitive(), random_generator.get_random_primitive()]
    world = WorldBuilder(config, random_generator).create_world()

    assert world.get_cell((0,)) == Compound([primitives[0]], random_generator.used_vectors[0])
    assert world.get_cell((1,)) == Compound([primitives[1]], random_generator.used_vectors[1])

def test_world_prints_correctly():
    config = WorldConfig(dimensions=(2,), primitive_count=2, population_size=2)
    random_generator = FakeRandomGenerator.Create(NUM_RANDOM_VALUES, config.dimensions)
    world = WorldBuilder(config, random_generator).create_world()
    output = world.to_string()

    # Good enough without tying us down to an implementation
    assert 'A' in output
    assert 'B' in output
