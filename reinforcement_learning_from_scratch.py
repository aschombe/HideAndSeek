import numpy as np


# def relu(x):
#     return np.where(x > 0, x, [x, 0])


def relu(x):
    return np.maximum(0, x)


def tanh(x):
    return np.tanh(x)


scalar = 1


class Model:
    def __init__(self) -> None:
        self.weights1 = 2 * (np.random.rand(1, 40) - 0.5)
        self.weights2 = 2 * (np.random.rand(40, 40) - 0.5)
        self.weights3 = 2 * (np.random.rand(40, 40) - 0.5)
        self.weights4 = 2 * (np.random.rand(40, 40) - 0.5)
        self.weights5 = 2 * (np.random.rand(40, 40) - 0.5)
        self.weights6 = 2 * (np.random.rand(40, 40) - 0.5)
        self.weights7 = 2 * (np.random.rand(40, 40) - 0.5)
        self.weights8 = 2 * (np.random.rand(40, 40) - 0.5)
        self.weights9 = 2 * (np.random.rand(40, 40) - 0.5)
        self.weights10 = 2 * (np.random.rand(40, 2) - 0.5)

    # Forward propagation
    def forward(self, time_since_start):
        layer1 = relu(np.dot(time_since_start, self.weights1))
        layer1 = layer1 / (np.linalg.norm(layer1) + 0.0000001)
        layer2 = relu(np.dot(layer1, self.weights2))
        layer2 = layer2 / (np.linalg.norm(layer2) + 0.0000001)
        layer3 = relu(np.dot(layer2, self.weights3))
        layer3 = layer3 / (np.linalg.norm(layer3) + 0.0000001)
        layer4 = relu(np.dot(layer3, self.weights4))
        layer4 = layer4 / (np.linalg.norm(layer4) + 0.0000001)
        layer5 = relu(np.dot(layer4, self.weights5))
        layer5 = layer5 / (np.linalg.norm(layer5) + 0.0000001)
        layer6 = relu(np.dot(layer5, self.weights6))
        layer6 = layer6 / (np.linalg.norm(layer6) + 0.0000001)
        layer7 = relu(np.dot(layer6, self.weights7))
        layer7 = layer7 / (np.linalg.norm(layer7) + 0.0000001)
        layer8 = relu(np.dot(layer7, self.weights8))
        layer8 = layer8 / (np.linalg.norm(layer8) + 0.0000001)
        layer9 = relu(np.dot(layer8, self.weights9))
        layer9 = layer9 / (np.linalg.norm(layer9) + 0.0000001)
        output = tanh(np.dot(layer9, self.weights10))
        output = np.transpose(output)
        return np.squeeze(output[0]) * 50, np.squeeze(output[1])

    def set_weights(self, w1, w2, w3, w4, w5, w6, w7, w8, w9, w10):
        self.weights1 = w1
        self.weights2 = w2
        self.weights3 = w3
        self.weights4 = w4
        self.weights5 = w5
        self.weights6 = w6
        self.weights7 = w7
        self.weights8 = w8
        self.weights9 = w9
        self.weights10 = w10

    def mutate(self):
        m = Model()
        w1 = scalar * np.where(
            2 * (abs(np.random.rand(self.weights1.shape[0], self.weights1.shape[1]) - 0.5) + self.weights1) > 0.2,
            2 * (np.random.rand(self.weights1.shape[0], self.weights1.shape[1]) - 0.5) + self.weights1,
            self.weights1,
        )
        w2 = scalar * np.where(
            abs(2 * (np.random.rand(self.weights2.shape[0], self.weights2.shape[1]) - 0.5)) > 0.2,
            2 * (np.random.rand(self.weights2.shape[0], self.weights2.shape[1]) - 0.5),
            self.weights2,
        )
        w3 = scalar * np.where(
            2 * (abs(np.random.rand(self.weights3.shape[0], self.weights3.shape[1]) - 0.5) + self.weights3) > 0.2,
            2 * (np.random.rand(self.weights3.shape[0], self.weights3.shape[1]) - 0.5) + self.weights3,
            self.weights3,
        )
        w4 = scalar * np.where(
            2 * (abs(np.random.rand(self.weights4.shape[0], self.weights4.shape[1]) - 0.5) + self.weights4) > 0.2,
            2 * (np.random.rand(self.weights4.shape[0], self.weights4.shape[1]) - 0.5) + self.weights4,
            self.weights4,
        )
        w5 = scalar * np.where(
            2 * (abs(np.random.rand(self.weights5.shape[0], self.weights5.shape[1]) - 0.5) + self.weights5) > 0.2,
            2 * (np.random.rand(self.weights5.shape[0], self.weights5.shape[1]) - 0.5) + self.weights5,
            self.weights5,
        )
        w6 = scalar * np.where(
            2 * (abs(np.random.rand(self.weights6.shape[0], self.weights6.shape[1]) - 0.5) + self.weights6) > 0.2,
            2 * (np.random.rand(self.weights6.shape[0], self.weights6.shape[1]) - 0.5) + self.weights6,
            self.weights6,
        )
        w7 = scalar * np.where(
            2 * (abs(np.random.rand(self.weights7.shape[0], self.weights7.shape[1]) - 0.5) + self.weights7) > 0.2,
            2 * (np.random.rand(self.weights7.shape[0], self.weights7.shape[1]) - 0.5) + self.weights7,
            self.weights7,
        )
        w8 = scalar * np.where(
            2 * (abs(np.random.rand(self.weights8.shape[0], self.weights8.shape[1]) - 0.5) + self.weights8) > 0.2,
            2 * (np.random.rand(self.weights8.shape[0], self.weights8.shape[1]) - 0.5) + self.weights8,
            self.weights8,
        )
        w9 = scalar * np.where(
            2 * (abs(np.random.rand(self.weights9.shape[0], self.weights9.shape[1]) - 0.5) + self.weights9) > 0.2,
            2 * (np.random.rand(self.weights9.shape[0], self.weights9.shape[1]) - 0.5) + self.weights9,
            self.weights9,
        )
        w10 = scalar * np.where(
            2 * (abs(np.random.rand(self.weights10.shape[0], self.weights10.shape[1]) - 0.5) + self.weights10) > 0.2,
            2 * (np.random.rand(self.weights10.shape[0], self.weights10.shape[1]) - 0.5) + self.weights10,
            self.weights10,
        )
        m.set_weights(w1, w2, w3, w4, w5, w6, w7, w8, w9, w10)
        return m
