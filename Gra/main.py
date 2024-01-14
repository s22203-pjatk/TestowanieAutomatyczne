import random

def setup_grid():
    grid = [['_' for _ in range(5)] for _ in range(5)]

    init_pos = (0, 0)
    grid[init_pos[0]][init_pos[1]] = 'S'

    target_pos = (4, 4)
    grid[target_pos[0]][target_pos[1]] = 'E'

    for _ in range(3):
        while True:
            row, col = random.randint(0, 4), random.randint(0, 4)
            if grid[row][col] == '_':
                grid[row][col] = 'X'
                break

    return grid, init_pos, target_pos

def display_grid(grid):
    for grid_row in grid:
        print(' '.join(grid_row))

def update_position(grid, move, pos, init, end):
    row, col = pos
    moves = {'w': (-1, 0), 's': (1, 0), 'a': (0, -1), 'd': (0, 1)}
    delta_row, delta_col = moves.get(move, (0, 0))

    new_row, new_col = row + delta_row, col + delta_col
    if 0 <= new_row < 5 and 0 <= new_col < 5 and grid[new_row][new_col] != 'X':
        grid[row][col] = '_'
        grid[new_row][new_col] = 'S'
        return new_row, new_col
    return row, col

def game_loop():
    grid, player_pos, end_pos = setup_grid()
    while player_pos != end_pos:
        print("\n")
        display_grid(grid)
        move = input("\nMove (W, S, A, D, q to quit): \n --> ").lower()
        
        if move == 'q':
            break
        player_pos = update_position(grid, move, player_pos, player_pos, end_pos)

        if player_pos == end_pos:
            grid[end_pos[0]][end_pos[1]] = '#'
            display_grid(grid)
            print("WIN!")


if __name__ == "__main__":
    game_loop()
