# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).
# ----------


# Perceptron implementation
import Helpers.util
from random import uniform


class PerceptronClassifier:

    def __init__( self, legalLabels, max_iterations):
        self.legalLabels = legalLabels
        self.type = "perceptron"
        self.epochs = max_iterations
        self.weights = None 


#ref:
# self.labels
# self.epochs
# self.weights
    def classify(self, data):
        # data is row
        # 2d weights, 10 rows of 784
        # row is 785 long (do one less add at end), weights 785
        sumList = []
        for i in range(10):
            sum = 0
            for l in range(len(data)-1):
                sum += data[l]*self.weights[i][l]
            sum += self.weights[i][-1]
            sumList.append(sum)

        return sumList.index(max(sumList))           

    def train(self, train_data, labels):
        self.weights = []
        for i in range(10):
            add = []
            for j in range(784):
                add.append(uniform(-1,1))
            self.weights.append(add)

        for i in range(self.epochs):
            correct = 0
            total = 0
            for j in range(len(train_data)):
                val = self.classify(train_data[j])
                actual = labels[j]
                if (val == actual):
                    correct += 1
                else:
                    for k in range(len(self.weights[val])):
                        self.weights[val][k] = self.weights[val][k] - train_data[j][k]
                    for k in range(len(self.weights[actual])):
                        self.weights[actual][k] = self.weights[actual][k] + train_data[j][k]
                total += 1
            print("epoch", i, "accuracy: ", correct/total)

        return self.weights
                

    

