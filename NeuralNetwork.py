import numpy as np
import numpy.random as rng


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


class NeuralNetwork:

    def __init__(self, layer_sizes):

        self.weights = []
        self.biases = []
        for i in range(1, len(layer_sizes)):
            self.weights.append(rng.randn(layer_sizes[i], layer_sizes[i-1]))
            self.biases.append(rng.randn(layer_sizes[i], 1))

    def propagate(self, nodes):

        for i in range(0, len(self.weights)):
            nodes = np.dot(self.weights[i], nodes) + self.biases[i]
            nodes = sigmoid(nodes)

        return nodes







