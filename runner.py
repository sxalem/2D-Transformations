import sys
import os

# Add the directory containing the modules to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '2D_Transformations')))

from point2d import Point2D  # Import the Point2D class

from translate import Translate
from rotate import Rotate
from transformation import Transformation

import numpy as np
import matplotlib.pyplot as plt

# Rest of the script remains unchanged

# Set up the points
points = [Point2D(2, 4), Point2D(3, 6), Point2D(0, 0), Point2D(1, 2)]

# Set up the transformations
t1 = Translate(1, 0)
r1 = Rotate(np.pi/8)
T1 = Transformation(t1, r1)

# Do operations with points
points.sort()
p_total = Point2D(0, 0)
for p in points:
    p_total = p_total + p

# Plotting
for p in points:
    p.plot('r')         # plot original point in red
    p_t = t1 * p
    p_r = r1 * p
    p_T = T1 * p
    
    # Plot points with specified colors
    p_t.plot('b')       # plot translated point in blue
    p_r.plot('g')       # plot rotated point in green
    p_T.plot('y')       # plot transformed point in yellow
    
    # Print point positions
    print("Original Point:", p.x, p.y)
    print("Translated Point:", p_t.x, p_t.y)
    print("Rotated Point:", p_r.x, p_r.y)
    print("Transformed Point:", p_T.x, p_T.y)

# Show all points plotted on the same graph
Point2D.show_plot()
