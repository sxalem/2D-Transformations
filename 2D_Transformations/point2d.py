import matplotlib.pyplot as plt

class Point2D:
    points = []  # Class variable to store all points
    colors = []  # Class variable to store corresponding colors

    def __init__(self, x=0, y=0):  # Default values for x and y
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
        Point2D.points.append((self.x, self.y))  # Append point coordinates
        Point2D.colors.append(color)             # Append color

    @classmethod
    def show_plot(cls):
        plt.figure(figsize=(8, 6))  # Set figure size
        
        for i in range(len(cls.points)):
            x, y = cls.points[i]
            color = cls.colors[i]
            plt.plot(x, y, color, marker='o', markersize=8),  # Plot point with larger marker size
            plt.text(x, y, f'({x:.2f}, {y:.2f})', fontsize=12)  # Add text label with larger font size
        
        plt.xlabel('X-axis', fontsize=14)  # Set X-axis label with larger font size
        plt.ylabel('Y-axis', fontsize=14)  # Set Y-axis label with larger font size
        plt.title('2D Points Plot', fontsize=16)  # Set title with larger font size
        plt.grid(True)  # Add grid
        
        # Show plot
        plt.legend(['Original', 'Translated', 'Rotated', 'Transformed'], loc='upper left')
        plt.show()
