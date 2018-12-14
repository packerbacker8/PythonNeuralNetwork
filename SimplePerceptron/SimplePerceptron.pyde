from perceptron import Perceptron
from training import Point, line_func
from neural_network import NeuralNetwork
from matrix import Matrix

num_points = 1000
points = []
brain = Perceptron(3)
nn_brain = NeuralNetwork(3,3,1)

def doubleIt(val):
    return val * 2

def setup():
    size(600,600)
    m = Matrix(3,2)
    m.randomize()
    print('first matrix\n%s' % m)
    m.apply_func(doubleIt)
    print('first matrix\n%s' % m)
    m2 = Matrix(2,3)
    m2.randomize()
    print('second matrix\n%s' % m2)
    m3 = Matrix.multiply(m, m2)
    print('added matrices\n%s' % m3)
    for i in range(num_points):
        points.append(Point())
    
    background(255)
    stroke(0)
    pt1 = Point(-1, line_func(-1))
    pt2 = Point(1, line_func(1))
    line(pt1.px, pt1.py, pt2.px, pt2.py)
    for poin in points:
        poin.show()

def draw():
    global training_index
    background(255)
    stroke(1)
    pt1 = Point(-1, line_func(-1))
    pt2 = Point(1, line_func(1))
    line(pt1.px, pt1.py, pt2.px, pt2.py)
    brain_line_pt1 = Point(-1, brain.guess_line_y(-1))
    brain_line_pt2 = Point(1, brain.guess_line_y(1))
    line(brain_line_pt1.px, brain_line_pt1.py, brain_line_pt2.px, brain_line_pt2.py)
    for poin in points:
        poin.show()
        target_inputs = [poin.x, poin.y, poin.bias]
        brain.train(target_inputs, poin.label)
        guess = brain.guess(target_inputs)
        if(guess == poin.label):
            fill(0, 255, 0)
        else:
            fill(255, 0, 0)
        noStroke()
        ellipse(poin.px, poin.py, poin.size / 2, poin.size / 2)


# def mousePressed():
#     for poin in points:
#         target_inputs = [poin.x, poin.y, poin.bias]
#         brain.train(target_inputs, poin.label)
#         guess = brain.guess(target_inputs)
#         if(guess == poin.label):
#             fill(0, 255, 0)
#         else:
#             fill(255, 0, 0)
#         noStroke()
#         ellipse(poin.px, poin.py, poin.size / 2, poin.size / 2)
    
def keyPressed():
    if key == 'a':
        for _ in range(1000):
            points.append(Point())
            
