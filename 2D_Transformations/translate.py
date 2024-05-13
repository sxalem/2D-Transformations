from point2d import Point2D



class Translate:
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy
    
    def __add__(self, other):
        if isinstance(other, Translate):
            return Translate(self.dx + other.dx, self.dy + other.dy)
        else:
            raise TypeError("Unsupported operand type for +: Translate and {}".format(type(other)))
    
    def __sub__(self, other):
        if isinstance(other, Translate):
            return Translate(self.dx - other.dx, self.dy - other.dy)
        else:
            raise TypeError("Unsupported operand type for -: Translate and {}".format(type(other)))
    
    def __mul__(self, point):
        if isinstance(point, Point2D):
            return Point2D(point.x + self.dx, point.y + self.dy)
        else:
            raise TypeError("Unsupported operand type for *: Translate and {}".format(type(point)))

