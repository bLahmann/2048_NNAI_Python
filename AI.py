import numpy as np
import copy
import NeuralNetwork as nn

class AI:

    NUM_AIs = 0

    def __init__(self, nn):
        self.nn = nn
        self.id = self.NUM_AIs
        self.NUM_AIs += 1

    def do_move(self, board):

        moves = {0: board.shift_up,
                 1: board.shift_down,
                 2: board.shift_left,
                 3: board.shift_right
                 }

        # Get the board input
        nodes = np.array([board.tiles.flatten()]).T

        # Take the log of the input
        nodes[np.where(nodes == 0)] = 1
        nodes = np.log2(nodes)

        # Propagate
        nodes = self.nn.propagate(nodes)

        # Pick a move
        indexes = np.argsort(nodes, 0)[::-1]
        for i in indexes:
            if moves[i[0]]():
                return True

        return False


    def breed(self, ai):

        child_nn = nn
        for i in range(len(self.nn.weights)):

            mother_weights = copy.deepcopy(self.nn.weights[i])
            father_weights = copy.deepcopy(ai.nn.weights[i])

            # Generate a random mask
            shape = mother_weights.shape
            indexes = np.random.rand(shape[0], shape[1]) > 0.5

            # Zero out values and add
            mother_weights[indexes] = 0.0
            father_weights[np.invert(indexes)] = 0.0
            child_weights = mother_weights + father_weights

            print(mother_weights)
            print(father_weights)
            print(child_weights)

            print(i)

