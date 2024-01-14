import unittest
from unittest.mock import patch
from main import setup_grid, update_position

class TestSimpleGame(unittest.TestCase):

    def test_board_initialization(self):
        grid, init_pos, target_pos = setup_grid()
        self.assertEqual(len(grid), 5)
        self.assertEqual(grid[init_pos[0]][init_pos[1]], 'S') 
        self.assertEqual(grid[target_pos[0]][target_pos[1]], 'E')
        self.assertEqual(sum(row.count('X') for row in grid), 3)

    def test_player_movement(self):
        grid, player_pos, _ = setup_grid()
        player_pos = (1, 1)
        grid[player_pos[0]][player_pos[1]] = 'S'
        grid[2][1] = '_'
        new_pos = update_position(grid, 's', player_pos, player_pos, player_pos)
        self.assertNotEqual(new_pos, player_pos)

    def test_reaching_the_end(self):
        grid, player_pos, end_pos = setup_grid()
        grid[3][4] = 'S'
        new_pos = update_position(grid, 's', (3, 4), (3, 4), (4, 4))
        self.assertEqual(new_pos, (4, 4))

    def test_avoiding_obstacle(self):
        grid, player_pos, _ = setup_grid()
        grid[0][1] = 'X'
        new_pos = update_position(grid, 'd', player_pos, player_pos, player_pos)
        self.assertEqual(new_pos, player_pos)

    def test_attempt_to_move_out_of_bounds(self):
        grid, player_pos, _ = setup_grid()
        new_pos = update_position(grid, 'w', player_pos, player_pos, player_pos)
        self.assertEqual(new_pos, player_pos)

    def test_obstacle_count(self):
        grid, _, _ = setup_grid()
        obstacle_count = sum(row.count('X') for row in grid)
        self.assertEqual(obstacle_count, 3, "Liczba przeszkód na planszy powinna być równa 3")

    @patch('builtins.input', return_value='x')
    def test_invalid_input(self, mock_input):
        grid, player_pos, end_pos = setup_grid()
        original_pos = player_pos
        new_pos = update_position(grid, 'x', player_pos, player_pos, end_pos)
        self.assertEqual(new_pos, original_pos)

if __name__ == "__main__":
    unittest.main()