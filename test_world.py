from Compound import Compound
from Primitive import Primitive
from World import World
from WorldConfig import WorldConfig
from WorldFactory import WorldFactory

def _get_empty_world(dimensions: tuple[int, ...]) -> World:
    config = WorldConfig(dimensions=dimensions, primitive_count=0, population_size=0, seed=1)
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


def test_single_cell_single_primitive_world_created_correctly():
    config = WorldConfig(dimensions=(1,), primitive_count=1, population_size=1, seed=1)
    world = WorldFactory.create(config)

    actual = world.state[0]
    expected = Compound([Primitive('A', -0.7312715117751976)], 0.6948674738744653)

    assert actual == expected