import matplotlib.pyplot as plt

class Point2D:
    points = []  
    colors = []  

    def __init__(self, x=0, y=0):  
        self.x = x
        self.y = y

    def __lt__(self, other):
        if isinstance(other, Point2D):
            return (self.x, self.y) < (other.x, other.y)
        else:
            raise TypeError("Unsupported operand type for <: Point2D and {}".format(type(other)))

    def __add__(self, other):
        if isinstance(other, Point2D):
            return Point2D(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Unsupported operand type for +: Point2D and {}".format(type(other)))

    def __sub__(self, other):
        if isinstance(other, Point2D):
            return Point2D(self.x - other.x, self.y - other.y)
        else:
            raise TypeError("Unsupported operand type for -: Point2D and {}".format(type(other)))

    def plot(self, color='ro'):
        Point2D.points.append((self.x, self.y)) 
        Point2D.colors.append(color)             

    @classmethod
    def show_plot(cls):
        plt.figure(figsize=(8, 6))  
        
        for i in range(len(cls.points)):
            x, y = cls.points[i]
            color = cls.colors[i]
            plt.plot(x, y, color, marker='o', markersize=8),  
            plt.text(x, y, f'({x:.2f}, {y:.2f})', fontsize=12)  
    
        plt.xlabel('X-axis', fontsize=14)  
        plt.ylabel('Y-axis', fontsize=14)  
        plt.title('2D Points Plot', fontsize=16)  
        plt.grid(True)  
        
        
        plt.legend(['Original', 'Translated', 'Rotated', 'Transformed'], loc='lower right')
        plt.show()
