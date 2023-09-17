import numpy as np


# def relu(x):
#     return np.where(x > 0, x, [x, 0])


def relu(x):
    return np.maximum(0, x)


def tanh(x):
    return np.tanh(x)


scalar = 0.1


class Model:
    def __init__(self) -> None:
        self.weights1 = 2 * (np.random.rand(1, 30) - 0.5)
        self.weights2 = 2 * (np.random.rand(30, 20) - 0.5)
        self.weights3 = 2 * (np.random.rand(20, 30) - 0.5)
        self.weights4 = 2 * (np.random.rand(30, 2) - 0.5)

    # Forward propagation
    def forward(self, time_since_start):
        layer1 = relu(np.dot(time_since_start, self.weights1))
        layer2 = relu(np.dot(layer1, self.weights2))
        layer3 = relu(np.dot(layer2, self.weights3))
        output = tanh(np.dot(layer3, self.weights4))
        output = np.transpose(output)
        return np.squeeze(output[0]) * 50, np.squeeze(output[1])


    def set_weights(self, w1, w2, w3, w4):
        self.weights1 = w1
        self.weights2 = w2
        self.weights3 = w3
        self.weights4 = w4

    def mutate(self):
        m = Model()
        w1 = scalar * 2 * (np.random.rand(self.weights1.shape[0], self.weights1.shape[1]) - 0.5) + self.weights1
        w2 = scalar * 2 * (np.random.rand(self.weights2.shape[0], self.weights2.shape[1]) - 0.5) + self.weights2
        w3 = scalar * 2 * (np.random.rand(self.weights3.shape[0], self.weights3.shape[1]) - 0.5) + self.weights3
        w4 = scalar * 2 * (np.random.rand(self.weights4.shape[0], self.weights4.shape[1]) - 0.5) + self.weights4
        m.set_weights(w1, w2, w3, w4)
        return m

    def save(self, filename):
        np.savez(filename, self.weights1, self.weights2, self.weights3, self.weights4)

    def load(self, filename):
        data = np.load(filename)
        self.weights1 = data["arr_0"]
        self.weights2 = data["arr_1"]
        self.weights3 = data["arr_2"]
        self.weights4 = data["arr_3"]
