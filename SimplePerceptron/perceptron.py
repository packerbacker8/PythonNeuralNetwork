from random import uniform

def sign(n):
    """
    This defines the activation function for our perceptron.
    """
    return 1 if n >= 0 else -1


class Perceptron:
    def __init__(self, num_weights):
        self.weights = []
        self.learning_rate = 0.01
        for i in range(num_weights):
            self.weights.append(uniform(-1,1))

    
    def guess(self, inputs):
        sum = 0
        for i in range(len(self.weights)):
            sum += inputs[i] * self.weights[i]
        return sign(sum)
    
    def guess_line_y(self, x):
        return -self.weights[2] / self.weights[1] - self.weights[0] / self.weights[1] * x
    
    def train(self, inputs, target):
        guess = self.guess(inputs)
        error = target - guess
        
        for i in range(len(self.weights)):
            self.weights[i] += error * inputs[i] * self.learning_rate
