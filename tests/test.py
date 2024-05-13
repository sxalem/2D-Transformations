
#test.py 
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '2D_Transformations')))

import numpy as np
from point2d import Point2D
from translate import Translate
from rotate import Rotate
from transformation import Transformation
import matplotlib.pyplot as plt

# Set up the points
points = [Point2D(2, 4), Point2D(3, 6), Point2D(), Point2D(1, 2)]
for p in points:
    print(p)

# Set up the transformations
t1 = Translate(1, 0)
r1 = Rotate(np.pi/8)
T1 = Transformation(t1, r1)
print(t1, r1, T1)

# Do operations with points
points.sort()
p_total = Point2D()
for p in points:
    p_total = p_total + p
    print(p)
print(p_total)

# Do operations with transformations
print(t1+t1)
print(r1+r1)
for p in points:
    p.plot('r')   # color red
    p_t = t1 * p
    p_t.plot('b') # color blue
    p_r = r1 * p
    p_r.plot('g') # color green
    p_T = T1 * p
    p_T.plot('y') # color yellow

plt.axis('equal')   