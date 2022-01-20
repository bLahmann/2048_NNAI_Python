import time

import numpy
import numpy as np
import numpy.random as rng


class Board:

    NUM_TILES = 4
    FOUR_CHANCE = 0.1

    def __init__(self):
        self.tiles = np.zeros((4, 4))
        self.spawn_tile()
        self.spawn_tile()

    def __str__(self):
        return self.tiles.__str__()

    def spawn_tile(self):
        rng.seed(int (time.time()))                     # Set a new random seed
        free_index = numpy.where(self.tiles == 0)       # Identify the free indexes
        i = rng.randint(0, len(free_index[0]))          # Sample one at random

        # Add a 2 or a 4
        if rng.rand() <= self.FOUR_CHANCE:
            self.tiles[free_index[0][i], free_index[1][i]] = 4
        else:
            self.tiles[free_index[0][i], free_index[1][i]] = 2

    def shift_left(self):

        valid_move = False

        # Check for copies first
        for i in range(0, len(self.tiles)):
            last_index = 0
            for j in range(1, len(self.tiles[i])):
                if self.tiles[i][j] != 0:
                    if self.tiles[i][j] == self.tiles[i][last_index]:       # If two non-zero tiles are adjacent
                        valid_move = True
                        self.tiles[i][last_index] *= 2
                        self.tiles[i][j] = 0
                        if last_index + 1 < len(self.tiles[i]):
                            last_index += 1
                    else:
                        last_index = j

        # Now move tiles
        for i in range(0, len(self.tiles)):
            free_index = 0
            for j in range(0, len(self.tiles[i])):
                if self.tiles[i][j] != 0:
                    if j != free_index:
                        valid_move = True
                        self.tiles[i][free_index] = self.tiles[i][j]
                        self.tiles[i][j] = 0
                    free_index += 1

        if valid_move:
            self.spawn_tile()

        return valid_move

    def shift_right(self):

        valid_move = False

        # Check for copies first
        for i in range(0, len(self.tiles)):
            last_index = len(self.tiles[i]) - 1
            for j in range(len(self.tiles[i])-2, -1, -1):
                if self.tiles[i][j] != 0:
                    if self.tiles[i][j] == self.tiles[i][last_index]:       # If two non-zero tiles are adjacent
                        valid_move = True
                        self.tiles[i][last_index] *= 2
                        self.tiles[i][j] = 0
                        if last_index + 1 < len(self.tiles[i]):
                            last_index -= 1
                    else:
                        last_index = j

        # Now move tiles
        for i in range(0, len(self.tiles)):
            free_index = len(self.tiles[i]) - 1
            for j in range(len(self.tiles[i])-1, -1, -1):
                if self.tiles[i][j] != 0:
                    if j != free_index:
                        valid_move = True
                        self.tiles[i][free_index] = self.tiles[i][j]
                        self.tiles[i][j] = 0
                    free_index -= 1

        if valid_move:
            self.spawn_tile()

        return valid_move

    def shift_up(self):

        valid_move = False

        # Check for copies first
        for j in range(0, len(self.tiles)):
            last_index = 0
            for i in range(1, len(self.tiles)):
                if self.tiles[i][j] != 0:
                    if self.tiles[i][j] == self.tiles[last_index][j]:       # If two non-zero tiles are adjacent
                        valid_move = True
                        self.tiles[last_index][j] *= 2
                        self.tiles[i][j] = 0
                        if last_index + 1 < len(self.tiles[i]):
                            last_index += 1
                    else:
                        last_index = i

        # Now move tiles
        for j in range(0, len(self.tiles)):
            free_index = 0
            for i in range(0, len(self.tiles)):
                if self.tiles[i][j] != 0:
                    if i != free_index:
                        valid_move = True
                        self.tiles[free_index][j] = self.tiles[i][j]
                        self.tiles[i][j] = 0
                    free_index += 1

        if valid_move:
            self.spawn_tile()

        return valid_move

    def shift_down(self):

        valid_move = False

        # Check for copies first
        for j in range(0, len(self.tiles)):
            last_index = len(self.tiles) - 1
            for i in range(len(self.tiles)-2, -1, -1):
                if self.tiles[i][j] != 0:
                    if self.tiles[i][j] == self.tiles[last_index][j]:       # If two non-zero tiles are adjacent
                        valid_move = True
                        self.tiles[last_index][j] *= 2
                        self.tiles[i][j] = 0
                        if last_index + 1 < len(self.tiles[i]):
                            last_index -= 1
                    else:
                        last_index = i

        # Now move tiles
        for j in range(0, len(self.tiles)):
            free_index = len(self.tiles) - 1
            for i in range(len(self.tiles)-1, -1, -1):
                if self.tiles[i][j] != 0:
                    if i != free_index:
                        valid_move = True
                        self.tiles[free_index][j] = self.tiles[i][j]
                        self.tiles[i][j] = 0
                    free_index -= 1

        if valid_move:
            self.spawn_tile()

        return valid_move

    def get_score(self):
        return np.sum(self.tiles)
