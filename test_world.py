from Compound import Compound
from Primitive import Primitive
from World import World
from WorldConfig import WorldConfig
from WorldFactory import WorldFactory
from test_helpers import FakeRNG

def _get_empty_world(dimensions: tuple[int, ...]) -> World:
    config = WorldConfig(dimensions=dimensions, primitive_count=0, population_size=0)
    return WorldFactory.create(config)

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
    config = WorldConfig(dimensions=(1,), primitive_count=1, population_size=1)
    rng = FakeRNG(uniforms=[0.1, 0.2], randints=[0])
    world = WorldFactory.create(config, rng=rng)

    assert world.state[0] == Compound([Primitive('A', 0.1)], 0.2)

def test_two_cells_one_primitive_world_puts_primitive_in_one_cell_with_other_empty():
    config = WorldConfig(dimensions=(2,), primitive_count=1, population_size=1)
    rng = FakeRNG(uniforms=[0.1, 0.2], randints=[0])
    world = WorldFactory.create(config, rng=rng)

    assert world.state[0] == Compound([Primitive('A', 0.1)], 0.2)
    assert world.state[1] is None

def test_two_cells_two_primitive_world_puts_primitives_in_each_cell():
    config = WorldConfig(dimensions=(2,), primitive_count=2, population_size=2)
    rng = FakeRNG(uniforms=[0.1, 0.2, 0.3, 0.4], randints=[0, 1])
    world = WorldFactory.create(config, rng=rng)

    assert world.state[0].primitives[0].name == 'A'
    assert world.state[1].primitives[0].name == 'B'