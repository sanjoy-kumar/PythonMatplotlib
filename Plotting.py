# Draw a line in a diagram from position (1, 3) to position (8, 10):

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints)
plt.show()


# --------------------- Plotting Without Line --------------------------------

# Draw two points in the diagram, one at position (10, 23) and one in position (18, 30):

xpoints = np.array([10, 18])
ypoints = np.array([23, 30])

plt.plot(xpoints, ypoints, 'o')  # To plot only the markers, you can use shortcut string notation parameter 'o', which means 'rings'.
plt.show()


# ----------------------- Multiple Points -------------------------------------

# Draw a line in a diagram from position (1, 3) to (2, 8) then to (6, 1) and finally to position (8, 10)

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.show()


# ------------------------ Default X-Points ----------------------------------


# If we do not specify the points in the x-axis, they will get the default values 0, 1, 2, 3, (etc. depending on the length of the y-points.


ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints)
plt.show()  

#The x-points in the example above is [0, 1, 2, 3, 4, 5].





