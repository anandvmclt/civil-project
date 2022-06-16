import numpy as np
import matplotlib.pyplot as plt

# Dataset for PCI
xp = np.array([0, 5,  10, 15,    20,    25,   30,   35,     40,  45,
              50,   55,  60,   65,   70,   75,     80,   85,  90,   95,  100])
yp1 = np.array([1, 1,  1,  0.83,  0.67,  0.5,  0.33, 0.17,    0,   0,
               0,   0,   0,   0,     0,    0,     0,    0,   0,    0,     0])
yp2 = np.array([0, 0,  0,  0,     0,     0,    0.33, 0.67,    1,  0.67,
               0.33, 0,   0,    0,     0,    0,     0,    0,   0,    0,     0])
yp3 = np.array([0, 0,  0,  0,     0,      0,   0,    0,       0,  0.33,
               0.67, 1,   0.67, 0.33,  0,    0,     0,    0,   0,    0,     0])
yp4 = np.array([0, 0,  0, 0,     0,    0,    0,    0,       0,  0,
               0,    0,   0.33,  0.67, 1,   0.67,  0.33,  0,   0,    0,     0])
yp5 = np.array([0, 0,  0, 0,     0,    0,    0,    0,       0,  0,
               0,    0,   0,     0,    0,    0.33,  0.67, 1,   0.67, 0.33,  0])


# Dataset for PCI
xd = np.array([0,  0.1,    0.2,    0.3,    0.4,    0.5,    0.6,    0.7,    0.8,    0.9,    1,     1.1,    1.2,
              1.3,    1.4,    1.5,    1.6,    1.7,    1.8,    1.9,    2.0,    2.1,    2.2,    2.3,    2.4,    2.5])
yd1 = np.array([1,  1,        1,      1,    0.75,   0.5,    0.25,    0,      0,      0,      0,    0,      0,
               0,      0,      0,     0,       0,     0,       0,     0,      0,      0,      0,      0,      0])
yd2 = np.array([0, 0, 0, 0, 1, 1, 1, 0.75, 0.5, 0.25, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
yd3 = np.array([0, 0, 0, 0, 0, 0.33, 0.67, 1, 1, 1, 0.66,
               0.33, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
yd4 = np.array([0, 0, 0, 0, 0, 0, 0, 0.15, 0.43, 0.71, 1, 0.8,
               0.6, 0.4, 0.2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
yd5 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0.12, 0.25, 0.38,
               0.5, 0.62, 0.75, 0.87, 1, 1, 1, 1, 1, 1, 1, 1,  1, 1])


# Dataset for IRI

xi = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6,
              6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12])
yi1 = np.array([1,  1, 1, 1, 1, 0.75, 0.5, 0.25, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0])
yi2 = np.array([0, 0.12, 0.25, 0.37, 0.5, 0.62, 0.75, 0.87, 1,
               1, 1,  0.5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
yi3 = np.array([0, 0, 0, 0, 0, 0, 0, 0.17, 0.34, 0.5, 0.67, 0.84,
               1, 0.84, 0.67, 0.5, 0.34, 0.17, 0, 0, 0, 0, 0, 0, 0])
yi4 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.17,
               0.34, 0.5, 0.67, 0.84, 1,  0.5, 0, 0, 0, 0, 0])
yi5 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 0.17, 0.34, 0.5, 0.67, 0.83, 1, 0.49, 0])

# Dataset for CVPD
xc = np.array([0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500,
              5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000])
yc1 = np.array([1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
yc2 = np.array([0,  0.33, 0.67, 1,  0.67, 0.33, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
yc3 = np.array([0, 0, 0, 0, 0, 0.25, 0.5, 0.75, 1, 0.75,
               0.5, 0.25, 0, 0, 0, 0, 0, 0, 0, 0, 0])
yc4 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0.25, 0.5,
               0.75, 1, 0.5, 0, 0, 0, 0, 0, 0, 0])
yc5 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
               0.25, 0.5, 0.75, 1, 1, 1, 1, 1, 1])

# Plotting the PCI Graph
# y1val = np.interp(25, xp, yp1)
# plt.plot(xp, yp1, 'r')
# plt.plot(xp, yp2, 'm')
# plt.plot(xp, yp3, 'y')
# plt.plot(xp, yp4, 'b')
# plt.plot(xp, yp5, 'g')
# plt.title("PCI plotted using the given points")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.show()

# Plotting the Deflection Graph
# plt.plot(xd, yd1, 'g')
# plt.plot(xd, yd2, 'b')
# plt.plot(xd, yd3, 'y')
# plt.plot(xd, yd4, 'm')
# plt.plot(xd, yd5, 'r')
# plt.title("Deflection plotted using the given points")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.show()

# # Plotting the Deflection IRI
# plt.plot(xi, yi1, 'g')
# plt.plot(xi, yi2, 'b')
# plt.plot(xi, yi3, 'y')
# plt.plot(xi, yi4, 'm')
# plt.plot(xi, yi5, 'r')
# plt.title("IRI plotted using the given points")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.show()

# Plotting the Deflection CVPD
# plt.plot(xc, yc1, 'g')
# plt.plot(xc, yc2, 'b')
# plt.plot(xc, yc3, 'y')
# plt.plot(xc, yc4, 'm')
# plt.plot(xc, yc5, 'r')
# plt.title("IRI plotted using the given points")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.show()
