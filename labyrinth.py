import numpy as np


class Labyrinth:
    def __init__(self, labyrinth=None):
        if labyrinth is not None and type(labyrinth) is not np.ndarray:
            labyrinth = np.array(labyrinth)

        self.labyrinth = labyrinth
        self.min_way = None

    def get_min_way(self):

        if self.min_way is None:
            self.fit()

        return self.min_way

    def get_len_min_way(self):

        if self.min_way is None and not self.fit():
            return None

        return len(self.min_way)

    def fit(self, algo='wave'):

        if self.labyrinth is None:
            return False

        if algo == 'wave':
            self._wave()

        return True

    def _wave(self):
        pass
