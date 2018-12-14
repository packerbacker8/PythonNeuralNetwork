from random import uniform

def line_func(x):
    # y = mx + b
    return 0.3 * x + 0.2


class Point:
    def __init__(self, x = None, y=None, size = 8):
        if x is None:
            self.x = uniform(-1,1)
        else:
            self.x = x
        if y is None:
            self.y = uniform(-1,1)
        else:
            self.y = y
        self.label = 1 if self.y > line_func(self.x) else -1
        self.size = size
        self.px = width / 2 + self.x * width / 2
        self.py = height / 2 - self.y * height / 2
        self.bias = 1
        
        
    def show(self):
        stroke(0)
        if(self.label == 1):
            fill(255)
        else:
            fill(0)
            
        ellipse(self.px, self.py, self.size, self.size)
