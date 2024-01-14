import unittest
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
        player_pos = (0, 0)
        grid[player_pos[0]][player_pos[1]] = 'S'
        grid[2][1] = '_'
        new_pos = update_position(grid, 's', player_pos, player_pos, player_pos)
        self.assertNotEqual(new_pos, player_pos)

if __name__ == "__main__":
    unittest.main()
