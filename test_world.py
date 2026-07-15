from World import World

def test_build_empty_grid_1d_correct_length():
    world = World([5])
    assert len(world.state) == 5

def test_build_empty_grid_1d_correct_contents():
    world = World([5])
    assert all(cell is None for cell in world.state)

def test_build_empty_grid_2d_correct_length():
    world = World([2, 3])
    assert len(world.state) == 2
    assert all(len(row) == 3 for row in world.state)

def test_build_empty_grid_2d_correct_contents():
    world = World([2, 3])
    assert all(all(cell is None for cell in row) for row in world.state)

def test_get_random_coords_1d():
    world = World([5], seed = 1)
    coords = world.get_random_coords()
    assert coords == (1,)

def test_get_random_coords_2d():
    world = World([2, 3], seed = 1)
    coords = world.get_random_coords()
    assert coords == (0, 2)