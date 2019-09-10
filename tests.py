import unittest
import numpy as np

from labyrinth import Labyrinth

LABYRINTH_1 = np.array([[1, 1, 0, 1, 0],
                        [0, 1, 1, 1, 0],
                        [0, 0, 0, 0, 0]])

LABYRINTH_2 = np.array([[1, 0, 0, 0, 0],
                        [0, 1, 1, 1, 0],
                        [0, 0, 0, 0, 0]])

LABYRINTH_3 = np.array([[1, 0, 0, 0, 0],
                        [0, 1, 1, 1, 0],
                        [0, 0, 0, 1, 0]])


class TestMinLengthLabyrinth(unittest.TestCase):
    def test_one_min_way(self):
        lab = Labyrinth(LABYRINTH_1, start_point=(1, 3), wall=0, hole=1)
        self.assertEquals(lab.get_len_min_way(), 2)

    def test_no_exit(self):
        lab = Labyrinth(LABYRINTH_2, start_point=(1, 2), wall=0, hole=1)
        self.assertEquals(lab.get_len_min_way(), -1)

    def test_one_way(self):
        lab = Labyrinth(LABYRINTH_3, start_point=(1, 1), wall=0, hole=1)
        self.assertEquals(lab.get_len_min_way(), 4)

    def test_two_min_way(self):
        lab = Labyrinth(LABYRINTH_1, start_point=(1, 2), wall=0, hole=1)
        self.assertEqual(lab.get_len_min_way(), 3)


if __name__ == '__main__':
    unittest.main()
