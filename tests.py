import unittest

from labyrinth import Labyrinth


class BaseTestLabyrinth(unittest.TestCase):
    def setUp(self) -> None:
        self.labyrinth = Labyrinth()

    def test_empty_fit(self):
        self.assertFalse(self.labyrinth.fit())

    def test_empty_way(self):
        self.assertEquals(self.labyrinth.get_min_way(), None)

    def test_empty_len_way(self):
        self.assertEquals(self.labyrinth.get_len_min_way(), None)


if __name__ == '__main__':
    unittest.main()
