from random import Random
from Compound import Compound
from Primitive import Primitive
from PrimitiveAlphabetBuilder import PrimitiveAlphabetBuilder
from World import World
from WorldConfig import WorldConfig
from WorldFactory import WorldFactory
from test_helpers import FakeRNG

def _get_empty_world(dimensions: tuple[int, ...]) -> World:
    alphabet_builder = PrimitiveAlphabetBuilder()
    config = WorldConfig(dimensions=dimensions, primitive_count=0, population_size=0, random_number_generator=Random())
    return WorldFactory.create(config, alphabet_builder)

def test_build_empty_grid_1d_correct_length():
    world = _get_empty_world((5,))
    assert len(world.state) == 5

def test_build_empty_grid_1d_correct_contents():
    world = _get_empty_world((5,))
    assert all(cell is None for cell in world.state)

def test_build_empty_grid_2d_correct_length():
    world = _get_empty_world((2, 3))
    assert len(world.state) == 2
    assert all(len(row) == 3 for row in world.state)

def test_build_empty_grid_2d_correct_contents():
    world = _get_empty_world((2, 3))
    assert all(all(cell is None for cell in row) for row in world.state)

def test_single_cell_single_primitive_world_creates_correct_primitive_in_cell():
    rng = FakeRNG(uniforms=[0.1, 0.2], randints=[0])
    config = WorldConfig(dimensions=(1,), primitive_count=1, population_size=1, random_number_generator=rng)
    alphabet_builder = PrimitiveAlphabetBuilder()
    world = WorldFactory.create(config, alphabet_builder)

    assert world.state[0] == Compound([Primitive('A', 0.1)], 0.2)

def test_two_cells_one_primitive_world_puts_primitive_in_one_cell_with_other_empty():
    rng = FakeRNG(uniforms=[0.1, 0.2], randints=[0])
    config = WorldConfig(dimensions=(2,), primitive_count=1, population_size=1, random_number_generator=rng)
    alphabet_builder = PrimitiveAlphabetBuilder()
    world = WorldFactory.create(config, alphabet_builder)

    assert world.state[0] == Compound([Primitive('A', 0.1)], 0.2)
    assert world.state[1] is None

def test_two_cells_two_primitive_world_puts_different_primitives_in_each_cell():
    rng = FakeRNG(uniforms=[0.1, 0.2, 0.3, 0.4], randints=[0, 1])
    config = WorldConfig(dimensions=(2,), primitive_count=2, population_size=2, random_number_generator=rng)
    alphabet_builder = PrimitiveAlphabetBuilder()
    world = WorldFactory.create(config, alphabet_builder)

    assert len(world.state[0].primitives) == 1 and world.state[0].primitives[0].name
    assert len(world.state[1].primitives) == 1 and world.state[1].primitives[0].name
    assert world.state[0].primitives[0].name != world.state[1].primitives[0].name

def test_world_prints_correctly():
    rng = FakeRNG(uniforms=[0.1, 0.2, 0.3, 0.4], randints=[0, 1])
    # config = WorldConfig(dimensions=(2,), primitive_count=1, population_size=1, random_number_generator=rng)
    config = WorldConfig(dimensions=(2,), primitive_count=2, population_size=2, random_number_generator=rng)
    alphabet_builder = PrimitiveAlphabetBuilder()
    world = WorldFactory.create(config, alphabet_builder)
    output = world.to_string()

    # Good enough without tying us down to an implementation
    assert 'A' in output
    assert 'B' in output