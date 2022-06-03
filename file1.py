import numpy as np
import matplotlib.pyplot as plt

# Dataset
x  =  np.array([0, 5,  10, 15,    20,    25,   30,   35,     40,  45,    50,   55,  60,   65,   70,   75,    80,   85,  90,  95,  100])
y1 =  np.array([1, 1,  1,  0.83,  0.67,  0.5,  0.33, 0.17,    0,   0,    0 ,   0,   0 ,   0,     0,    0,     0,    0,   0,    0,   0])
y2 =  np.array([0, 0,  0,  0,     0,     0,    0.33, 0.67,    1,  0.67,  0.33, 0,   0,    0,     0,    0,     0,    0,   0,    0,   0])
y3 =  np.array([0, 0,  0,  0,     0,      0,   0,    0,       0,  0.33,  0.67, 1,   0.67, 0.33,  0,    0,     0,    0,   0,    0,   0])
y4 =  np.array([0, 0,  0 , 0,     0 ,    0,    0,    0,       0,  0,     0,    0,   0.33,  0.67, 1,   0.67,  0.33,  0,   0,    0,   0])
y5 =  np.array([0, 0,  0 , 0,     0 ,    0,    0,    0,       0,  0,     0,    0,   0,     0,    0,    0.33,   0.67, 1,   0.67, 0.33,0])
a = np.array([10, 30])
b = np.array([10,0])

# Plotting the Graph
y1val = np.interp(25, x,y1)
plt.plot(x, y1, 'r')
plt.plot(x, y2, 'm')
plt.plot(x, y3, 'y')
plt.plot(x, y4, 'b')
plt.plot(x, y5, 'g')
plt.title("PCI plotted using the given points")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

