import numpy as np
from D_Transformations.point2d import Point2D
#rotate.py

class Rotate:
    def __init__(self, theta):
        self.theta = theta
    
    def __add__(self, other):
        if isinstance(other, Rotate):
            return Rotate(self.theta + other.theta)
        else:
            raise TypeError("Unsupported operand type for +: Rotate and {}".format(type(other)))
    
    def __sub__(self, other):
        if isinstance(other, Rotate):
            return Rotate(self.theta - other.theta)
        else:
            raise TypeError("Unsupported operand type for -: Rotate and {}".format(type(other)))
    
    def __mul__(self, point):
        if isinstance(point, Point2D):
            cos_theta = np.cos(self.theta)
            sin_theta = np.sin(self.theta)
            x = point.x * cos_theta - point.y * sin_theta
            y = point.x * sin_theta + point.y * cos_theta
            return Point2D(x, y)
        else:
            raise TypeError("Unsupported operand type for *: Rotate and {}".format(type(point)))

