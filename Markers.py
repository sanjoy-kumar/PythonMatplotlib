# The keyword argument "marker" to emphasize each point with a specified marker:

# Mark each point with a circle:

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o')
plt.show()


# Mark each point with a star:

plt.plot(ypoints, marker = '*')
plt.show()

# -----------  Format Strings "fmt" -----------------------------

# This parameter is also called fmt, and is written with this syntax:

#      marker|line|color

plt.plot(ypoints, 'o-.r')  # ':'	=> Dotted line; '-' => Solid line ; '--' => Dashed line; '-.' => Dashed/dotted line 
plt.show()

# Note: If you leave out the line value in the fmt parameter, no line will be plottet.


# ------------------------ Marker Size ---------------------------

# The keyword argument markersize or the shorter version, "ms" to set the size of the markers:

plt.plot(ypoints, marker = 'o', ms = 20)
plt.show()

# ------------------------ Marker Color ---------------------------
# The keyword argument markeredgecolor or the shorter "mec" to set the color of the edge of the markers:

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
plt.show()

# The keyword argument markerfacecolor or the shorter "mfc" to set the color inside the edge of the markers:

plt.plot(ypoints, marker = 'D', ms = 20, mfc = 'r')
plt.show()


# Use both the mec and mfc arguments to color of the entire marker:

plt.plot(ypoints, marker = 's', ms = 20, mec = 'r', mfc = 'r')
plt.show()

# Mark each point with a beautiful green color:

plt.plot(ypoints, marker = 'o', ms = 20, mec = '#4CAF50', mfc = '#4CAF50')
plt.show()

# Mark each point with the color named "hotpink":

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'hotpink', mfc = 'hotpink')
plt.show()







