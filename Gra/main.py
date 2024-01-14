
def setup_grid():
    grid = [['_' for _ in range(5)] for _ in range(5)]

    init_pos = (0, 0)
    grid[init_pos[0]][init_pos[1]] = 'S'

    target_pos = (4, 4)
    grid[target_pos[0]][target_pos[1]] = 'E'

    return grid, init_pos, target_pos

def display_grid():
    for grid_row in grid:
        print(' '.join(grid_row))

def update_position():

def game_loop():

if __name__ == "__main__":
    game_loop()