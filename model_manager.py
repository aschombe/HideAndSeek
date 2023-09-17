import reinforcement_learning_from_scratch as rlfs
import pandas as pd
import numpy as np


class manager:
    def __init__(self, num) -> None:
        self.list = np.array([rlfs.Model() for i in range(num)])
        self.list_fitness = np.array([0 for i in range(num)])

    def mutate_models(self, n=1):
        for j in range(n):
            for i in range(len(self.list)):
                self.list = np.append(self.list, (self.list[i].mutate()))
                self.list_fitness = np.append(self.list_fitness, self.list_fitness[i])

    def get_n_best_models(self, n):
        a = np.argsort(self.list_fitness)
        sorted_list = self.list[a]
        self.list = sorted_list[-n:]
        self.list_fitness = self.list_fitness[a]
        self.list_fitness = self.list_fitness[-n:]

    def update_fitness(self, fitness):
        self.list_fitness += np.array(fitness)
        self.list_fitness /= 2

    def set_fitness(self, fitness):
        self.list_fitness = np.array(fitness)

    def get_fitness(self):
        return self.list_fitness

    def get_models(self):
        return self.list

    def save(self, filename):
        for i, model in enumerate(self.list):
            np.savez(
                filename + str(i),
                model.weights1,
                model.weights2,
                model.weights3,
                model.weights4,
                model.weights5,
                model.weights6,
                model.weights7,
                model.weights8,
                model.weights9,
                model.weights10,
            )

    def load(self, filename):
        i = 0
        while True:
            try:
                data = np.load(filename + str(i) + ".npz")
                self.weights1 = data["arr_0"]
                self.weights2 = data["arr_1"]
                self.weights3 = data["arr_2"]
                self.weights4 = data["arr_3"]
                self.weights5 = data["arr_4"]
                self.weights6 = data["arr_5"]
                self.weights7 = data["arr_6"]
                self.weights8 = data["arr_7"]
                self.weights9 = data["arr_8"]
                self.weights10 = data["arr_9"]
                self.list = np.append(self.list, rlfs.Model())
                self.list[i].set_weights(
                    self.weights1,
                    self.weights2,
                    self.weights3,
                    self.weights4,
                    self.weights5,
                    self.weights6,
                    self.weights7,
                    self.weights8,
                    self.weights9,
                    self.weights10,
                )
                i += 1
            except FileNotFoundError:
                break

    def __len__(self):
        return len(self.list)

    def __getitem__(self, key):
        return self.list[key]
