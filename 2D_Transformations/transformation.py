from point2d import Point2D
#trasnformation.py

class Transformation:
    def __init__(self, translate, rotate):
        self.translate = translate
        self.rotate = rotate
    
    def __mul__(self, point):
        if isinstance(point, Point2D):
            rotated_point = self.rotate * point
            translated_point = self.translate * rotated_point
            return translated_point
        else:
            raise TypeError("Unsupported operand type for *: Transformation and {}".format(type(point)))

