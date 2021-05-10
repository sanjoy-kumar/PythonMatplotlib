# Draw a line in a diagram from position (0,0) to position (16,350)
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0,16])
ypoints = np.array([0,350])

plt.plot(xpoints,ypoints)
plt.show()
