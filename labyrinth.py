import numpy as np

from itertools import compress


class Labyrinth:
    def __init__(self, labyrinth: np.ndarray, start_point: tuple, wall=0, hole=1):

        self.WALL = -1
        self.HOLE = 0

        self.labyrinth = labyrinth.copy()
        self.labyrinth[labyrinth == wall] = self.WALL
        self.labyrinth[labyrinth == hole] = self.HOLE

        self.start_point = start_point
        self.hight = self.labyrinth.shape[0]
        self.wight = self.labyrinth.shape[1]
        self.out_value_wall = wall
        self.out_value_hole = hole
        self.min_way = None
        self.len_min_way = None

    def get_min_way(self):

        if self.min_way is None:
            self.fit()

        return self.min_way

    def get_len_min_way(self):

        if self.min_way is None and not self.fit():
            return None

        return self.len_min_way

    def fit(self, algorithm='wave'):

        if self.labyrinth is None:
            return False

        if algorithm == 'wave':
            self._wave()

        return True

    @staticmethod
    def _get_adj_points(point: tuple) -> list:
        left = (point[0], (point[1] - 1))
        top = ((point[0] + 1), point[1])
        right = (point[0], (point[1] + 1))
        down = ((point[0] - 1), point[1])
        return [left, top, right, down]

    def _wave(self):
        wave_level = 1
        curr_points = [self.start_point]
        final_points = self._find_final_points()

        if not final_points:
            self.len_min_way = -1
            return

        while all(self._check_holes(final_points)) and curr_points:
            next_points = []
            for point in curr_points:
                adj_points = self._get_adj_points(point)
                tmp_bool = list(map(lambda p: self._wave_pass(p) and p != self.start_point, adj_points))
                good_adj_points = list(compress(adj_points, tmp_bool))
                next_points.extend(good_adj_points)
                for p in good_adj_points:
                    self.labyrinth[p] = wave_level
            curr_points = next_points
            wave_level += 1

        tmp = self._check_holes(final_points)
        exit_points = list(compress(final_points, [not i for i in tmp]))
        if exit_points:
            self.len_min_way = self.labyrinth[exit_points[0]] + 1
            ways = []
            for exit_point in exit_points:
                way, curr_point = [exit_point], exit_point
                while curr_point != self.start_point:
                    adj_points = self._get_adj_points(curr_point)
                    tmp_bool = list(map(lambda p: self._within_maze(p), adj_points))
                    adj_points = list(compress(adj_points, tmp_bool))
                    tmp_bool = list(map(lambda p: self.labyrinth[p] == self.labyrinth[curr_point] - 1, adj_points))
                    curr_point = list(compress(adj_points, tmp_bool))[0]
                    way.append(curr_point)
                ways.append(way[::-1])
            self.min_way = ways
        else:
            self.len_min_way = -1

    def _find_final_points(self) -> list:
        top_line = [(0, i) for i in range(self.wight)]
        down_line = [(self.hight-1, i) for i in range(self.wight)]
        left_column = [(i, 0) for i in range(1, self.hight-1)]
        right_column = [(i, self.wight-1) for i in range(1, self.hight-1)]
        border = top_line + down_line + left_column + right_column
        return [point for point in border if self.labyrinth[point] == 0]

    def _check_holes(self, points: list) -> list:
        return [self.labyrinth[point] == 0 for point in points]

    def _within_maze(self, point: tuple) -> bool:
        return 0 <= point[0] < self.hight and 0 <= point[1] < self.wight

    def _wave_pass(self, point: tuple) -> bool:
        return self._within_maze(point) and self.labyrinth[point] == self.HOLE


if __name__ == '__main__':
    some_labyrinth = np.array([[1, 1, 0, 1, 0],
                               [0, 1, 1, 1, 0],
                               [0, 0, 0, 0, 0]])
    lab = Labyrinth(some_labyrinth, start_point=(1, 2), wall=0, hole=1)
    print(lab.labyrinth)
    #print('Min ways: ', lab.get_min_way())
    print('Min len: ', lab.get_len_min_way())

